/* BiLoans.com — calculator suite */
(function () {
  "use strict";
  var cur = "$";
  function $(id) { return document.getElementById(id); }
  function n(id) { var e = $(id); return e ? parseFloat(e.value) || 0 : 0; }
  function money(v, d) { if (!isFinite(v)) return "—"; return cur + v.toLocaleString(undefined, { minimumFractionDigits: d === 0 ? 0 : 2, maximumFractionDigits: d === 0 ? 0 : 2 }); }
  function pct(v) { return isFinite(v) ? v.toFixed(2) + "%" : "—"; }
  function pmt(P, annual, months, perYear) {
    perYear = perYear || 12;
    var r = annual / 100 / perYear;
    if (months <= 0) return 0;
    if (r === 0) return P / months;
    return (P * r * Math.pow(1 + r, months)) / (Math.pow(1 + r, months) - 1);
  }
  function pv(pay, annual, months) { var r = annual / 100 / 12; if (r === 0) return pay * months; return pay * (1 - Math.pow(1 + r, -months)) / r; }
  /* APR: rate at which payments discount to net proceeds */
  function aprFrom(net, pay, periods, perYear) {
    var lo = 0, hi = 5; // periodic up to 500%
    for (var i = 0; i < 200; i++) {
      var mid = (lo + hi) / 2, v = 0;
      v = mid === 0 ? pay * periods : pay * (1 - Math.pow(1 + mid, -periods)) / mid;
      if (v > net) lo = mid; else hi = mid;
    }
    return ((lo + hi) / 2) * perYear * 100;
  }
  function dl(pairs) { return "<dl>" + pairs.map(function (p) { return "<dt>" + p[0] + "</dt><dd>" + p[1] + "</dd>"; }).join("") + "</dl>"; }
  function cta(amount, audience) { return '<a class="btn btn-green btn-block" style="margin-top:18px" href="apply.html?audience=' + (audience || "personal") + "&amount=" + Math.round(amount || 0) + '">Get matched for this loan →</a>'; }

  var calcs = {
    pay: function () {
      var P = n("pay_amount"), r = n("pay_rate"), m = n("pay_term"), f = n("pay_fee");
      var M = pmt(P, r, m), total = M * m, interest = total - P, fee = P * f / 100;
      var apr = f > 0 ? aprFrom(P - fee, M, m, 12) : r;
      var rows = "", bal = P, rr = r / 1200, yi = 0, yp = 0;
      for (var i = 1; i <= m; i++) {
        var it = bal * rr, pr = M - it; bal = Math.max(0, bal - pr); yi += it; yp += pr;
        if (i % 12 === 0 || i === m) { rows += "<tr><td>Year " + Math.ceil(i / 12) + "</td><td>" + money(yp) + "</td><td>" + money(yi) + "</td><td>" + money(bal) + "</td></tr>"; yi = 0; yp = 0; }
      }
      $("pay_out").innerHTML = '<div class="muted" style="color:#C3CEE3">Monthly payment</div><div class="big">' + money(M) + "</div>" +
        dl([["Total interest", money(interest)], ["Origination fee", money(fee)], ["You receive", money(P - fee)], ["Total cost of loan", money(total + (f > 0 ? 0 : 0))], ["Effective APR", pct(apr)]]) + cta(P);
      $("pay_amort").innerHTML = '<div class="table-wrap"><table><thead><tr><th>Period</th><th>Principal</th><th>Interest</th><th>Balance</th></tr></thead><tbody>' + rows + "</tbody></table></div>";
    },
    apr: function () {
      var P = n("apr_amount"), r = n("apr_rate"), m = n("apr_term"), f = n("apr_fee");
      var M = pmt(P, r, m), fee = P * f / 100, apr = aprFrom(P - fee, M, m, 12);
      $("apr_out").innerHTML = '<div class="muted" style="color:#C3CEE3">True APR</div><div class="big">' + pct(apr) + "</div>" +
        dl([["Interest rate", pct(r)], ["Fee cost", money(fee)], ["Net proceeds", money(P - fee)], ["Monthly payment", money(M)], ["Total repaid", money(M * m)]]) +
        '<p style="margin-top:14px;color:#C3CEE3;font-size:.9rem">APR adds upfront fees to the interest rate so you can compare offers like-for-like.</p>' + cta(P);
    },
    afford: function () {
      var pay = n("aff_pay"), r = n("aff_rate"), m = n("aff_term");
      var P = pv(pay, r, m);
      $("aff_out").innerHTML = '<div class="muted" style="color:#C3CEE3">You could borrow about</div><div class="big">' + money(P, 0) + "</div>" +
        dl([["Monthly payment", money(pay)], ["Total repaid", money(pay * m)], ["Total interest", money(pay * m - P)]]) + cta(P);
    },
    dti: function () {
      var inc = n("dti_income");
      var debts = ["dti_housing", "dti_car", "dti_cards", "dti_student", "dti_other", "dti_new"].reduce(function (a, id) { return a + n(id); }, 0);
      var d = inc > 0 ? debts / inc * 100 : 0;
      var verdict = d <= 20 ? ["Excellent", "#12B76A"] : d <= 36 ? ["Good — most lenders approve", "#12B76A"] : d <= 43 ? ["Borderline — some lenders", "#F5A524"] : d <= 50 ? ["High — limited options", "#F5A524"] : ["Very high — reduce debt first", "#E5484D"];
      $("dti_out").innerHTML = '<div class="muted" style="color:#C3CEE3">Debt-to-income ratio</div><div class="big">' + pct(d) + '</div><p style="font-weight:800;color:' + verdict[1] + '">' + verdict[0] + "</p>" +
        dl([["Monthly debts", money(debts)], ["Gross monthly income", money(inc)], ["Room to 36% DTI", money(Math.max(0, inc * .36 - debts))]]) + cta(0);
    },
    consol: function () {
      var B = n("con_balance"), cr = n("con_cur_rate"), cp = n("con_cur_pay"), nr = n("con_new_rate"), nt = n("con_new_term"), fee = n("con_fee");
      // months to pay off current debts
      var r = cr / 1200, months = 0, bal = B, curInt = 0;
      if (cp <= B * r) months = Infinity; else { while (bal > 0.01 && months < 600) { var it = bal * r; curInt += it; bal = bal + it - cp; months++; } }
      var loan = B / (1 - fee / 100), M = pmt(loan, nr, nt), newInt = M * nt - B;
      var save = curInt - newInt;
      $("con_out").innerHTML = '<div class="muted" style="color:#C3CEE3">Estimated savings</div><div class="big" style="color:' + (save >= 0 ? "#6CF0B0" : "#FF8C8C") + '">' + (months === Infinity ? "Payment too low" : money(save)) + "</div>" +
        dl([["Current payoff time", months === Infinity ? "Never" : months + " months"], ["Current total interest", months === Infinity ? "—" : money(curInt)], ["New monthly payment", money(M)], ["New loan size (incl. fee)", money(loan)], ["New total interest + fee", money(newInt)], ["Months saved", months === Infinity ? "—" : (months - nt)]]) + cta(loan);
    },
    biz: function () {
      var P = n("biz_amount"), r = n("biz_rate"), y = n("biz_term"), fq = $("biz_freq").value;
      var per = fq === "daily" ? 252 : fq === "weekly" ? 52 : 12, np = Math.round(y * per);
      var p = pmt(P, r, np, per), total = p * np;
      $("biz_out").innerHTML = '<div class="muted" style="color:#C3CEE3">' + fq.charAt(0).toUpperCase() + fq.slice(1) + ' payment</div><div class="big">' + money(p) + "</div>" +
        dl([["Number of payments", np], ["Total interest", money(total - P)], ["Total repaid", money(total)], ["Approx. monthly cash need", money(p * per / 12)]]) + cta(P, "business");
    },
    sba: function () {
      var P = n("sba_amount"), prime = n("sba_prime"), y = n("sba_term"), gf = n("sba_gfee");
      var spread = P <= 50000 ? 6.5 : P <= 250000 ? 6 : P <= 350000 ? 4.5 : 3;
      var maxRate = prime + spread, M = pmt(P, maxRate, y * 12), fee = P * .75 * gf / 100;
      $("sba_out").innerHTML = '<div class="muted" style="color:#C3CEE3">Max variable rate (prime + ' + spread + '%)</div><div class="big">' + pct(maxRate) + "</div>" +
        dl([["Monthly payment at max rate", money(M)], ["Total interest", money(M * y * 12 - P)], ["Est. SBA guaranty fee*", money(fee)], ["Term", y + " years"]]) +
        '<p style="margin-top:14px;color:#C3CEE3;font-size:.85rem">*Estimated on a 75% guaranteed portion; actual fee depends on loan size, maturity and the current fiscal-year SBA fee schedule. Your lender may charge less than the maximum spread.</p>' + cta(P, "business");
    },
    mca: function () {
      var A = n("mca_amount"), fr = n("mca_factor"), mo = n("mca_months");
      var payback = A * fr, days = Math.max(1, Math.round(mo * 21)), daily = payback / days;
      var apr = aprFrom(A, daily, days, 252);
      $("mca_out").innerHTML = '<div class="muted" style="color:#C3CEE3">Equivalent APR</div><div class="big" style="color:#FFB86B">' + pct(apr) + "</div>" +
        dl([["Total payback", money(payback)], ["Cost of capital", money(payback - A)], ["Daily payment (business days)", money(daily)], ["Business days", days]]) +
        '<p style="margin-top:14px;color:#C3CEE3;font-size:.9rem">Factor rates look small but short terms make the APR high. Compare with a term loan or line of credit.</p>' + cta(A, "business");
    },
    cmp: function () {
      function one(p) { var P = n(p + "_amount"), r = n(p + "_rate"), m = n(p + "_term"), f = n(p + "_fee"); var M = pmt(P, r, m); return { M: M, total: M * m + P * f / 100, apr: aprFrom(P - P * f / 100, M, m, 12) }; }
      var a = one("ca"), b = one("cb"), win = a.total <= b.total ? "A" : "B", diff = Math.abs(a.total - b.total);
      $("cmp_out").innerHTML = '<div class="muted" style="color:#C3CEE3">Cheaper overall</div><div class="big">Offer ' + win + "</div><p>Saves " + money(diff) + " over the life of the loan.</p>" +
        dl([["A — monthly / APR", money(a.M) + " / " + pct(a.apr)], ["A — total cost", money(a.total)], ["B — monthly / APR", money(b.M) + " / " + pct(b.apr)], ["B — total cost", money(b.total)]]) + cta(0);
    }
  };
  window.BL_CALCS = calcs;
  document.addEventListener("DOMContentLoaded", function () {
    var c = $("curr");
    if (c) c.addEventListener("change", function () { cur = c.value; run(); });
    function run() { Object.keys(calcs).forEach(function (k) { if ($(k + "_out")) try { calcs[k](); } catch (e) { } }); }
    document.addEventListener("input", function (e) {
      var p = e.target.closest("[data-calc]"); if (p && calcs[p.getAttribute("data-calc")]) calcs[p.getAttribute("data-calc")]();
      var o = e.target.getAttribute("data-mirror"); if (o && $(o)) $(o).textContent = e.target.value;
    });
    run();
    /* mini hero calculator on home */
    var mh = $("heroCalc");
    if (mh) {
      var upd = function () { var P = n("hc_amt"), r = n("hc_rate"), m = n("hc_term"); $("hc_amt_v").textContent = "$" + P.toLocaleString(); $("hc_term_v").textContent = m + " mo"; $("hc_rate_v").textContent = r + "%"; $("hc_out").textContent = "$" + pmt(P, r, m).toFixed(0); };
      mh.addEventListener("input", upd); upd();
    }
  });
})();
