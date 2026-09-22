/* BiLoans.com — Get Matched multi-step lead wizard */
(function () {
  "use strict";
  document.addEventListener("DOMContentLoaded", function () {
    var form = document.getElementById("leadForm");
    if (!form) return;
    var S = window.BL_STORE;
    var steps = Array.prototype.slice.call(form.querySelectorAll(".step"));
    var bar = document.getElementById("wizBar");
    var count = document.getElementById("wizCount");
    var back = document.getElementById("wizBack");
    var next = document.getElementById("wizNext");
    var submit = document.getElementById("wizSubmit");
    var idx = 0;

    function audience() { var r = form.querySelector("[name=audience]:checked"); return r ? r.value : "personal"; }
    function visible() {
      var a = audience();
      return steps.filter(function (s) {
        var p = s.getAttribute("data-path") || "all";
        return p === "all" || p === a || (a === "both" && (p === "personal" || p === "business"));
      });
    }
    function show() {
      var v = visible();
      if (idx >= v.length) idx = v.length - 1;
      steps.forEach(function (s) { s.classList.remove("active"); });
      v[idx].classList.add("active");
      var pct = Math.round(((idx + 1) / v.length) * 100);
      bar.style.width = pct + "%";
      count.textContent = "Step " + (idx + 1) + " of " + v.length;
      back.style.visibility = idx === 0 ? "hidden" : "visible";
      var last = idx === v.length - 1;
      next.style.display = last ? "none" : "";
      submit.style.display = last ? "" : "none";
      var f = v[idx].querySelector("input:not([type=hidden]),select,textarea");
      if (f && idx > 0 && window.innerWidth > 760) try { f.focus({ preventScroll: true }); } catch (e) {}
      save();
    }
    function valid(step) {
      var ok = true;
      var fields = step.querySelectorAll("input,select,textarea");
      for (var i = 0; i < fields.length; i++) {
        var f = fields[i];
        if (f.type === "radio") {
          if (f.required && !step.querySelector('[name="' + f.name + '"]:checked')) { ok = false; step.querySelector(".err-note") && (step.querySelector(".err-note").style.display = "block"); break; }
        } else if (!f.checkValidity()) { f.reportValidity(); return false; }
      }
      return ok;
    }
    next.addEventListener("click", function () {
      var v = visible();
      if (!valid(v[idx])) return;
      idx++; show();
      window.scrollTo({ top: form.getBoundingClientRect().top + scrollY - 120, behavior: "smooth" });
    });
    back.addEventListener("click", function () { if (idx > 0) { idx--; show(); } });
    /* auto-advance on tile choice */
    form.addEventListener("change", function (e) {
      if (e.target.type === "radio" && e.target.closest(".tiles[data-auto]")) {
        var n = e.target.closest(".step").querySelector(".err-note"); if (n) n.style.display = "none";
        setTimeout(function () { next.click(); }, 220);
      }
      save();
    });
    form.addEventListener("click", function (e) {
      var lab = e.target.closest(".tiles[data-auto] .tile");
      if (lab && e.target.tagName !== "INPUT") { var ip = lab.querySelector("input"); if (ip && ip.checked) setTimeout(function () { next.click(); }, 220); }
    });
    /* amount slider */
    var amt = document.getElementById("amount"), amtOut = document.getElementById("amountOut");
    function fmt(v) { return "$" + Number(v).toLocaleString(); }
    if (amt) { amt.addEventListener("input", function () { amtOut.textContent = fmt(amt.value); }); }
    var bamt = document.getElementById("bamount"), bamtOut = document.getElementById("bamountOut");
    if (bamt) { bamt.addEventListener("input", function () { bamtOut.textContent = fmt(bamt.value); }); }

    /* prefill from URL / storage */
    var q = new URLSearchParams(location.search);
    try {
      var saved = JSON.parse(S.get("bl-lead", true) || "{}");
      Object.keys(saved).forEach(function (k) { setVal(k, saved[k]); });
    } catch (e) {}
    if (q.get("audience")) setVal("audience", q.get("audience"));
    if (q.get("amount")) { setVal("amount", q.get("amount")); setVal("business_amount", q.get("amount")); }
    if (q.get("purpose")) setVal("purpose", q.get("purpose"));
    if (amt) amtOut.textContent = fmt(amt.value);
    if (bamt) bamtOut.textContent = fmt(bamt.value);

    function setVal(name, val) {
      var els = form.querySelectorAll('[name="' + name + '"]');
      Array.prototype.forEach.call(els, function (el) {
        if (el.type === "radio" || el.type === "checkbox") { if (el.value === val) el.checked = true; }
        else if (el.type !== "hidden" || name === "audience") el.value = val;
      });
    }
    function save() {
      var d = {};
      new FormData(form).forEach(function (v, k) { if (["email", "phone", "first_name", "last_name", "_honey", "consent"].indexOf(k) < 0) d[k] = v; });
      S.set("bl-lead", JSON.stringify(d), true);
    }

    function score() {
      var d = {}; new FormData(form).forEach(function (v, k) { d[k] = v; });
      var s = 0;
      s += { excellent: 30, good: 22, fair: 12, poor: 4, unsure: 8 }[d.credit] || 0;
      var inc = parseFloat(d.income || 0); s += inc >= 100000 ? 25 : inc >= 60000 ? 18 : inc >= 35000 ? 10 : inc > 0 ? 4 : 0;
      s += { "2y+": 20, "1-2y": 14, "6-12m": 7, "<6m": 2 }[d.time_in_business] || 0;
      var rev = parseFloat(d.monthly_revenue || 0); s += rev >= 50000 ? 25 : rev >= 15000 ? 18 : rev >= 5000 ? 10 : rev > 0 ? 3 : 0;
      if (d.employment === "full-time" || d.employment === "self-employed") s += 8;
      var tier = s >= 60 ? "A" : s >= 40 ? "B" : s >= 20 ? "C" : "D";
      return { score: s, tier: tier };
    }

    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var v = visible();
      if (!valid(v[idx])) return;
      if (form.querySelector("[name=_honey]").value) return;
      var vis = visible();
      steps.forEach(function (st) { if (vis.indexOf(st) < 0) Array.prototype.forEach.call(st.querySelectorAll("input,select,textarea"), function (f) { f.disabled = true; }); });
      var sc = score();
      submit.disabled = true; submit.textContent = "Matching…";
      var msg = document.getElementById("wizMsg");
      window.BL_SEND(form, { lead_score: sc.score, lead_tier: sc.tier, _subject: "[BiLoans] NEW LEAD (" + audience() + ", tier " + sc.tier + ")" })
        .then(function () {
          form.style.display = "none";
          document.getElementById("wizIntro") && (document.getElementById("wizIntro").style.display = "none");
          var done = document.getElementById("wizDone"); done.style.display = "block";
          var name = form.querySelector("[name=first_name]").value;
          document.getElementById("doneName").textContent = name ? ", " + name : "";
          try { sessionStorage.removeItem("bl-lead"); } catch (x) {}
          window.scrollTo({ top: 0, behavior: "smooth" });
        })
        .catch(function () {
          steps.forEach(function (st) { Array.prototype.forEach.call(st.querySelectorAll("input,select,textarea"), function (f) { f.disabled = false; }); });
          msg.className = "form-msg err"; msg.textContent = "We couldn't submit just now. Please check your connection and try again.";
          submit.disabled = false; submit.textContent = "See my matches";
        });
    });
    show();
  });
})();
