"""Guides hub, long-form articles, glossary, videos."""
from blsite import *  # noqa

AUTHOR = "BiLoans Editorial Team"
REVIEWER = "Reviewed by the BiLoans Credit Review Desk"

ARTICLES = []


def article(slug, cat, title, desc, takeaways, sections, faqs, video, related):
    fq, fs = faq(faqs)
    toc = "".join(f'<a href="#s{i}">{esc(h)}</a>' for i, (h, _) in enumerate(sections))
    secs = ""
    for i, (h, c) in enumerate(sections):
        secs += f'<h2 id="s{i}">{h}</h2>{c}'
        if i == 1:
            secs += ad("inArticle")
        if i == 2:
            secs += f'<div class="card" style="margin:24px 0">{video_card(video[0], video[1], "", "Video")}</div>'
    rel = "".join(f'<a href="{{R}}{h}">{esc(t)}</a>' for t, h in related)
    art = {"@context": "https://schema.org", "@type": "Article", "headline": title, "description": desc,
           "datePublished": "2026-09-22", "dateModified": "2026-09-22",
           "author": {"@type": "Organization", "name": AUTHOR}, "publisher": {"@type": "Organization", "name": "BiLoans"}}
    crumbs = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": BASE},
        {"@type": "ListItem", "position": 2, "name": "Guides", "item": BASE + "guides.html"},
        {"@type": "ListItem", "position": 3, "name": title, "item": BASE + "guides/" + slug + ".html"}]}
    body = f"""
<section class="page-hero" style="padding-bottom:24px"><div class="container">
 <nav class="crumbs" aria-label="Breadcrumb"><a href="{{R}}index.html">Home</a> › <a href="{{R}}guides.html">Guides</a> › {esc(cat)}</nav>
 <span class="eyebrow">{esc(cat)}</span><h1 style="max-width:900px">{title}</h1>
 <div class="byline"><span>By {AUTHOR}</span><span>{REVIEWER}</span><span>Updated {ASOF}</span></div>
 <p class="disclosure" style="max-width:900px">Editorial content is independent. BiLoans may earn compensation from partners, which never influences our analysis. BiLoans is not a lender. This article is educational, not financial advice.</p>
</div></section>
<section style="padding-top:10px"><div class="container article">
 <article class="article-body">
  <div class="takeaways"><h3>Key takeaways</h3><ul>{"".join(f"<li>{t}</li>" for t in takeaways)}</ul></div>
  {secs}
  <h2>Frequently asked questions</h2>{fq}
  <div class="cta-band" style="margin-top:30px"><div><h3 style="margin:0 0 6px">Compare your options in 2 minutes</h3><p style="margin:0">Free, and no impact on your credit score.</p></div><a class="btn btn-white" href="{{R}}apply.html">Get Matched →</a></div>
 </article>
 <aside class="sidebar"><div class="sticky">
  <div class="card toc"><strong>On this page</strong>{toc}</div>
  <div class="card"><strong>Quick estimate</strong><p class="muted" style="font-size:.9rem">See your monthly payment and true APR.</p><a class="btn btn-primary btn-block" href="{{R}}calculators.html">Open calculators</a></div>
  {ad("sidebar")}
  <div class="card"><strong>Related guides</strong><div class="pill-list" style="margin-top:10px">{rel}</div></div>
 </div></aside>
</div></section>"""
    ARTICLES.append((slug, cat, title, desc))
    write(f"guides/{slug}.html", f"{title} | BiLoans", desc, body, schema=[fs, art, crumbs], priority="0.8")


def ul(*items):
    return "<ul>" + "".join(f"<li>{i}</li>" for i in items) + "</ul>"


def build_articles():
    article("personal-loan-guide", "Personal loans", "Personal loans: the complete 2026 guide",
            "How personal loans work, typical rates by credit score, fees to watch, eligibility and a step-by-step process for getting the best offer.",
            ["Personal loans are usually unsecured, fixed-rate installment loans of $1,000–$100,000 over 1–7 years.",
             "Typical APRs run from about 6% to 36%; your credit score is the single biggest driver.",
             "Always compare APR (rate + fees), not just the interest rate.",
             "Prequalify with several lenders using soft checks before you formally apply."],
            [("What is a personal loan?", "<p>A personal loan is a lump sum you repay in fixed monthly installments over a set term. Most are <strong>unsecured</strong>: no house or car is at risk. The lender prices the loan on your credit history, income and existing debts. Because the rate and payment are fixed, personal loans are easier to budget for than credit cards.</p>"),
             ("How much do personal loans cost?", "<p>The cost has three parts: the <strong>interest rate</strong>, any <strong>origination fee</strong> (0–10%, often deducted from the loan amount), and the <strong>term</strong>. The APR combines rate and fees into one yearly number. For example, a $10,000, 36-month loan at 13.94% interest with a 5% fee has an APR of about 17.6%. You'd receive $9,500 and pay about $341 a month.</p>" + ul("Excellent credit (720+): roughly 7%–15% APR", "Good (690–719): roughly 14%–22%", "Fair (630–689): roughly 18%–30%", "Poor (below 630): roughly 25%–36%, or a secured or co-signed loan")),
             ("Eligibility requirements", ul("Age 18+ and a resident of a state or country the lender serves", "Steady, verifiable income (employment, self-employment, benefits)", "Debt-to-income typically below 36%–45%", "Minimum credit score often 580–660", "A bank account and valid ID") + "<p>Check your DTI with our <a href='{R}calculators.html#c-dti'>DTI calculator</a> before you apply.</p>"),
             ("How to get the best rate: step by step", "<ol><li><strong>Check your credit</strong> and dispute any errors.</li><li><strong>Decide the amount</strong> and the payment you can afford. Try the <a href='{R}calculators.html#c-afford'>affordability calculator</a>.</li><li><strong>Prequalify</strong> with 3–5 lenders using soft checks.</li><li><strong>Compare APR and total cost</strong>, not the monthly payment alone.</li><li><strong>Read the terms</strong>: prepayment penalties, late fees, autopay discounts.</li><li><strong>Apply formally</strong> with the winner. Expect a hard inquiry.</li><li><strong>Set up autopay</strong> to protect your credit and often lower your rate.</li></ol>"),
             ("Alternatives to consider", ul("0% intro APR balance-transfer cards (if you can repay within the promo period)", "Credit-union loans, often cheaper for fair credit", "Home-equity loans/HELOCs, cheaper but secured by your home", "Secured personal loans backed by savings", "Negotiating directly with creditors or a nonprofit credit counselor"))],
            [("Does a personal loan hurt my credit?", "Applying causes a hard inquiry (a small, temporary dip). On-time payments build your credit, and consolidating card balances can lower utilization."),
             ("How fast can I get the money?", "Many online lenders fund within 1–3 business days after approval; some the next business day."),
             ("Can I pay off a personal loan early?", "Most lenders allow it without penalty, but check the agreement for prepayment fees.")],
            ("Personal loans explained", "personal loans explained for beginners"),
            [("Debt consolidation", "guides/debt-consolidation-loans.html"), ("APR vs interest rate", "guides/apr-vs-interest-rate.html"), ("Credit scores", "guides/credit-score-and-loans.html")])

    article("debt-consolidation-loans", "Personal loans", "Debt consolidation loans: when they save money (and when they don't)",
            "Learn how debt consolidation loans work, how to calculate your savings, and the mistakes that make consolidation backfire.",
            ["A consolidation loan replaces several high-interest debts with one fixed payment.",
             "It only saves money if the new APR (including fees) is meaningfully lower than your current average rate.",
             "Close the gap that created the debt, or you risk ending up with the loan plus new card balances.",
             "Use our consolidation calculator to test your exact numbers."],
            [("How consolidation works", "<p>You take out one personal loan and use it to pay off credit cards or other debts. Some lenders pay your creditors directly. You're left with one payment, one due date, and a fixed payoff date, often 3–5 years away.</p>"),
             ("Will it actually save you money?", "<p>Compare three numbers: your current <strong>weighted-average APR</strong>, the new loan's <strong>APR</strong>, and the <strong>total interest</strong> under each plan. Example: $12,000 of card debt at 24% APR, paid at $400 a month, takes over 4 years and costs thousands in interest. A 36-month loan at 13% with a 3% fee can save a significant amount. Run your own numbers in the <a href='{R}calculators.html#c-consol'>consolidation calculator</a>.</p>"),
             ("Pros and cons", "<div class='split'><div class='card'><h3 style='color:var(--green)'>Pros</h3>" + ul("Lower APR if your credit is fair or better", "Fixed payoff date", "Simpler budgeting", "Can lower credit utilization") + "</div><div class='card'><h3 style='color:var(--red)'>Cons</h3>" + ul("Origination fees", "A longer term can raise total interest", "Risk of re-running card balances", "Hard inquiry when you apply") + "</div></div>"),
             ("Alternatives", ul("Balance-transfer card with a 0% intro APR (typically 3%–5% transfer fee)", "Nonprofit debt management plan (DMP)", "Debt avalanche or snowball payoff methods", "Home-equity borrowing, cheaper but puts your home at risk") + "<div class='notice'>Be wary of <strong>debt settlement</strong> companies that charge upfront fees or tell you to stop paying creditors. See <a href='{R}guides/avoid-loan-scams.html'>how to avoid loan scams</a>.</div>")],
            [("What credit score do I need to consolidate debt?", "Many lenders accept 600+, but savings usually require good credit (690+) so the new APR beats your card rates."),
             ("Does consolidation hurt my credit?", "Briefly, from the hard inquiry and the new account. Over time, lower utilization and on-time payments usually help.")],
            ("Is debt consolidation a good idea?", "debt consolidation loan explained"),
            [("Personal loan guide", "guides/personal-loan-guide.html"), ("Credit scores", "guides/credit-score-and-loans.html"), ("Loan scams", "guides/avoid-loan-scams.html")])

    article("business-loan-types", "Business loans", "11 types of business loans compared",
            "Term loans, SBA, lines of credit, equipment, invoice, MCA and more: how each business loan type works, what it costs, and who it suits.",
            ["Match the loan to the use: long-term assets need long-term financing, cash-flow gaps need revolving credit.",
             "SBA loans are cheapest but slowest; MCAs are fastest but most expensive.",
             "Convert every offer to APR so you can compare factor rates and fees fairly.",
             "Most small-business loans need a personal guarantee."],
            [("Quick comparison", "<div class='table-wrap'><table><thead><tr><th>Type</th><th>Best for</th><th>Speed</th><th>Cost</th></tr></thead><tbody><tr><td>Term loan</td><td>Expansion</td><td>Days–weeks</td><td>Low–high</td></tr><tr><td>SBA 7(a)</td><td>Most purposes</td><td>1–3 months</td><td>Low</td></tr><tr><td>SBA 504</td><td>Real estate, equipment</td><td>1–3 months</td><td>Lowest</td></tr><tr><td>SBA microloan</td><td>Startups</td><td>Weeks</td><td>Low–medium</td></tr><tr><td>Line of credit</td><td>Cash flow</td><td>1–7 days</td><td>Medium</td></tr><tr><td>Equipment financing</td><td>Machinery, vehicles</td><td>Days</td><td>Medium</td></tr><tr><td>Invoice factoring</td><td>Slow-paying B2B clients</td><td>1–3 days</td><td>High</td></tr><tr><td>Invoice financing</td><td>B2B cash flow</td><td>Days</td><td>Medium–high</td></tr><tr><td>Revenue-based</td><td>E-commerce, SaaS</td><td>Days</td><td>Medium–high</td></tr><tr><td>Merchant cash advance</td><td>Emergencies</td><td>24–48 hrs</td><td>Very high</td></tr><tr><td>Business credit card</td><td>Small, recurring costs</td><td>Days</td><td>Medium–high</td></tr></tbody></table></div>"),
             ("Term loans and SBA loans", "<p><strong>Term loans</strong> give a lump sum repaid over 1–10 years. Banks offer the lowest rates to established, profitable businesses. Online lenders approve faster with looser criteria at higher APRs. <strong>SBA loans</strong> are partially guaranteed by the U.S. Small Business Administration, which caps rates and allows terms up to 25 years for real estate. Read <a href='{R}guides/sba-loans-explained.html'>SBA loans explained</a>.</p>"),
             ("Lines of credit and equipment financing", "<p>A <strong>business line of credit</strong> works like a credit card with a higher limit and lower rate: draw what you need and pay interest only on what you use. <strong>Equipment financing</strong> uses the equipment itself as collateral, so it's easier to qualify for, and terms match the asset's useful life.</p>"),
             ("Invoice, revenue-based financing and MCAs", "<p><strong>Invoice factoring</strong> sells your unpaid invoices at a discount. <strong>Invoice financing</strong> borrows against them. <strong>Revenue-based financing</strong> is repaid as a percentage of monthly revenue. A <strong>merchant cash advance</strong> buys a share of future card sales at a factor rate such as 1.3. That looks like 30%, but over 6–8 months it often equals an APR above 60%. Check any offer with our <a href='{R}calculators.html#c-mca'>MCA → APR calculator</a>.</p>"),
             ("How to choose", ul("Define the use and how long the benefit lasts", "Check your eligibility: time in business, revenue, credit", "Get 3+ quotes and convert each to APR", "Model the payment against your cash flow (DSCR 1.25+ is healthy)", "Read the covenants, prepayment terms and personal-guarantee language"))],
            [("What's the easiest business loan to get?", "MCAs, invoice factoring and equipment financing have the loosest criteria. MCAs are the costliest, so treat them as a last resort."),
             ("Can a startup get a business loan?", "Yes, through SBA microloans, CDFIs, equipment financing, business cards, personal loans or grants. Most term lenders want 6–24 months of history.")],
            ("Types of business loans explained", "types of small business loans explained"),
            [("SBA loans", "guides/sba-loans-explained.html"), ("Self-employed loans", "guides/self-employed-loans.html"), ("Business hub", "business-loans.html")])

    article("sba-loans-explained", "Business loans", "SBA loans explained: 7(a), 504 and microloans",
            "How SBA loans work, current rate caps, eligibility, documents and a realistic timeline for approval.",
            ["SBA loans are made by approved lenders and partially guaranteed by the U.S. Small Business Administration.",
             "7(a) loans go up to $5 million; 504 loans finance real estate and major equipment; microloans go up to $50,000.",
             "SBA caps the spread over prime: for 7(a) variable loans, from +3% (large loans) to +6.5% (loans up to $50K).",
             "Expect 30–90 days and a thorough document package."],
            [("The three main programs", ul("<strong>7(a)</strong>: the flagship program. Working capital, equipment, refinancing, acquisitions, real estate. Up to $5M.", "<strong>504</strong>: long-term fixed-rate financing for real estate and heavy equipment through a bank plus a Certified Development Company.", "<strong>Microloan</strong>: up to $50,000 through nonprofit intermediaries. Great for startups.", "<strong>7(a) Express</strong>: faster decisions, up to $500K, with a lower guarantee.")),
             ("Rates and fees", "<p>Rates are negotiated with the lender but capped by SBA. For variable 7(a) loans, the maximum spread over prime depends on size: roughly +6.5% up to $50K, +6% from $50K–$250K, +4.5% from $250K–$350K, and +3% above $350K. Fixed-rate caps are somewhat higher. SBA also charges an upfront <strong>guaranty fee</strong> on the guaranteed portion, which varies by size and fiscal year. Use our <a href='{R}calculators.html#c-sba'>SBA calculator</a> to estimate payments.</p>"),
             ("Eligibility", ul("For-profit business operating in the U.S.", "Meets SBA size standards", "Owner has invested equity", "Can't obtain credit elsewhere on reasonable terms", "Good personal credit (often 680+), no recent defaults on government debt", "Personal guarantee from owners with 20%+ ownership")),
             ("Documents and timeline", "<p>Prepare 3 years of business and personal tax returns, year-to-date P&amp;L and balance sheet, a debt schedule, a business plan or projections (for startups and acquisitions), and entity documents. Most 7(a) loans close in <strong>30–90 days</strong>. Lenders with SBA preferred-lender status can move faster.</p>")],
            [("Can startups get SBA loans?", "Yes. Microloans and some 7(a) lenders fund startups, usually with strong owner credit, industry experience and an equity injection of around 10%+."),
             ("Is collateral required?", "For 7(a) loans above $50K, lenders must take available collateral, but SBA won't decline a loan solely for lack of collateral.")],
            ("SBA 7(a) loans: how to qualify", "SBA 7a loan how to qualify"),
            [("Business loan types", "guides/business-loan-types.html"), ("Business hub", "business-loans.html"), ("SBA calculator", "calculators.html#c-sba")])

    article("self-employed-loans", "Both", "Loans for the self-employed: personal or business loan?",
            "Freelancers, gig workers and sole proprietors: how to qualify with 1099 or variable income, and when to choose a personal loan over a business loan.",
            ["Self-employed borrowers can use personal loans, business loans, or both. The right choice depends on the purpose and your paperwork.",
             "Lenders usually want 2 years of tax returns, or 12–24 months of bank statements.",
             "Taking large write-offs lowers taxable income, and lenders see the lower number.",
             "Keep business and personal finances separate to qualify more easily for both."],
            [("Personal vs business loan: quick decision", "<div class='table-wrap'><table><thead><tr><th>If you…</th><th>Consider</th></tr></thead><tbody><tr><td>Need under $50K for mixed purposes, with good personal credit</td><td>Personal loan</td></tr><tr><td>Have 1+ year of business revenue and need working capital</td><td>Business line of credit / term loan</td></tr><tr><td>Are buying equipment or vehicles for the business</td><td>Equipment financing</td></tr><tr><td>Want to build business credit separate from yours</td><td>Business loan / card</td></tr><tr><td>Just started with little revenue</td><td>SBA microloan, CDFI, or personal loan</td></tr></tbody></table></div>"),
             ("How lenders verify self-employed income", ul("Two years of personal tax returns (Schedule C in the U.S.; T1/T2125 in Canada; ITR in India)", "1099s, invoices or platform payout statements", "12–24 months of bank statements (bank-statement programs)", "Year-to-date profit-and-loss statement", "Business licence or registration")),
             ("Boost your approval odds", ul("Open a separate business bank account", "Get an EIN (U.S.) or business number and build business credit", "Keep DTI under 36%", "Consider a co-signer or a secured loan", "Show consistent or rising income over 24 months")),
             ("Why BiLoans' 'Both' path exists", "<p>Most comparison sites send you down either a personal or a business funnel. If you're an owner-operator, your approval depends on both. Our <a href='{R}apply.html?audience=both'>'Both' application</a> collects personal and business details together so partners can suggest the best-fit product.</p>")],
            [("Can I get a personal loan with 1099 income?", "Yes. Many online lenders accept self-employment income verified by tax returns or bank statements."),
             ("Will a business loan show on my personal credit?", "Many small-business lenders report only to business bureaus, but a personal guarantee means a default can hit your personal credit.")],
            ("Loans for self-employed people", "loans for self employed explained"),
            [("Personal loan guide", "guides/personal-loan-guide.html"), ("Business loan types", "guides/business-loan-types.html"), ("Get matched (both)", "apply.html?audience=both")])

    article("credit-score-and-loans", "Personal loans", "Credit scores and loans: what lenders see and how to improve",
            "How credit scores affect loan approval and rates, what factors matter most, and a 90-day plan to raise your score before applying.",
            ["Moving from fair (630–689) to good (690+) credit can cut a personal loan APR by several points.",
             "Payment history and utilization make up most of a FICO score.",
             "Soft checks (prequalification) don't affect your score; hard inquiries cause a small, temporary dip.",
             "Multiple loan inquiries within a short window are often treated as one for rate shopping."],
            [("Score bands lenders use", ul("Excellent: 720–850", "Good: 690–719", "Fair: 630–689", "Poor: 300–629") + "<p>India's CIBIL scale also runs 300–900, with 750+ considered strong. Canada and the UK use their own bureau scales.</p>"),
             ("What drives your score", ul("Payment history (~35%)", "Credit utilization (~30%): keep it under 30%, ideally under 10%", "Length of history (~15%)", "Credit mix (~10%)", "New credit / inquiries (~10%)")),
             ("A 90-day improvement plan", "<ol><li>Pull your reports and dispute errors.</li><li>Pay every bill on time. Set up autopay.</li><li>Pay card balances down before the statement date to cut reported utilization.</li><li>Ask for credit-limit increases (no new hard pull where possible).</li><li>Don't open or close accounts right before applying.</li><li>Consider becoming an authorized user on a well-managed card.</li></ol>"),
             ("Borrowing with bad credit", ul("Credit unions and community lenders", "Secured personal loans or share-secured loans", "A creditworthy co-signer", "Smaller amounts and shorter terms") + "<div class='notice'>Avoid payday loans and 'guaranteed approval' offers. Their APRs can exceed 300%.</div>")],
            [("What score do I need for a personal loan?", "Often 580–660 at minimum. Best rates at 720+."),
             ("Does checking my own score hurt it?", "No. Checking your own credit is a soft inquiry.")],
            ("How to raise your credit score fast", "how to raise credit score fast"),
            [("Personal loan guide", "guides/personal-loan-guide.html"), ("Debt consolidation", "guides/debt-consolidation-loans.html"), ("DTI calculator", "calculators.html#c-dti")])

    article("avoid-loan-scams", "Safety", "How to spot and avoid loan scams",
            "The warning signs of loan scams and predatory lenders, how to verify a lender, and what to do if you've been targeted.",
            ["Legitimate lenders never ask you to pay a fee before the loan is approved and funded.",
             "'Guaranteed approval regardless of credit' is a red flag.",
             "Verify the lender's registration: state licences (US), FCA register (UK), provincial regulators (Canada), RBI list (India).",
             "BiLoans will never ask for payment, gift cards, crypto, OTPs or passwords."],
            [("Red flags", ul("Upfront 'processing', 'insurance' or 'guarantee' fees before funding", "Guaranteed approval without a credit check", "Pressure to act immediately", "Payment requested by gift card, wire, crypto or P2P app", "No physical address, or a website without HTTPS", "Unsolicited calls, texts or WhatsApp messages offering loans", "Loan apps asking for access to your contacts and photos")),
             ("How to verify a lender", ul("US: check your state's financial regulator and the NMLS Consumer Access database", "UK: search the FCA Financial Services Register", "Canada: check your provincial consumer-protection or financial regulator", "India: confirm the NBFC on the RBI website; check the lender's KFS", "Search the company name plus 'scam' or 'complaints'")),
             ("Predatory (but legal) products", "<p>Some products are legal but extremely costly: payday loans, car-title loans, and some merchant cash advances. Compare their APR with alternatives using our <a href='{R}calculators.html'>calculators</a> before you sign.</p>"),
             ("If you've been targeted", ul("Stop contact and don't send more money", "Contact your bank immediately to try to reverse payments", "US: report to the FTC (reportfraud.ftc.gov) and the CFPB", "Canada: Canadian Anti-Fraud Centre · UK: Action Fraud · India: cybercrime.gov.in / 1930", "Freeze your credit if personal data was shared"))],
            [("Does BiLoans charge fees?", "No. BiLoans is free for borrowers and will never ask you for payment to get a loan."),
             ("Is it safe to share my SSN or PAN?", "Only on a lender's secure application after you've verified it. BiLoans' matching form does not ask for it.")],
            ("How to spot loan scams", "how to spot loan scams"),
            [("Credit scores", "guides/credit-score-and-loans.html"), ("Personal loan guide", "guides/personal-loan-guide.html"), ("Contact BiLoans", "contact.html")])

    article("apr-vs-interest-rate", "Personal loans", "APR vs interest rate: which number matters?",
            "The difference between APR and interest rate, how fees change the true cost of a loan, with worked examples.",
            ["The interest rate is the cost of borrowing the principal; APR adds required fees.",
             "Always compare APRs when you shop for loans. It's the apples-to-apples number.",
             "A lower rate with a big origination fee can cost more than a higher no-fee rate.",
             "UK ads show a 'representative APR'; India's KFS shows the all-in APR."],
            [("The definitions", "<p><strong>Interest rate</strong>: the percentage charged on the principal each year. <strong>APR (annual percentage rate)</strong>: the interest rate plus mandatory fees such as origination or processing fees, expressed as a yearly rate.</p>"),
             ("Worked example", "<p>Offer A: $15,000, 60 months, 11.5%, 6% fee. Offer B: $15,000, 36 months, 14%, no fee. A has the lower rate and the lower monthly payment. B finishes two years sooner and can cost less in total. Run both in our <a href='{R}calculators.html#c-cmp'>offer comparison tool</a>.</p>"),
             ("Why fees matter so much", "<p>Origination fees are often deducted from your proceeds. You pay interest on money you never receive. On short terms, the fee's effect on the APR is even larger.</p>"),
             ("What else to compare", ul("Total repayment amount", "Monthly payment vs your budget", "Prepayment penalties", "Autopay discounts", "Funding speed and customer service"))],
            [("Is a lower APR always better?", "For the same term, yes. Across different terms, also compare total cost and whether the payment fits your budget."),
             ("What's a good APR for a personal loan?", "Below ~12% is excellent in the current market; 12%–20% is typical for good credit.")],
            ("APR vs interest rate explained", "APR vs interest rate explained"),
            [("APR calculator", "calculators.html#c-apr"), ("Personal loan guide", "guides/personal-loan-guide.html"), ("Compare offers", "calculators.html#c-cmp")])


def guides_hub():
    cats = {"Personal loans": "", "Business loans": "green", "Both": "amber", "Safety": "amber"}
    cards = "".join(f'<a class="card reveal" href="{{R}}guides/{s}.html"><span class="badge {cats.get(c, "")}">{esc(c)}</span><h3 style="margin-top:10px">{esc(t)}</h3><p class="muted">{esc(d)}</p></a>' for s, c, t, d in ARTICLES)
    body = page_hero("Learn", "Loan guides", "Independent, plain-English guides to personal and business borrowing. Written for real decisions, not jargon.", [("Guides", "")]) + f"""
<section style="padding-top:10px"><div class="container">
 <div class="grid g3">{cards}</div>
 {ad("inArticle")}
 <div class="grid g3" style="margin-top:20px">
  <a class="card" href="{{R}}glossary.html"><div class="ico">📖</div><h3>Loan glossary</h3><p class="muted">60+ terms, from APR to UCC lien.</p></a>
  <a class="card green" href="{{R}}videos.html"><div class="ico">🎬</div><h3>Video hub</h3><p class="muted">Short explainers you can watch in minutes.</p></a>
  <a class="card amber" href="{{R}}global.html"><div class="ico">🌍</div><h3>Loans by country</h3><p class="muted">US, Canada, UK and India.</p></a>
 </div>
</div></section>{cta_band()}"""
    write("guides.html", "Loan Guides: Personal & Business Borrowing Explained | BiLoans",
          "Plain-English guides to personal loans, business loans, SBA loans, debt consolidation, credit scores, APR and avoiding loan scams.", body, priority="0.8")


GLOSS = [
    ("Amortization", "Paying off a loan through scheduled payments that cover interest first and then principal."),
    ("Annual Percentage Rate (APR)", "The yearly cost of a loan including interest and mandatory fees."),
    ("Autopay discount", "A rate reduction (often 0.25%–0.50%) for automatic payments."),
    ("Balance transfer", "Moving card debt to a new card, often at a 0% intro APR, usually with a fee."),
    ("Balloon payment", "A large lump-sum payment due at the end of a loan."),
    ("Blanket lien", "A lender's claim on all business assets as collateral."),
    ("Bridge loan", "Short-term financing that covers a gap until longer-term funding arrives."),
    ("Business credit score", "A score from bureaus such as D&B, Experian Business or Equifax that measures business creditworthiness."),
    ("CIBIL score", "India's most widely used credit score, ranging 300–900."),
    ("Co-signer", "A person who agrees to repay if the borrower doesn't, strengthening the application."),
    ("Collateral", "An asset pledged to secure a loan."),
    ("Credit utilization", "Revolving balances divided by credit limits; lower is better."),
    ("Debt consolidation", "Combining several debts into one new loan."),
    ("Debt-service coverage ratio (DSCR)", "Business cash flow divided by debt payments; lenders like 1.25+."),
    ("Debt-to-income ratio (DTI)", "Monthly debt payments divided by gross monthly income."),
    ("Default", "Failure to repay a loan as agreed."),
    ("EMI", "Equated Monthly Instalment: a fixed monthly loan payment (common term in India)."),
    ("Equipment financing", "A loan or lease secured by the equipment being purchased."),
    ("Factor rate", "A decimal multiplier (e.g. 1.3) used by MCAs to set total payback; not an APR."),
    ("FICO Score", "A widely used US credit score ranging 300–850."),
    ("Fixed rate", "An interest rate that doesn't change over the loan term."),
    ("Grace period", "Time after a due date before a late fee is charged."),
    ("Guaranty fee", "The fee SBA charges on the guaranteed portion of a loan."),
    ("Hard inquiry", "A credit check for a new credit application; can lower your score slightly."),
    ("HELOC", "Home equity line of credit: revolving credit secured by your home."),
    ("Installment loan", "A loan repaid in fixed, scheduled payments."),
    ("Interest rate", "The percentage charged for borrowing principal, excluding fees."),
    ("Invoice factoring", "Selling unpaid invoices to a factor for immediate cash."),
    ("Key Facts Statement (KFS)", "India's standardized loan disclosure showing APR and all charges."),
    ("Late fee", "A penalty charged when a payment is late."),
    ("Line of credit", "Revolving credit you can draw on, repay and reuse."),
    ("Loan-to-value (LTV)", "Loan amount divided by the collateral's value."),
    ("Merchant cash advance (MCA)", "An advance repaid from a share of future card sales; typically very expensive."),
    ("Microloan", "A small loan, often up to $50,000, for startups and very small businesses."),
    ("NBFC", "Non-Banking Financial Company: an RBI-registered lender in India."),
    ("NMLS", "Nationwide Multistate Licensing System, the US registry for many lenders and brokers."),
    ("Origination fee", "An upfront fee for processing a loan, usually 0%–10%."),
    ("Personal guarantee", "An owner's promise to repay a business loan personally."),
    ("Prepayment penalty", "A fee for paying off a loan early."),
    ("Prequalification", "An estimate of your rate and eligibility, usually with a soft credit check."),
    ("Prime rate", "The benchmark rate banks charge top customers; many business loans float above it."),
    ("Principal", "The amount borrowed, excluding interest."),
    ("Promissory note", "The signed document containing your promise to repay."),
    ("Refinancing", "Replacing an existing loan with a new one, often at a lower rate."),
    ("Representative APR", "UK: the APR that at least 51% of accepted applicants receive."),
    ("Revenue-based financing", "Funding repaid as a percentage of monthly revenue."),
    ("Revolving credit", "Credit you can repeatedly borrow and repay, such as cards and lines of credit."),
    ("SBA 504", "SBA program for long-term, fixed-rate real estate and equipment financing."),
    ("SBA 7(a)", "The SBA's primary loan program, up to $5 million."),
    ("Secured loan", "A loan backed by collateral."),
    ("Soft inquiry", "A credit check that doesn't affect your score (e.g. prequalification)."),
    ("Term", "The length of time to repay a loan."),
    ("Term loan", "A lump sum repaid over a fixed period."),
    ("TILA", "Truth in Lending Act: US law requiring clear disclosure of APR and loan costs."),
    ("UCC lien", "A public filing that gives a lender a claim on business assets."),
    ("Underwriting", "The lender's process of evaluating risk and deciding on approval."),
    ("Unsecured loan", "A loan with no collateral."),
    ("Variable rate", "An interest rate that can change with a benchmark."),
    ("Working capital", "Current assets minus current liabilities; funding for day-to-day operations."),
]


def glossary():
    letters = sorted({t[0].upper() for t, _ in GLOSS})
    az = "".join(f'<a href="#g-{l}">{l}</a>' for l in letters)
    out, cur = "", ""
    for t, d in GLOSS:
        l = t[0].upper()
        if l != cur:
            out += f'</dl><h2 id="g-{l}" style="margin-top:30px">{l}</h2><dl class="gloss">'
            cur = l
        out += f"<dt>{esc(t)}</dt><dd>{esc(d)}</dd>"
    out = out[5:] + "</dl>"
    schema = {"@context": "https://schema.org", "@type": "DefinedTermSet", "name": "BiLoans Loan Glossary",
              "hasDefinedTerm": [{"@type": "DefinedTerm", "name": t, "description": d} for t, d in GLOSS]}
    body = page_hero("Learn", "Loan glossary", f"{len(GLOSS)} personal and business lending terms, explained in one sentence each.", [("Glossary", "")]) + f"""
<section style="padding-top:10px"><div class="container article"><div><div class="az">{az}</div>{out}</div>
<aside class="sidebar"><div class="sticky">{ad("sidebar")}<div class="card"><strong>Put it into practice</strong><p class="muted">Run your numbers with our free calculators.</p><a class="btn btn-primary btn-block" href="{{R}}calculators.html">Calculators</a></div></div></aside></div></section>"""
    write("glossary.html", "Loan Glossary: 60 Lending Terms Explained | BiLoans",
          "APR, DSCR, factor rate, origination fee, KFS, SBA 7(a) and more: personal and business loan terms explained simply.", body, schema=[schema], priority="0.6")


def videos():
    V = [("Personal loans explained for beginners", "personal loans explained", ""), ("How debt consolidation works", "debt consolidation loan explained", ""),
         ("APR vs interest rate", "APR vs interest rate explained", "a"), ("How to raise your credit score fast", "how to raise credit score fast", ""),
         ("SBA 7(a) loans: how to qualify", "SBA 7a loan how to qualify", "g"), ("Business line of credit explained", "business line of credit explained", "g"),
         ("Merchant cash advance: the true cost", "merchant cash advance true cost APR", "a"), ("Equipment financing basics", "equipment financing explained", "g"),
         ("Loans for self-employed people", "loans for self employed explained", "a"), ("How to spot loan scams", "how to spot loan scams", ""),
         ("Personal loan EMI explained (India)", "personal loan EMI explained", ""), ("Small business grants vs loans", "small business grants vs loans", "g")]
    cards = "".join(video_card(t, q, v) for t, q, v in V)
    body = page_hero("Watch", "Loan video hub", "Short explainers on personal and business borrowing. Subscribe to the BiLoans channel for weekly rate updates.", [("Videos", "")]) + f"""
<section style="padding-top:10px"><div class="container">
 <div data-featured-video style="max-width:900px;margin:0 auto 30px"></div>
 <div class="grid g3">{cards}</div>
 {ad("inArticle")}
 <div class="card" style="margin-top:30px;display:flex;gap:18px;flex-wrap:wrap;align-items:center;justify-content:space-between">
  <div><h3 style="margin:0">Are you a finance creator?</h3><p class="muted" style="margin:4px 0 0">Feature your video on BiLoans, or join our creator program and paid video contests.</p></div>
  <div><a class="btn btn-primary" href="{{R}}contests.html">Video contests</a> <a class="btn btn-ghost" href="{{R}}advertise.html">Creator partnerships</a></div>
 </div>
</div></section>"""
    write("videos.html", "Loan Videos: Personal & Business Loan Explainers | BiLoans",
          "Watch short video explainers on personal loans, debt consolidation, APR, credit scores, SBA loans, lines of credit and loan scams.", body, priority="0.6")
