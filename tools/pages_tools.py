"""Calculators, rates tracker, loans by country."""
from blsite import *  # noqa
ACT = ' class="active"'


def inp(id_, label, val, step="any", mn="0", suffix=""):
    return f'<div class="field"><label for="{id_}">{label}{(" <span class=muted>(" + suffix + ")</span>") if suffix else ""}</label><input id="{id_}" type="number" min="{mn}" step="{step}" value="{val}"></div>'


def calc_panel(key, title, intro, inputs, extra=""):
    return f"""<div class="tabpanel" id="c-{key}"><div class="calc" data-calc="{key}">
<div class="card"><h2 style="font-size:1.5rem">{title}</h2><p class="muted">{intro}</p>{inputs}</div>
<div><div class="result-box" id="{key}_out" aria-live="polite"></div>{extra}</div></div></div>"""


def calculators():
    panels = [
        calc_panel("pay", "Loan payment / EMI calculator", "Monthly payment, total interest and a yearly amortization schedule.",
                   inp("pay_amount", "Loan amount", 15000, "500") + '<div class="row2">' + inp("pay_rate", "Interest rate", 12.5, "0.1", suffix="% per year") + inp("pay_term", "Term", 36, "1", "1", "months") + "</div>" + inp("pay_fee", "Origination fee", 3, "0.1", suffix="% of loan"),
                   '<div id="pay_amort" class="amort"></div>'),
        calc_panel("apr", "APR calculator (rate + fees)", "Convert an interest rate plus upfront fee into a true APR.",
                   inp("apr_amount", "Loan amount", 10000, "500") + '<div class="row2">' + inp("apr_rate", "Interest rate", 13.94, "0.01", suffix="%") + inp("apr_term", "Term", 36, "1", "1", "months") + "</div>" + inp("apr_fee", "Origination fee", 5, "0.1", suffix="%")),
        calc_panel("afford", "How much can I borrow?", "Start with the monthly payment you can comfortably afford.",
                   inp("aff_pay", "Affordable monthly payment", 400, "10") + '<div class="row2">' + inp("aff_rate", "Expected APR", 14, "0.1", suffix="%") + inp("aff_term", "Term", 48, "1", "1", "months") + "</div>"),
        calc_panel("dti", "Debt-to-income (DTI) calculator", "Lenders prefer DTI under 36%; many cap at 43–50%.",
                   inp("dti_income", "Gross monthly income", 5500, "50") + '<div class="row2">' + inp("dti_housing", "Rent / mortgage", 1500, "10") + inp("dti_car", "Auto loans", 350, "10") + "</div>" + '<div class="row2">' + inp("dti_cards", "Credit card minimums", 150, "10") + inp("dti_student", "Student loans", 0, "10") + "</div>" + '<div class="row2">' + inp("dti_other", "Other debts", 0, "10") + inp("dti_new", "Proposed new loan payment", 0, "10") + "</div>"),
        calc_panel("consol", "Debt consolidation savings", "Compare paying off cards as-is versus one consolidation loan.",
                   inp("con_balance", "Total balances to consolidate", 12000, "100") + '<div class="row2">' + inp("con_cur_rate", "Average current APR", 24, "0.1", suffix="%") + inp("con_cur_pay", "Current total monthly payment", 400, "10") + "</div>" + '<div class="row2">' + inp("con_new_rate", "New loan interest rate", 13, "0.1", suffix="%") + inp("con_new_term", "New loan term", 36, "1", "1", "months") + "</div>" + inp("con_fee", "Origination fee", 3, "0.1", suffix="%")),
        calc_panel("biz", "Business loan calculator", "Term-loan payments by monthly, weekly or daily schedule.",
                   inp("biz_amount", "Loan amount", 100000, "1000") + '<div class="row2">' + inp("biz_rate", "Annual interest rate", 11, "0.1", suffix="%") + inp("biz_term", "Term", 3, "0.5", "0.5", "years") + '</div><div class="field"><label for="biz_freq">Payment frequency</label><select id="biz_freq"><option value="monthly">Monthly</option><option value="weekly">Weekly</option><option value="daily">Daily (business days)</option></select></div>'),
        calc_panel("sba", "SBA 7(a) loan calculator", "Estimate the maximum variable rate, payment and guaranty fee.",
                   inp("sba_amount", "Loan amount", 250000, "5000") + '<div class="row2">' + inp("sba_prime", "Prime rate (edit to current)", 7.0, "0.05", suffix="%") + inp("sba_term", "Term", 10, "1", "1", "years") + "</div>" + inp("sba_gfee", "Guaranty fee rate (on guaranteed part)", 2, "0.05", suffix="%")),
        calc_panel("mca", "Merchant cash advance → APR", "See the true annualized cost of a factor-rate advance.",
                   inp("mca_amount", "Advance amount", 50000, "1000") + '<div class="row2">' + inp("mca_factor", "Factor rate", 1.3, "0.01", "1") + inp("mca_months", "Estimated payback period", 8, "1", "1", "months") + "</div>"),
        calc_panel("cmp", "Compare two loan offers", "Enter both offers to see which costs less overall.",
                   '<h3>Offer A</h3><div class="row2">' + inp("ca_amount", "Amount", 15000, "500") + inp("ca_rate", "Rate", 11.5, "0.1", suffix="%") + '</div><div class="row2">' + inp("ca_term", "Term (months)", 60, "1", "1") + inp("ca_fee", "Fee", 6, "0.1", suffix="%") + '</div><h3>Offer B</h3><div class="row2">' + inp("cb_amount", "Amount", 15000, "500") + inp("cb_rate", "Rate", 14, "0.1", suffix="%") + '</div><div class="row2">' + inp("cb_term", "Term (months)", 36, "1", "1") + inp("cb_fee", "Fee", 0, "0.1", suffix="%") + "</div>"),
    ]
    panels[0] = panels[0].replace('class="tabpanel"', 'class="tabpanel active"', 1)
    tabs = [("pay", "Payment / EMI"), ("apr", "APR"), ("afford", "Affordability"), ("dti", "DTI"), ("consol", "Consolidation"), ("biz", "Business loan"), ("sba", "SBA 7(a)"), ("mca", "MCA → APR"), ("cmp", "Offer A vs B")]
    tb = "".join(f'<button type="button" role="tab" data-tab="c-{k}"{ACT if i == 0 else ""}>{l}</button>' for i, (k, l) in enumerate(tabs))
    fq, fs = faq([
        ("Are these calculators accurate?", "They use standard amortization and APR formulas. Results are estimates; lenders may calculate fees, day counts and rounding differently."),
        ("What's the difference between APR and interest rate?", "The interest rate is the cost of borrowing the principal. APR adds mandatory fees such as origination fees, so it reflects the true yearly cost."),
        ("What is EMI?", "Equated Monthly Instalment: the fixed monthly payment, a term widely used in India. It's the same as the monthly payment in our Payment/EMI calculator."),
    ])
    body = page_hero("Free tools", "Loan calculators", "Nine free calculators for personal and business borrowing. Change the currency, adjust the sliders, and carry your numbers straight into a match.", [("Calculators", "")]) + f"""
<section style="padding-top:10px"><div class="container">
 <div style="display:flex;justify-content:space-between;gap:12px;flex-wrap:wrap;align-items:center;margin-bottom:10px">
  <div class="tabs" role="tablist" data-tabs data-hash>{tb}</div>
  <div style="min-width:150px"><label for="curr" class="sr-only">Currency</label><select id="curr"><option value="$">$ USD / CAD</option><option value="₹">₹ INR</option><option value="£">£ GBP</option><option value="€">€ EUR</option></select></div>
 </div>
 {''.join(panels)}
 {ad("inArticle")}
 <div class="narrow" style="margin:40px auto 0"><h2>Calculator FAQ</h2>{fq}</div>
</div></section>
{cta_band()}"""
    write("calculators.html", "Free Loan Calculators: EMI, APR, DTI, SBA, MCA & More | BiLoans",
          "Nine free loan calculators: monthly payment/EMI with amortization, true APR, affordability, debt-to-income, consolidation savings, business loan, SBA 7(a), MCA factor rate and offer comparison.",
          body, schema=[fs], extra_js='<script src="{R}assets/js/calc.js"></script>', priority="0.9")


def rates():
    data = [("Excellent (720+)", 14.96, "#12B76A"), ("Good (690–719)", 19.50, "#1557FF"), ("Fair (630–689)", 23.80, "#F5A524"), ("Poor (under 630)", 27.28, "#E5484D")]
    mx = 30
    bars = ""
    for i, (l, v, c) in enumerate(data):
        y = 20 + i * 62
        w = v / mx * 560
        bars += f'<text x="0" y="{y+24}" font-size="14" fill="currentColor">{l}</text><rect x="170" y="{y}" width="{w:.0f}" height="36" rx="8" fill="{c}"/><text x="{170+w+8:.0f}" y="{y+24}" font-size="15" font-weight="800" fill="currentColor">{v:.2f}%</text>'
    svg = f'<svg viewBox="0 0 800 270" role="img" aria-label="Average personal loan APR by credit band" style="width:100%;height:auto;color:var(--text)">{bars}</svg>'
    biz = [("SBA 7(a), variable", "~9.75%–13.25%"), ("SBA 7(a), fixed", "~11.75%–14.75%"), ("SBA 504", "~5%–7%"), ("SBA microloan", "~8%–13%"),
           ("Bank term loan", "~5.35%–11%"), ("Online term loan", "~10%–36%"), ("Bank line of credit", "~7%–8%+"), ("Online line of credit", "~8%–36%+"),
           ("Equipment financing", "~9.9%–24%"), ("Invoice / receivables financing", "~24%–36%"), ("Revenue-based financing", "~10%–40%")]
    btr = "".join(f"<tr><td>{a}</td><td><strong>{b}</strong></td></tr>" for a, b in biz)
    glob = [("United States", "Personal ~6%–36% APR", "Online lenders, banks, credit unions"), ("Canada", "From ~9% APR; legal cap 35% APR", "Online lenders, banks, credit unions"),
            ("United Kingdom", "Headline from ~5.8% representative APR", "Banks, online lenders"), ("India", "~10%–30% p.a. + 0.5%–4% processing fee", "Banks & RBI-registered NBFCs")]
    gtr = "".join(f"<tr><td><strong>{a}</strong></td><td>{b}</td><td>{c}</td></tr>" for a, b, c in glob)
    body = page_hero("Rate tracker", "Loan rates today", f"Average and typical ranges for personal and business loans, updated {ASOF}. Use them as a benchmark before you accept an offer.", [("Rates", "")]) + f"""
<section style="padding-top:10px"><div class="container">
 <div class="split">
  <div class="chart-wrap"><h2 style="font-size:1.35rem">Average personal loan APR by credit score</h2>{svg}<p class="muted" style="font-size:.85rem">Illustrative averages compiled from publicly reported marketplace data, {ASOF}. Overall average ≈ 19%.</p></div>
  <div><h2 style="font-size:1.35rem">What moves loan rates?</h2>
   <ul><li><strong>Central-bank policy</strong>: Fed, Bank of Canada, Bank of England and RBI decisions shift lender funding costs.</li>
   <li><strong>Your credit profile</strong>: score, DTI and credit history drive the biggest spread (often 10+ points).</li>
   <li><strong>Loan size &amp; term</strong>: longer terms usually carry higher rates.</li>
   <li><strong>Fees</strong>: origination fees of 0–10% raise the APR above the interest rate.</li>
   <li><strong>Collateral / co-signer</strong>: secured and co-signed loans price lower.</li></ul>
   <a class="btn btn-primary" href="{{R}}apply.html">See rates for my profile</a></div>
 </div>
 {ad("inArticle")}
 <h2 style="margin-top:34px">US small-business loan rates</h2>
 <div class="table-wrap"><table><thead><tr><th>Product</th><th>Typical APR / rate</th></tr></thead><tbody>{btr}</tbody></table></div>
 <p class="muted" style="font-size:.85rem;margin-top:8px">Based on a prime rate near 7% (edit the prime in our <a href="{{R}}calculators.html#c-sba">SBA calculator</a>). MCA costs often exceed 40%–100% APR.</p>
 <h2 style="margin-top:34px">International snapshot</h2>
 <div class="table-wrap"><table><thead><tr><th>Country</th><th>Typical personal-loan pricing</th><th>Main lenders</th></tr></thead><tbody>{gtr}</tbody></table></div>
 <div class="notice"><strong>Methodology:</strong> Ranges come from lenders' published APR disclosures and publicly reported marketplace averages, reviewed monthly. They are benchmarks, not offers. <a href="{{R}}how-we-make-money.html#methodology">Read our methodology</a>.</div>
 <div class="card" style="margin-top:26px;display:flex;gap:18px;flex-wrap:wrap;align-items:center;justify-content:space-between">
  <div><h3 style="margin:0">Get rate alerts</h3><p class="muted" style="margin:4px 0 0">We'll email you when average rates move.</p></div>
  <form class="inline-form" data-bl-form="Rate alert signup" data-ok="You're on the rate-alert list." style="flex:1;max-width:460px">{form_extras()}<input type="email" name="email" required placeholder="you@email.com" aria-label="Email"><button class="btn btn-primary">Alert me</button><div class="form-msg" style="flex-basis:100%"></div></form>
 </div>
</div></section>"""
    write("rates.html", f"Personal & Business Loan Rates Today ({ASOF}) | BiLoans",
          f"Average personal loan APR by credit score and typical small-business loan rates for {ASOF}, plus Canada, UK and India snapshots.",
          body, priority="0.8")


def global_page():
    C = [
        ("us", "🇺🇸 United States", "USD", [
            "Personal loans typically $1,000–$100,000, 12–84 months, ~6%–36% APR.",
            "Lenders must give Truth in Lending (TILA) disclosures showing APR and finance charge.",
            "Business owners can access SBA 7(a), 504 and microloans through approved lenders.",
            "Interest-rate caps and licensing vary by state; some lenders don't operate in every state."],
         "Business owners: compare SBA vs online term loans. Individuals: prequalify with several lenders (soft pull) to compare."),
        ("ca", "🇨🇦 Canada", "CAD", [
            "Federal criminal interest-rate cap of 35% APR (since January 2025).",
            "Online lenders from ~9% APR; banks and credit unions often lower for strong credit.",
            "Provinces regulate high-cost credit and payday lending separately.",
            "BDC and the Canada Small Business Financing Program (CSBFP) support small businesses."],
         "Check your Equifax/TransUnion score free before applying; compare credit-union rates."),
        ("uk", "🇬🇧 United Kingdom", "GBP", [
            "Lenders and credit brokers must be FCA-authorised.",
            "Ads must show a Representative APR that at least 51% of accepted applicants receive.",
            "Eligibility checkers use soft searches that don't affect your credit file.",
            "The British Business Bank supports SME finance, including Start Up Loans."],
         "Use eligibility checkers, compare representative APR, and watch for early-repayment charges."),
        ("in", "🇮🇳 India", "INR", [
            "Personal loans from banks and RBI-registered NBFCs, typically ~10%–30% p.a.",
            "Processing fees 0.5%–4%; lenders must give a Key Facts Statement (KFS) with the all-in APR.",
            "Common requirements: PAN, Aadhaar, salary slips / ITR, CIBIL score ~700+.",
            "MSMEs can explore CGTMSE-backed loans, Mudra loans and government schemes."],
         "Compare EMI and the KFS APR, not just the headline rate. Beware of unregistered loan apps."),
    ]
    tabs = "".join(f'<button type="button" data-tab="{k}"{ACT if i == 0 else ""}>{n}</button>' for i, (k, n, *_ ) in enumerate(C))
    panels = ""
    for i, (k, n, cur, pts, tip) in enumerate(C):
        panels += f'<div class="tabpanel{" active" if i == 0 else ""}" id="{k}"><div class="split"><div class="card"><h2>{n}</h2><span class="badge">Currency: {cur}</span><ul style="margin-top:14px">{"".join(f"<li>{p}</li>" for p in pts)}</ul></div><div class="card green"><div class="ico">💡</div><h3>BiLoans tip</h3><p class="muted">{tip}</p><a class="btn btn-primary" href="{{R}}apply.html">Get matched</a> <a class="btn btn-ghost" href="{{R}}calculators.html">Calculators</a></div></div></div>'
    body = page_hero("Global", "Loans by country", "Borrowing rules differ a lot by country. Here's what to know in the US, Canada, UK and India.", [("Loans by country", "")]) + f"""
<section style="padding-top:10px"><div class="container">
 <div class="tabs" data-tabs data-hash>{tabs}</div>{panels}
 {ad("inArticle")}
 <div class="notice blue">Matching partners are currently focused on the United States. Canada, UK and India matching is expanding. Submit a request and we'll tell you what's available where you live. In the UK, BiLoans provides information only and does not broker credit.</div>
</div></section>{cta_band()}"""
    write("global.html", "Loans by Country: US, Canada, UK & India Guide | BiLoans",
          "How personal and business loans work in the United States, Canada, United Kingdom and India: rate caps, regulators, typical APRs and tips.",
          body, priority="0.7")
