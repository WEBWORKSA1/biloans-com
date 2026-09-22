"""Core money pages: home, apply, hubs, compare."""
from blsite import *  # noqa


def home():
    fq, fs = faq([
        ("Is BiLoans a lender?", "No. BiLoans is an independent comparison and matching platform. We help you understand options and may connect you with third-party lending partners, who make all credit decisions."),
        ("Does checking my options affect my credit score?", "No. Submitting the BiLoans form does not pull your credit. If you later apply with a lender, that lender may run a hard inquiry, which can affect your score."),
        ("Why Business AND Individual loans in one place?", "Millions of borrowers are both: freelancers, gig workers, sole proprietors and owner-operators. Their finances overlap, so they need to compare personal and business options side by side. BiLoans is built for that."),
        ("How much does BiLoans cost?", "Nothing. BiLoans is free for borrowers. We are supported by advertising, partner compensation and community donations. <a href='{R}how-we-make-money.html'>See how we make money</a>."),
        ("What rates can I expect?", "In " + ASOF + " typical personal-loan APRs run from about 6% to 36%, and online business loans from about 7% to well above 36% depending on product. See <a href='{R}rates.html'>today's rate ranges</a>."),
        ("Which countries do you cover?", "Education and calculators work worldwide. Matching focuses on the United States, with growing coverage for Canada, the United Kingdom and India. See <a href='{R}global.html'>loans by country</a>."),
    ])
    body = f"""
<section class="hero"><div class="container hero-grid">
 <div>
  <span class="eyebrow">Business + Individual loans · free · no credit impact</span>
  <h1>Compare <span>business &amp; personal loans</span> in one place.</h1>
  <p class="lead">Freelancer, founder, or just need cash for life's big moments? BiLoans lets you compare lender types, run the real numbers, and get matched in about 2 minutes.</p>
  <ul class="checks"><li>Won't affect your credit score</li><li>Personal, business, or both</li><li>100% free, no obligation</li></ul>
  <div class="pill-list" style="margin-top:22px">
   <a href="{{R}}apply.html?audience=personal&purpose=debt-consolidation">Debt consolidation</a><a href="{{R}}apply.html?audience=personal&purpose=home-improvement">Home improvement</a>
   <a href="{{R}}apply.html?audience=business&purpose=working-capital">Working capital</a><a href="{{R}}apply.html?audience=business&purpose=equipment">Equipment</a>
   <a href="{{R}}apply.html?audience=both">Self-employed</a></div>
 </div>
 <div class="hero-card">
  <form action="{{R}}apply.html" method="get">
   <div class="seg" data-input="aud" role="group" aria-label="Who is the loan for?">
    <button type="button" class="active" data-val="personal" data-label="How much do you need?">For me</button>
    <button type="button" data-val="business" data-label="How much does your business need?">My business</button>
    <button type="button" data-val="both" data-label="Total amount needed (personal + business)">Both</button>
   </div>
   <input type="hidden" name="audience" id="aud" value="personal">
   <label for="hamt" data-seg-label>How much do you need?</label>
   <select id="hamt" name="amount">
    <option value="2500">Under $5,000</option><option value="7500">$5,000 – $10,000</option><option value="15000" selected>$10,000 – $25,000</option>
    <option value="35000">$25,000 – $50,000</option><option value="75000">$50,000 – $100,000</option><option value="250000">$100,000 – $500,000</option><option value="750000">$500,000+</option>
   </select>
   <button class="btn btn-primary btn-lg btn-block" style="margin-top:16px" type="submit">Check my options →</button>
   <p class="muted center" style="font-size:.82rem;margin:12px 0 0">🔒 256-bit encrypted · No credit pull · 2 minutes</p>
  </form>
  <hr style="border:0;border-top:1px solid var(--line);margin:20px 0">
  <div id="heroCalc">
   <strong>Quick payment estimate</strong>
   <div class="row2" style="margin-top:10px">
    <div><label>Amount <span id="hc_amt_v" class="muted"></span></label><input type="range" id="hc_amt" min="1000" max="100000" step="500" value="15000"></div>
    <div><label>Term <span id="hc_term_v" class="muted"></span></label><input type="range" id="hc_term" min="12" max="84" step="12" value="36"></div>
   </div>
   <label>APR <span id="hc_rate_v" class="muted"></span></label><input type="range" id="hc_rate" min="6" max="36" step="0.5" value="14">
   <p style="margin:12px 0 0">Estimated monthly payment: <strong id="hc_out" style="font-size:1.4rem;color:var(--blue)"></strong></p>
  </div>
 </div>
</div></section>

<section class="section-sm bg-alt"><div class="container grid g4 center">
 <div><div class="stat">2 min</div><div class="muted">to get matched</div></div>
 <div><div class="stat">9</div><div class="muted">free calculators</div></div>
 <div><div class="stat">10+</div><div class="muted">lender types compared</div></div>
 <div><div class="stat">$0</div><div class="muted">cost to you, ever</div></div>
</div></section>

<div class="container">{ad("header")}</div>

<section><div class="container">
 <div class="head"><span class="eyebrow">Two paths, one platform</span><h2>What are you borrowing for?</h2><p class="lead">Most sites make you choose. BiLoans lets you compare both, especially if you're self-employed.</p></div>
 <div class="split">
  <div class="path-card p reveal"><span class="badge" style="background:rgba(255,255,255,.2);color:#fff">Individual</span><h3 style="font-size:1.6rem;margin-top:12px">Personal loans</h3>
   <ul><li>Debt consolidation &amp; credit-card payoff</li><li>Home improvement &amp; major purchases</li><li>Medical, moving, wedding &amp; emergencies</li><li>$1,000 – $100,000 · 12–84 month terms</li></ul>
   <a class="btn btn-white" href="{{R}}personal-loans.html">Explore personal loans</a> <a class="btn" style="color:#fff;border-color:rgba(255,255,255,.5)" href="{{R}}apply.html?audience=personal">Get matched</a></div>
  <div class="path-card b reveal"><span class="badge" style="background:rgba(255,255,255,.2);color:#fff">Business</span><h3 style="font-size:1.6rem;margin-top:12px">Business loans</h3>
   <ul><li>Working capital &amp; lines of credit</li><li>SBA 7(a), 504 &amp; microloans</li><li>Equipment, invoice &amp; revenue-based financing</li><li>$5,000 – $5 million · startups welcome</li></ul>
   <a class="btn btn-white" href="{{R}}business-loans.html">Explore business loans</a> <a class="btn" style="color:#fff;border-color:rgba(255,255,255,.5)" href="{{R}}apply.html?audience=business">Get matched</a></div>
 </div>
</div></section>

<section class="bg-alt"><div class="container">
 <div class="head"><span class="eyebrow">How it works</span><h2>Matched in three simple steps</h2></div>
 <div class="steps">
  <div class="card reveal"><h3>Tell us what you need</h3><p class="muted">Answer a few quick questions about the loan, your credit range and income or revenue. No documents, no credit pull.</p></div>
  <div class="card reveal"><h3>Compare real options</h3><p class="muted">We show which lender types fit your profile and route your request to relevant partners where available.</p></div>
  <div class="card reveal"><h3>Choose with confidence</h3><p class="muted">Review offers on the lender's own site, check the APR and fees with our calculators, and only then decide.</p></div>
 </div>
 <p class="center" style="margin-top:28px"><a class="btn btn-primary btn-lg" href="{{R}}apply.html">Start now: it's free</a></p>
</div></section>

<section><div class="container">
 <div class="head"><span class="eyebrow">Market snapshot · <span data-rates-asof>{ASOF}</span></span><h2>Typical rate ranges right now</h2><p class="lead">Illustrative ranges from public lender disclosures. Your rate depends on your profile.</p></div>
 <div class="grid g4">
  <div class="card rate-card reveal"><span class="badge">Personal · excellent credit</span><div class="big">~7–15%</div><p class="muted">APR, 720+ score</p></div>
  <div class="card rate-card reveal"><span class="badge">Personal · fair credit</span><div class="big">~18–30%</div><p class="muted">APR, 630–689 score</p></div>
  <div class="card rate-card reveal green"><span class="badge green">SBA 7(a)</span><div class="big">~10–15%</div><p class="muted">Variable/fixed, capped by SBA</p></div>
  <div class="card rate-card reveal amber"><span class="badge amber">Online business</span><div class="big">~10–36%+</div><p class="muted">Term loans &amp; lines of credit</p></div>
 </div>
 <p class="center" style="margin-top:22px"><a href="{{R}}rates.html">See the full rate tracker →</a></p>
</div></section>

<section class="bg-alt"><div class="container">
 <div class="head"><span class="eyebrow">Free tools</span><h2>Run the numbers before you borrow</h2></div>
 <div class="grid g4">
  <a class="card reveal" href="{{R}}calculators.html#c-pay"><div class="ico">🧮</div><h3>Payment / EMI</h3><p class="muted">Monthly payment with a full amortization schedule.</p></a>
  <a class="card reveal" href="{{R}}calculators.html#c-apr"><div class="ico">📊</div><h3>True APR</h3><p class="muted">See how origination fees change the real cost.</p></a>
  <a class="card reveal green" href="{{R}}calculators.html#c-consol"><div class="ico">💳</div><h3>Consolidation savings</h3><p class="muted">Will one loan beat your credit-card interest?</p></a>
  <a class="card reveal amber" href="{{R}}calculators.html#c-mca"><div class="ico">⚠️</div><h3>MCA → APR</h3><p class="muted">Convert a factor rate into an honest APR.</p></a>
  <a class="card reveal" href="{{R}}calculators.html#c-afford"><div class="ico">🏦</div><h3>How much can I borrow?</h3><p class="muted">Work backward from a payment you can afford.</p></a>
  <a class="card reveal" href="{{R}}calculators.html#c-dti"><div class="ico">⚖️</div><h3>Debt-to-income</h3><p class="muted">The ratio lenders check first.</p></a>
  <a class="card reveal green" href="{{R}}calculators.html#c-sba"><div class="ico">🏛️</div><h3>SBA 7(a)</h3><p class="muted">Max rate caps, payments and guaranty fee.</p></a>
  <a class="card reveal amber" href="{{R}}calculators.html#c-cmp"><div class="ico">🆚</div><h3>Offer A vs B</h3><p class="muted">Pick the cheaper loan in seconds.</p></a>
 </div>
</div></section>

<section><div class="container">
 <div class="head"><span class="eyebrow">Compare</span><h2>Which lender type fits you?</h2></div>
 <div class="table-wrap"><table>
  <thead><tr><th>Lender type</th><th>Typical APR</th><th>Speed</th><th>Best for</th></tr></thead>
  <tbody>
   <tr><td><strong>Online personal lenders</strong></td><td>~6–36%</td><td>1–3 days</td><td>Fast consolidation, good–fair credit</td></tr>
   <tr><td><strong>Credit unions</strong></td><td>~7–18%</td><td>2–7 days</td><td>Lowest rates if you're a member</td></tr>
   <tr><td><strong>SBA lenders</strong></td><td>~10–15%</td><td>30–90 days</td><td>Established businesses, long terms</td></tr>
   <tr><td><strong>Fintech lines of credit</strong></td><td>~8–36%+</td><td>1–2 days</td><td>Cash-flow gaps, repeat draws</td></tr>
   <tr class="featured"><td><strong>Featured partner slot</strong> <span class="badge amber">Available</span></td><td>—</td><td>—</td><td><a href="{{R}}advertise.html">Advertise your offer here →</a></td></tr>
  </tbody></table></div>
 <p class="center" style="margin-top:20px"><a class="btn btn-ghost" href="{{R}}compare.html">Full comparison table →</a></p>
</div></section>

<section class="bg-alt"><div class="container">
 <div class="head"><span class="eyebrow">Watch &amp; learn</span><h2>Loan explainers in minutes</h2></div>
 <div data-featured-video style="max-width:860px;margin:0 auto 26px"></div>
 <div class="grid g3">
  {video_card("Personal loans explained for beginners", "personal loans explained")}
  {video_card("SBA loans: how to qualify", "SBA 7a loan how to qualify", "g")}
  {video_card("APR vs interest rate", "APR vs interest rate explained", "a", "5 min")}
 </div>
 <p class="center" style="margin-top:22px"><a href="{{R}}videos.html">Browse the video hub →</a></p>
</div></section>

<section><div class="container">
 <div class="head"><span class="eyebrow">Guides</span><h2>Borrow smarter</h2></div>
 <div class="grid g3">
  <a class="card reveal" href="{{R}}guides/personal-loan-guide.html"><span class="badge">Personal</span><h3 style="margin-top:10px">Personal loans: the complete guide</h3><p class="muted">Rates, fees, eligibility and how to pick the right lender.</p></a>
  <a class="card reveal" href="{{R}}guides/business-loan-types.html"><span class="badge green">Business</span><h3 style="margin-top:10px">11 types of business loans compared</h3><p class="muted">Term loans, SBA, lines of credit, equipment, invoice and more.</p></a>
  <a class="card reveal" href="{{R}}guides/self-employed-loans.html"><span class="badge amber">Both</span><h3 style="margin-top:10px">Loans for the self-employed</h3><p class="muted">Personal or business loan? How to qualify with 1099 income.</p></a>
 </div>
</div></section>

<div class="container">{ad("inArticle")}</div>

<section class="bg-navy"><div class="container">
 <div class="head"><span class="eyebrow" style="background:rgba(255,255,255,.12);color:#fff">Community</span><h2>Built with, and for, borrowers</h2><p class="lead">BiLoans is independent. Support it, win prizes, or join the team.</p></div>
 <div class="grid g3">
  <a class="card" href="{{R}}support.html"><div class="ico">💙</div><h3>Support BiLoans</h3><p class="muted">Donate to keep tools free and fund education, marketing and new talent.</p></a>
  <a class="card green" href="{{R}}contests.html"><div class="ico">🏆</div><h3>Contests &amp; prizes</h3><p class="muted">Share your debt-freedom story or budget hack and win cash prizes.</p></a>
  <a class="card amber" href="{{R}}careers.html"><div class="ico">🚀</div><h3>Join the team</h3><p class="muted">Writers, finance reviewers, video creators and ambassadors wanted.</p></a>
 </div>
</div></section>

<section><div class="container narrow">
 <div class="head"><span class="eyebrow">FAQ</span><h2>Common questions</h2></div>
 {fq}
</div></section>

<section class="section-sm"><div class="container"><div class="card" style="display:flex;gap:20px;align-items:center;justify-content:space-between;flex-wrap:wrap">
 <div><h3 style="margin:0">Get the monthly rate report</h3><p class="muted" style="margin:4px 0 0">Rate moves, new tools and money-saving tips. One email a month.</p></div>
 <form class="inline-form" data-bl-form="Newsletter" data-ok="You're subscribed. Watch your inbox!" style="flex:1;max-width:480px">{form_extras()}
  <input type="email" name="email" placeholder="you@email.com" required aria-label="Email"><button class="btn btn-primary" type="submit">Subscribe</button><div class="form-msg" style="flex-basis:100%"></div></form>
</div></div></section>
{cta_band()}
<div class="modal" id="exitModal" role="dialog" aria-label="Before you go"><div class="box"><button class="x" aria-label="Close">×</button>
 <h3>Before you go: free 2026 rate guide</h3><p class="muted">Get our cheat-sheet of typical APRs by credit score and the 7 fees lenders don't advertise.</p>
 <form data-bl-form="Exit-intent guide request" data-ok="Sent! Check your inbox shortly.">{form_extras()}<div class="field"><input type="email" name="email" placeholder="you@email.com" required aria-label="Email"></div>
 <button class="btn btn-primary btn-block" type="submit">Send me the guide</button><div class="form-msg"></div></form></div></div>
"""
    write("index.html", "BiLoans: Compare Business & Personal Loans in One Place",
          "Compare personal and business loans side by side, run free loan calculators, and get matched with lending partners in 2 minutes. No credit impact.",
          body, schema=[fs], extra_js='<script src="{R}assets/js/calc.js"></script>', priority="1.0")


def tile(name, val, icon, label, req=True):
    return f'<label class="tile"><input type="radio" name="{name}" value="{val}"{" required" if req else ""}><span><em>{icon}</em>{label}</span></label>'


def apply_page():
    T = tile
    body = f"""
<section class="page-hero" style="padding-bottom:10px"><div class="container center" id="wizIntro">
 <span class="eyebrow">Free · No credit pull · ~2 minutes</span>
 <h1>Get matched with the right loan</h1>
 <p class="lead" style="max-width:640px;margin:0 auto">Personal, business, or both: answer a few questions and we'll show you the best-fit options and connect you with lending partners where available.</p>
</div></section>
<section style="padding-top:20px"><div class="container">
<div class="wizard">
 <div class="form-card">
 <form id="leadForm" data-bl-form="Lead" novalidate>
  {form_extras()}
  <div style="display:flex;justify-content:space-between;font-size:.85rem" class="muted"><span id="wizCount">Step 1</span><span>🔒 Secure &amp; private</span></div>
  <div class="progress" aria-hidden="true"><i id="wizBar"></i></div>

  <div class="step" data-path="all"><h2>Who is this loan for?</h2><p class="muted">Pick "Both" if you're self-employed or need personal and business funding.</p>
   <div class="tiles" data-auto>{T("audience","personal","👤","Me (personal)")}{T("audience","business","🏢","My business")}{T("audience","both","🔀","Both")}</div><p class="err-note muted" style="display:none;color:var(--red)">Please choose one.</p></div>

  <div class="step" data-path="personal"><h2>What's the personal loan for?</h2>
   <div class="tiles" data-auto>{T("purpose","debt-consolidation","💳","Debt consolidation")}{T("purpose","credit-card-payoff","🧾","Credit card payoff")}{T("purpose","home-improvement","🔨","Home improvement")}{T("purpose","major-purchase","🛒","Major purchase")}{T("purpose","medical","🩺","Medical")}{T("purpose","auto","🚗","Car / auto")}{T("purpose","moving","📦","Moving")}{T("purpose","wedding","💍","Wedding")}{T("purpose","emergency","🆘","Emergency")}{T("purpose","other","✨","Other")}</div>
   <p class="err-note" style="display:none;color:var(--red)">Please choose one.</p></div>

  <div class="step" data-path="personal"><h2>How much do you need?</h2>
   <div class="amount-out" id="amountOut">$15,000</div>
   <input type="range" id="amount" name="amount" min="1000" max="100000" step="500" value="15000" aria-label="Loan amount">
   <div style="display:flex;justify-content:space-between" class="muted"><span>$1,000</span><span>$100,000</span></div>
   <div class="field" style="margin-top:18px"><label for="term">Preferred term</label><select id="term" name="term"><option>12 months</option><option>24 months</option><option selected>36 months</option><option>48 months</option><option>60 months</option><option>72+ months</option><option>Not sure</option></select></div></div>

  <div class="step" data-path="all"><h2>What's your credit score range?</h2><p class="muted">An estimate is fine. We never pull your credit.</p>
   <div class="tiles" data-auto>{T("credit","excellent","🌟","Excellent 720+")}{T("credit","good","👍","Good 690–719")}{T("credit","fair","🙂","Fair 630–689")}{T("credit","poor","🧱","Poor below 630")}{T("credit","unsure","❓","Not sure")}</div>
   <p class="err-note" style="display:none;color:var(--red)">Please choose one.</p></div>

  <div class="step" data-path="personal"><h2>Employment &amp; income</h2>
   <div class="field"><label for="employment">Employment status</label><select id="employment" name="employment" required><option value="">Select…</option><option value="full-time">Employed full-time</option><option value="part-time">Employed part-time</option><option value="self-employed">Self-employed / freelancer</option><option value="retired">Retired</option><option value="other">Other</option></select></div>
   <div class="row2"><div class="field"><label for="income">Annual income (before tax)</label><input id="income" name="income" type="number" min="0" step="1000" placeholder="e.g. 65000" required></div>
   <div class="field"><label for="housing">Housing</label><select id="housing" name="housing"><option>Rent</option><option>Own with mortgage</option><option>Own outright</option><option>Other</option></select></div></div></div>

  <div class="step" data-path="business"><h2>What does your business need funding for?</h2>
   <div class="tiles" data-auto>{T("business_purpose","working-capital","💵","Working capital")}{T("business_purpose","expansion","📈","Expansion")}{T("business_purpose","equipment","⚙️","Equipment")}{T("business_purpose","inventory","📦","Inventory")}{T("business_purpose","payroll","👥","Payroll")}{T("business_purpose","real-estate","🏬","Real estate")}{T("business_purpose","refinance","🔁","Refinance debt")}{T("business_purpose","startup","🚀","Start a business")}</div>
   <p class="err-note" style="display:none;color:var(--red)">Please choose one.</p></div>

  <div class="step" data-path="business"><h2>How much funding?</h2>
   <div class="amount-out" id="bamountOut">$50,000</div>
   <input type="range" id="bamount" name="business_amount" min="5000" max="2000000" step="5000" value="50000" aria-label="Business funding amount">
   <div style="display:flex;justify-content:space-between" class="muted"><span>$5,000</span><span>$2,000,000+</span></div>
   <div class="field" style="margin-top:18px"><label for="speed">How soon do you need it?</label><select id="speed" name="speed"><option>Within 48 hours</option><option selected>Within 2 weeks</option><option>Within a month</option><option>Just exploring</option></select></div></div>

  <div class="step" data-path="business"><h2>How long have you been in business?</h2>
   <div class="tiles" data-auto>{T("time_in_business","<6m","🌱","Less than 6 months")}{T("time_in_business","6-12m","🌿","6–12 months")}{T("time_in_business","1-2y","🌳","1–2 years")}{T("time_in_business","2y+","🏆","2+ years")}</div>
   <p class="err-note" style="display:none;color:var(--red)">Please choose one.</p></div>

  <div class="step" data-path="business"><h2>About your business</h2>
   <div class="row2"><div class="field"><label for="rev">Average monthly revenue</label><input id="rev" name="monthly_revenue" type="number" min="0" step="500" placeholder="e.g. 20000" required></div>
   <div class="field"><label for="entity">Business structure</label><select id="entity" name="entity"><option>Sole proprietor</option><option>LLC</option><option>Corporation</option><option>Partnership</option><option>Not registered yet</option></select></div></div>
   <div class="row2"><div class="field"><label for="industry">Industry</label><select id="industry" name="industry"><option>Retail / e-commerce</option><option>Restaurant / food</option><option>Construction / trades</option><option>Healthcare</option><option>Transportation / trucking</option><option>Professional services</option><option>Tech / online</option><option>Manufacturing</option><option>Real estate</option><option>Other</option></select></div>
   <div class="field"><label for="bname">Business name (optional)</label><input id="bname" name="business_name" type="text" autocomplete="organization"></div></div></div>

  <div class="step" data-path="all"><h2>Where are you located?</h2>
   <div class="row2"><div class="field"><label for="country">Country</label><select id="country" name="country"><option>United States</option><option>Canada</option><option>United Kingdom</option><option>India</option><option>Other</option></select></div>
   <div class="field"><label for="zip">ZIP / postal / PIN code</label><input id="zip" name="postal_code" type="text" autocomplete="postal-code" required></div></div>
   <div class="field"><label for="dob">Date of birth</label><input id="dob" name="date_of_birth" type="date" required><small class="muted">You must be 18+ (21+ in some regions).</small></div></div>

  <div class="step" data-path="all"><h2>Where should we send your matches?</h2>
   <div class="row2"><div class="field"><label for="fn">First name</label><input id="fn" name="first_name" autocomplete="given-name" required></div>
   <div class="field"><label for="ln">Last name</label><input id="ln" name="last_name" autocomplete="family-name" required></div></div>
   <div class="row2"><div class="field"><label for="em">Email</label><input id="em" name="email" type="email" autocomplete="email" required></div>
   <div class="field"><label for="ph">Mobile phone</label><input id="ph" name="phone" type="tel" autocomplete="tel" minlength="7" required></div></div>
   <label class="consent"><input type="checkbox" name="consent" value="yes" required><span>By clicking "See my matches", I agree to the BiLoans <a href="terms.html" target="_blank">Terms</a> and <a href="privacy.html" target="_blank">Privacy Policy</a>, and I give my express written consent for BiLoans and its lending and marketing partners to contact me about my request at the number and email provided, including by autodialed or prerecorded calls and text messages. Message/data rates may apply. Consent is not a condition of any purchase. I understand BiLoans is not a lender and submitting this request does not guarantee an offer.</span></label>
   <label class="consent" style="margin-top:10px"><input type="checkbox" name="marketing_opt_in" value="yes"><span>Also send me the monthly rate report and money tips (optional).</span></label>
   <div class="form-msg" id="wizMsg"></div></div>

  <div class="wiz-nav">
   <button type="button" class="btn btn-ghost" id="wizBack">← Back</button>
   <button type="button" class="btn btn-primary" id="wizNext">Continue →</button>
   <button type="submit" class="btn btn-green" id="wizSubmit" style="display:none">See my matches</button>
  </div>
  <div class="assure"><span>✓ No credit pull</span><span>✓ Free, no obligation</span><span>✓ 256-bit encryption</span><span>✓ We never sell data without consent</span></div>
 </form>
 <div id="wizDone" style="display:none" class="center">
  <div style="font-size:3rem">🎉</div><h2>You're all set<span id="doneName"></span>!</h2>
  <p class="lead">Your request is in. A BiLoans specialist or matched partner will reach out shortly, usually within one business day.</p>
  <div class="notice blue" style="text-align:left"><strong>While you wait:</strong><ul style="margin:8px 0 0"><li>Compare APRs, not just interest rates: <a href="calculators.html#c-apr">APR calculator</a></li><li>Check your debt-to-income: <a href="calculators.html#c-dti">DTI calculator</a></li><li>Never pay an upfront fee to get a loan: <a href="guides/avoid-loan-scams.html">spot loan scams</a></li></ul></div>
  <p><a class="btn btn-primary" href="index.html">Back to home</a> <a class="btn btn-ghost" href="support.html">Support BiLoans</a></p>
 </div>
 </div>
 <p class="disclosure" style="margin-top:18px">BiLoans is not a lender and does not make credit decisions. Submitting a request does not guarantee you will be matched, receive an offer, or be approved. Lenders may perform a hard credit inquiry if you choose to apply with them. Rates, terms and availability vary by lender and location. Loans are not available in all states, provinces or countries.</p>
</div>
</div></section>
"""
    write("apply.html", "Get Matched: Personal & Business Loan Options | BiLoans",
          "Answer a few questions and get matched with personal or business loan options in about 2 minutes. Free, no obligation, no credit pull.",
          body, extra_js='<script src="{R}assets/js/apply.js"></script>', priority="0.9")


def personal():
    fq, fs = faq([
        ("What credit score do I need for a personal loan?", "Many online lenders accept scores from about 580–600, but the best rates generally require 720+. Credit unions and secured loans can help if your score is lower."),
        ("How fast can I get a personal loan?", "Online lenders often fund within 1–3 business days after approval, and some the next day. Banks and credit unions can take up to a week."),
        ("What is an origination fee?", "An upfront fee (typically 0–10% of the loan) usually deducted from the amount you receive. It is included in the APR, which is why comparing APRs matters."),
        ("Can I use a personal loan for my business?", "Some lenders allow it, many don't. If you're self-employed, compare both paths. See our <a href='{R}guides/self-employed-loans.html'>self-employed guide</a>."),
        ("Will prequalifying hurt my credit?", "Prequalification usually uses a soft inquiry, which does not affect your score. A formal application typically triggers a hard inquiry."),
    ])
    rows = [("Excellent (720–850)", "~7%–15%", "Widest choice, lowest fees"), ("Good (690–719)", "~14%–22%", "Most online lenders"),
            ("Fair (630–689)", "~18%–30%", "Online lenders, credit unions"), ("Poor (300–629)", "~25%–36%", "Secured / co-signed loans, credit unions")]
    tr = "".join(f"<tr><td><strong>{a}</strong></td><td>{b}</td><td>{c}</td></tr>" for a, b, c in rows)
    body = page_hero("Individual loans", "Personal loans: compare &amp; get matched",
                     "Consolidate debt, fund a project, or cover the unexpected. Understand rates, fees and eligibility, then compare lender types that fit your credit.", [("Personal loans", "")]) + f"""
<section style="padding-top:10px"><div class="container">
 <p class="disclosure">Advertiser disclosure: BiLoans may be compensated by partners. This does not influence our editorial content. <a href="{{R}}how-we-make-money.html">Learn more</a>. BiLoans is not a lender.</p>
 <div class="grid g4" style="margin-top:26px">
  <a class="card" href="{{R}}guides/debt-consolidation-loans.html"><div class="ico">💳</div><h3>Debt consolidation</h3><p class="muted">Roll high-interest balances into one fixed payment.</p></a>
  <a class="card" href="{{R}}apply.html?audience=personal&purpose=home-improvement"><div class="ico">🔨</div><h3>Home improvement</h3><p class="muted">Renovate without tapping home equity.</p></a>
  <a class="card" href="{{R}}apply.html?audience=personal&purpose=medical"><div class="ico">🩺</div><h3>Medical &amp; emergency</h3><p class="muted">Cover urgent costs with a fixed plan.</p></a>
  <a class="card" href="{{R}}guides/credit-score-and-loans.html"><div class="ico">🧱</div><h3>Fair or bad credit</h3><p class="muted">Options, and how to raise your odds.</p></a>
 </div>
</div></section>
<div class="container">{ad("header")}</div>
<section><div class="container">
 <h2>Typical personal loan APRs by credit score</h2><p class="muted">Illustrative ranges as of {ASOF}, compiled from public lender disclosures. Your rate may differ.</p>
 <div class="table-wrap"><table><thead><tr><th>Credit score</th><th>Typical APR</th><th>Where to look</th></tr></thead><tbody>{tr}</tbody></table></div>
 <div class="notice blue"><strong>Representative example:</strong> a $10,000 loan over 36 months at 17.59% APR (13.94% interest rate and a 5% origination fee deducted upfront) has 36 monthly payments of about $341, and you receive $9,500. Total repaid ≈ $12,293. For illustration only.</div>
</div></section>
<section class="bg-alt"><div class="container split">
 <div><h2>Eligibility checklist</h2><ul class="checks" style="flex-direction:column">
  <li>Age 18+ (19 in some US states/Canadian provinces, 21+ in India)</li><li>Verifiable income: pay stubs, tax returns or bank statements</li>
  <li>Debt-to-income ideally under 36% (many lenders allow up to 40–50%)</li><li>Credit score typically 580+ (best rates at 720+)</li>
  <li>Valid ID, bank account and residential address</li><li>US: SSN or ITIN · Canada: SIN optional for some lenders · India: PAN &amp; Aadhaar</li></ul></div>
 <div><h2>Documents to have ready</h2><ul class="checks" style="flex-direction:column">
  <li>Government-issued photo ID</li><li>Last 2 pay stubs or 2 years of tax returns (self-employed)</li><li>2–3 months of bank statements</li>
  <li>Proof of address (utility bill or lease)</li><li>Details of debts you plan to consolidate</li></ul>
  <a class="btn btn-primary" style="margin-top:14px" href="{{R}}apply.html?audience=personal">Check my options</a></div>
</div></section>
<section><div class="container">
 <h2>Pros &amp; cons of personal loans</h2>
 <div class="split"><div class="card"><h3 style="color:var(--green)">Pros</h3><ul><li>Fixed rate and fixed payment</li><li>No collateral for unsecured loans</li><li>Usually cheaper than credit cards for fair-to-excellent credit</li><li>Fast funding, often within days</li></ul></div>
 <div class="card"><h3 style="color:var(--red)">Cons</h3><ul><li>Origination fees up to ~10%</li><li>High APRs for poor credit</li><li>Hard inquiry when you formally apply</li><li>New monthly obligation that affects DTI</li></ul></div></div>
 {ad("inArticle")}
 <h2>FAQ</h2>{fq}
</div></section>
{cta_band()}"""
    write("personal-loans.html", "Personal Loans: Compare Rates, Fees & Lenders | BiLoans",
          "Compare personal loan rates by credit score, understand fees and eligibility, and get matched with lenders. Debt consolidation, home improvement and more.",
          body, schema=[fs], priority="0.9")


def business():
    fq, fs = faq([
        ("Can I get a business loan with no revenue?", "It's hard. Startups usually rely on SBA microloans, equipment financing, business credit cards, personal loans used for business, or grants. Some online lenders require only 6 months in business."),
        ("What is the easiest business loan to get?", "Merchant cash advances and invoice factoring have the loosest requirements but are the most expensive. Always convert the cost to APR with our <a href='{R}calculators.html#c-mca'>MCA calculator</a>."),
        ("How long does an SBA loan take?", "Typically 30–90 days from application to funding. SBA Express can be faster."),
        ("Do business loans affect personal credit?", "Most small-business lenders check your personal credit and ask for a personal guarantee, so defaults can affect you personally."),
        ("What documents do I need?", "Usually 3–6 months of bank statements, business and personal tax returns, financial statements, business registration, and ID. SBA loans require more."),
    ])
    prods = [("Term loan", "~7%–36%+", "$25K–$500K", "1–5 yrs", "Expansion, one-time investments"),
             ("SBA 7(a)", "Prime + 3%–6.5% cap", "Up to $5M", "Up to 10/25 yrs", "Established businesses, low rates"),
             ("SBA 504", "~5%–7% (fixed)", "Up to $5.5M+", "10–25 yrs", "Real estate, heavy equipment"),
             ("SBA microloan", "~8%–13%", "Up to $50K", "Up to 7 yrs", "Startups, very small businesses"),
             ("Business line of credit", "~8%–36%+", "$10K–$250K", "Revolving", "Cash-flow gaps, seasonal needs"),
             ("Equipment financing", "~10%–24%", "Up to 100% of cost", "Life of asset", "Machinery, vehicles, tech"),
             ("Invoice factoring / financing", "~24%–36%+", "80–90% of invoices", "30–90 days", "B2B firms with slow payers"),
             ("Revenue-based financing", "~10%–40%", "Based on revenue", "Variable", "E-commerce, SaaS"),
             ("Merchant cash advance", "Factor 1.1–1.5 (often 40%–100%+ APR)", "Based on card sales", "3–18 mo", "Last resort, fast cash")]
    tr = "".join(f"<tr><td><strong>{a}</strong></td><td>{b}</td><td>{c}</td><td>{d}</td><td>{e}</td></tr>" for a, b, c, d, e in prods)
    body = page_hero("Business loans", "Business loans: compare every funding type",
                     "From SBA loans to lines of credit and equipment financing, see what each costs, who qualifies, and how fast you can get funded.", [("Business loans", "")]) + f"""
<section style="padding-top:10px"><div class="container">
 <p class="disclosure">Advertiser disclosure: BiLoans may be compensated by partners. BiLoans is not a lender. Rates are illustrative as of {ASOF}.</p>
 <div class="grid g4" style="margin-top:26px">
  <a class="card green" href="{{R}}guides/sba-loans-explained.html"><div class="ico">🏛️</div><h3>SBA loans</h3><p class="muted">Government-backed, long terms, capped rates.</p></a>
  <a class="card green" href="{{R}}apply.html?audience=business&purpose=working-capital"><div class="ico">💵</div><h3>Working capital</h3><p class="muted">Lines of credit &amp; short-term loans.</p></a>
  <a class="card green" href="{{R}}apply.html?audience=business&purpose=equipment"><div class="ico">⚙️</div><h3>Equipment</h3><p class="muted">The equipment is the collateral.</p></a>
  <a class="card green" href="{{R}}guides/self-employed-loans.html"><div class="ico">🧑‍💻</div><h3>Self-employed &amp; startups</h3><p class="muted">Funding when you're just getting going.</p></a>
 </div>
</div></section>
<div class="container">{ad("header")}</div>
<section><div class="container">
 <h2>Business financing at a glance</h2>
 <div class="table-wrap"><table><thead><tr><th>Product</th><th>Typical APR</th><th>Amount</th><th>Term</th><th>Best for</th></tr></thead><tbody>{tr}</tbody></table></div>
 <p class="muted" style="font-size:.85rem;margin-top:10px">SBA 7(a) maximum variable spreads over prime depend on loan size (e.g. +6.5% up to $50K; +3% above $350K). Confirm current SBA rules with your lender.</p>
</div></section>
<section class="bg-alt"><div class="container">
 <h2>What lenders look at</h2>
 <div class="grid g4">
  <div class="card"><div class="ico">📅</div><h3>Time in business</h3><p class="muted">6 months minimum online; 2+ years for banks and SBA.</p></div>
  <div class="card"><div class="ico">💰</div><h3>Revenue</h3><p class="muted">Often $8K–$10K+/month for online loans.</p></div>
  <div class="card"><div class="ico">📈</div><h3>Credit</h3><p class="muted">Personal FICO 600+ online; 680+ for SBA; business credit helps.</p></div>
  <div class="card"><div class="ico">🧮</div><h3>Cash flow (DSCR)</h3><p class="muted">Banks like a debt-service coverage ratio of 1.25+.</p></div>
 </div>
 <p class="center" style="margin-top:24px"><a class="btn btn-green btn-lg" href="{{R}}apply.html?audience=business">Check business funding options</a></p>
</div></section>
<section><div class="container">
 <h2>Loans by industry</h2>
 <div class="pill-list">{"".join(f'<a href="{{R}}apply.html?audience=business">{i}</a>' for i in ["Restaurants","Construction","Trucking","Healthcare & dental","Retail","E-commerce","Salons & beauty","Auto repair","Agriculture","Real estate investors","Tech startups","Manufacturing","Franchises","Gig & freelance"])}</div>
 {ad("inArticle")}
 <h2>FAQ</h2>{fq}
</div></section>
{cta_band()}"""
    write("business-loans.html", "Business Loans: Compare SBA, Term, Lines of Credit & More | BiLoans",
          "Compare small business loan types, rates, requirements and speed: SBA 7(a), term loans, lines of credit, equipment, invoice and revenue-based financing.",
          body, schema=[fs], priority="0.9")


AUD = {"both": "personal business", "personal": "personal", "business": "business"}


def compare():
    L = [("Online personal lenders", "personal", "6–36", "$1K–$100K", "1–3 days", "580", "Fast funding; debt consolidation"),
         ("Banks", "both", "7–25", "$3K–$100K+", "3–10 days", "680", "Existing customers; relationship discounts"),
         ("Credit unions", "personal", "7–18", "$500–$50K", "2–7 days", "600", "Lowest rates; members; fair credit"),
         ("Peer-to-peer platforms", "personal", "8–36", "$2K–$50K", "3–7 days", "600", "Flexible criteria"),
         ("SBA lenders", "business", "10–15", "$50K–$5M", "30–90 days", "680", "Long terms; lowest business rates"),
         ("Online term lenders", "business", "10–36", "$25K–$500K", "1–3 days", "625", "Speed; 1+ year in business"),
         ("Fintech lines of credit", "business", "8–60", "$5K–$250K", "1–2 days", "600", "Working capital; repeat draws"),
         ("Equipment financiers", "business", "10–24", "Up to 100% of cost", "2–5 days", "600", "Machinery; vehicles"),
         ("Invoice factoring", "business", "24–36", "80–90% of invoices", "1–3 days", "500", "B2B with slow payers"),
         ("Merchant cash advance", "business", "40–150", "$5K–$500K", "24–48 hrs", "500", "Emergency cash only"),
         ("NBFCs (India)", "personal", "10–36", "₹50K–₹40L", "1–3 days", "650 (CIBIL)", "Salaried & self-employed in India"),
         ("Microlenders / CDFIs", "business", "8–18", "$500–$50K", "1–4 weeks", "None/low", "Startups; underserved founders")]
    tr = "".join(f'<tr data-aud="{AUD[a]}" data-credit="{int(c.split()[0]) if c.split()[0].isdigit() else 0}"><td><strong>{n}</strong><br><span class="badge {"green" if a=="business" else ("amber" if a=="both" else "")}">{a}</span></td><td data-v="{r.split("–")[0]}">~{r}%</td><td>{m}</td><td>{s}</td><td data-v="{c.split()[0] if c.split()[0].isdigit() else 0}">{c}</td><td>{b}</td><td><a class="btn btn-sm btn-primary" href="{{R}}apply.html?audience={"business" if a=="business" else "personal"}">Check</a></td></tr>' for n, a, r, m, s, c, b in L)
    feat = "".join(f'<tr class="featured" data-aud="personal business"><td><strong>Featured partner slot #{i}</strong><br><span class="badge amber">Sponsored</span></td><td>—</td><td>—</td><td>—</td><td>—</td><td>Your lender offer here</td><td><a class="btn btn-sm btn-amber" href="{{R}}advertise.html">Reserve</a></td></tr>' for i in (1, 2))
    body = page_hero("Compare", "Compare lender types side by side",
                     "Sort and filter 12 lender categories by rate, speed and minimum credit score. Then get matched with the type that fits.", [("Compare", "")]) + f"""
<section style="padding-top:10px"><div class="container">
 <p class="disclosure">Ranges are illustrative market ranges as of {ASOF}, drawn from public lender disclosures, and are not offers. "Sponsored" rows are paid placements. BiLoans is not a lender.</p>
 <div class="card" style="margin:22px 0;display:flex;gap:14px;flex-wrap:wrap;align-items:end">
  <div style="flex:1;min-width:180px"><label for="fAud">Loan for</label><select id="fAud" data-filter-table="cmpTable" data-key="aud"><option value="all">All</option><option value="personal">Personal</option><option value="business">Business</option></select></div>
  <div style="flex:2;min-width:220px"><label for="fText">Search</label><input id="fText" data-filter-table="cmpTable" data-key="text" placeholder="e.g. equipment, fast, credit union"></div>
 </div>
 <div class="table-wrap"><table id="cmpTable" data-sortable><thead><tr><th class="sortable">Lender type</th><th class="sortable">APR range</th><th>Amounts</th><th>Funding speed</th><th class="sortable">Min. credit</th><th>Best for</th><th></th></tr></thead><tbody>{feat}{tr}</tbody></table></div>
 {ad("inArticle")}
 <h2 style="margin-top:40px">How to compare loan offers like a pro</h2>
 <div class="grid g3">
  <div class="card"><h3>1. Compare APR, not rate</h3><p class="muted">APR includes fees. A 12% rate with an 8% fee can cost more than a 15% no-fee loan.</p></div>
  <div class="card"><h3>2. Check total cost</h3><p class="muted">Longer terms mean lower payments but more interest. Use our <a href="{{R}}calculators.html#c-cmp">offer comparison</a>.</p></div>
  <div class="card"><h3>3. Read the fine print</h3><p class="muted">Prepayment penalties, late fees, autopay discounts, and whether fees are deducted from proceeds.</p></div>
 </div>
</div></section>
{cta_band()}"""
    body = body.replace('data-key="text"', 'data-key="none"')
    write("compare.html", "Compare Lenders: Personal & Business Loan Types | BiLoans",
          "Sortable comparison of 12 lender types, including online lenders, banks, credit unions, SBA lenders, lines of credit and more, by APR, speed and credit score.",
          body, priority="0.8")
