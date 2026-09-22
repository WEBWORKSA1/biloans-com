"""BiLoans.com static site framework: shared layout, helpers and writer."""
import json, os, html as H

OUT = os.path.join(os.path.dirname(__file__), "..")
BASE = "https://webworksa1.github.io/biloans-com/"
YEAR = "2026"
ASOF = "September 2026"
PAGES = []  # for sitemap

NAV = [
    ("Personal Loans", "personal-loans.html", [
        ("Personal loans hub", "personal-loans.html"),
        ("Debt consolidation", "guides/debt-consolidation-loans.html"),
        ("Personal loan basics", "guides/personal-loan-guide.html"),
        ("Credit scores & loans", "guides/credit-score-and-loans.html"),
        ("Loan payment calculator", "calculators.html#c-pay"),
    ]),
    ("Business Loans", "business-loans.html", [
        ("Business loans hub", "business-loans.html"),
        ("Types of business loans", "guides/business-loan-types.html"),
        ("SBA loans explained", "guides/sba-loans-explained.html"),
        ("Loans for self-employed", "guides/self-employed-loans.html"),
        ("SBA 7(a) calculator", "calculators.html#c-sba"),
    ]),
    ("Compare", "compare.html", [
        ("Compare lender types", "compare.html"),
        ("Today's rates", "rates.html"),
        ("Loans by country", "global.html"),
    ]),
    ("Calculators", "calculators.html", [
        ("Payment / EMI calculator", "calculators.html#c-pay"),
        ("APR calculator", "calculators.html#c-apr"),
        ("How much can I borrow?", "calculators.html#c-afford"),
        ("Debt-to-income", "calculators.html#c-dti"),
        ("Debt consolidation savings", "calculators.html#c-consol"),
        ("Business loan", "calculators.html#c-biz"),
        ("MCA factor rate → APR", "calculators.html#c-mca"),
        ("Compare two offers", "calculators.html#c-cmp"),
    ]),
    ("Learn", "guides.html", [
        ("All guides", "guides.html"),
        ("Videos", "videos.html"),
        ("Glossary", "glossary.html"),
        ("Avoid loan scams", "guides/avoid-loan-scams.html"),
    ]),
    ("Community", "support.html", [
        ("Support BiLoans (donate)", "support.html"),
        ("Contests & prizes", "contests.html"),
        ("Careers & talent", "careers.html"),
        ("Advertise & partner", "advertise.html"),
    ]),
]


def esc(s):
    return H.escape(s, quote=True)


def head(title, desc, path, root, schema=None, noindex=False):
    url = BASE + path.replace("index.html", "")
    sch = [{
        "@context": "https://schema.org", "@type": "Organization", "name": "BiLoans",
        "url": BASE, "logo": BASE + "assets/img/logo.svg",
        "description": "Independent comparison and matching platform for business and individual loans."
    }, {
        "@context": "https://schema.org", "@type": "WebSite", "name": "BiLoans", "url": BASE
    }]
    if schema:
        sch += schema if isinstance(schema, list) else [schema]
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{url}">
{'<meta name="robots" content="noindex">' if noindex else '<meta name="robots" content="index, follow, max-image-preview:large">'}
<meta name="theme-color" content="#0B1F3A">
<meta property="og:type" content="website">
<meta property="og:site_name" content="BiLoans">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{url}">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="{root}assets/img/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{root}assets/css/style.css">
<script>try{{var t=localStorage.getItem('bl-theme');if(t)document.documentElement.setAttribute('data-theme',t)}}catch(e){{}}</script>
<script type="application/ld+json">{json.dumps(sch)}</script>
</head>"""


def header(root):
    items = []
    for label, href, sub in NAV:
        dd = "".join(f'<a href="{root}{h}">{esc(l)}</a>' for l, h in sub)
        items.append(f'<li><a href="{root}{href}">{esc(label)}</a><div class="dropdown">{dd}</div></li>')
    return f"""<body data-root="{root}">
<a class="skip" href="#main">Skip to content</a>
<div class="topstrip" role="note"><a href="https://web.works/contact" target="_blank" rel="noopener">Contact, if you are interested in this website / domain name / Sponsorship / Advertisement / Partnership →</a></div>
<header class="site-header">
 <div class="container nav">
  <a class="logo" href="{root}index.html" aria-label="BiLoans home"><span class="mark">Bi</span><span>Bi<b>Loans</b></span></a>
  <ul class="menu" id="menu">{''.join(items)}</ul>
  <div class="nav-actions">
   <button class="icon-btn" data-theme-toggle aria-label="Toggle dark mode">☾</button>
   <a class="btn btn-primary btn-sm btn-cta-top" href="{root}apply.html">Get Matched</a>
   <button class="icon-btn burger" aria-label="Open menu" aria-controls="menu" aria-expanded="false">☰</button>
  </div>
 </div>
</header>
<main id="main">"""


def footer(root, extra_js=""):
    r = root
    return f"""</main>
<footer class="site-footer">
 <div class="container">
  <div class="foot-grid">
   <div>
    <a class="logo" href="{r}index.html" style="color:#fff"><span class="mark">Bi</span><span>Bi<b style="color:#6FA0FF">Loans</b></span></a>
    <p style="margin-top:14px">One place for <strong style="color:#fff">Business &amp; Individual</strong> loans. Compare options, run the numbers, and get matched with lending partners &mdash; free.</p>
    <div class="pill-list" style="margin-top:14px">
     <a data-social="youtube" href="#" aria-label="YouTube">YouTube</a><a data-social="x" href="#" aria-label="X">X</a><a data-social="linkedin" href="#">LinkedIn</a><a data-social="instagram" href="#">Instagram</a>
    </div>
   </div>
   <div><h4>Borrow</h4><ul>
    <li><a href="{r}apply.html">Get matched</a></li><li><a href="{r}personal-loans.html">Personal loans</a></li>
    <li><a href="{r}business-loans.html">Business loans</a></li><li><a href="{r}compare.html">Compare lenders</a></li>
    <li><a href="{r}rates.html">Today's rates</a></li><li><a href="{r}global.html">Loans by country</a></li></ul></div>
   <div><h4>Tools &amp; Learn</h4><ul>
    <li><a href="{r}calculators.html">Calculators</a></li><li><a href="{r}guides.html">Guides</a></li>
    <li><a href="{r}videos.html">Videos</a></li><li><a href="{r}glossary.html">Glossary</a></li>
    <li><a href="{r}guides/avoid-loan-scams.html">Avoid loan scams</a></li></ul></div>
   <div><h4>Community</h4><ul>
    <li><a href="{r}support.html">Support us / Donate</a></li><li><a href="{r}contests.html">Contests &amp; prizes</a></li>
    <li><a href="{r}careers.html">Careers</a></li><li><a href="{r}advertise.html">Advertise &amp; partner</a></li>
    <li><a href="https://web.works/contact" target="_blank" rel="noopener">Buy this domain / site</a></li></ul></div>
   <div><h4>Company</h4><ul>
    <li><a href="{r}about.html">About</a></li><li><a href="{r}how-we-make-money.html">How we make money</a></li>
    <li><a href="{r}contact.html">Contact</a></li><li><a href="{r}privacy.html">Privacy</a></li>
    <li><a href="{r}terms.html">Terms</a></li><li><a href="{r}disclosures.html">Disclosures &amp; trademarks</a></li></ul></div>
  </div>
  <div class="legal">
   <p><strong>BiLoans is not a lender</strong> and does not make credit decisions, broker loans in jurisdictions where a licence is required, or guarantee approval, rates or terms. We are an independent, advertising-supported publisher that helps you compare options and may connect you with third-party lending partners. Rates shown are illustrative market ranges as of {ASOF} and may change. Your actual rate depends on credit, income, loan amount, term and lender criteria. Information is educational and is not financial, legal or tax advice.</p>
   <p><strong>Advertiser disclosure:</strong> We may receive compensation when you click links, submit a request, or are approved for products. Compensation may affect where offers appear but does not influence our editorial ratings. Not all lenders or offers are included. <a href="{r}how-we-make-money.html">Learn more</a>.</p>
   <p><strong>Trademark &amp; copyright:</strong> &ldquo;BiLoans&rdquo; and the Bi|Loans wordmark identify this independent website only. BiLoans is not affiliated with, endorsed or sponsored by any bank, lender, credit bureau, government agency or other company referenced. All third-party names and marks belong to their respective owners and are used for identification only. &copy; <span data-year>{YEAR}</span> BiLoans.com &mdash; Webworks Media Network. All rights reserved. <a href="{r}disclosures.html">Full disclosures</a>.</p>
  </div>
 </div>
</footer>
<div class="mobile-cta"><a class="btn btn-primary btn-block" href="{r}apply.html">Get Matched &mdash; free, 2 minutes</a></div>
<div class="cookie" id="cookie" role="dialog" aria-label="Cookie consent">
 <p style="margin-bottom:10px"><strong>We value your privacy.</strong> We use cookies for analytics and to show ads that keep BiLoans free. See our <a href="{r}privacy.html#cookies">cookie policy</a>.</p>
 <div style="display:flex;gap:8px;flex-wrap:wrap"><button class="btn btn-primary btn-sm" data-consent="all">Accept all</button><button class="btn btn-ghost btn-sm" data-consent="essential">Essential only</button></div>
</div>
<script src="{r}assets/js/config.js"></script>
<script src="{r}assets/js/main.js"></script>
{extra_js}
</body>
</html>"""


def ad(slot="inArticle"):
    return f'<div class="ad-slot" data-slot="{slot}"></div>'


def faq(items):
    html = '<div class="faq">' + "".join(
        f"<details><summary>{esc(q)}</summary><p>{a}</p></details>" for q, a in items) + "</div>"
    import re
    schema = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": re.sub("<[^>]+>", "", a)}}
        for q, a in items]}
    return html, schema


def video_card(title, query, variant="", minutes="8 min"):
    q = query.replace(" ", "+")
    return f"""<a class="card video-card" href="https://www.youtube.com/results?search_query={q}" target="_blank" rel="noopener">
<div class="video-thumb {variant}">▶&nbsp; {esc(title)}</div>
<div><span class="badge">Video · {minutes}</span><h3 style="margin-top:8px">{esc(title)}</h3></div></a>"""


def form_extras():
    return '<input type="text" name="_honey" class="hp" tabindex="-1" autocomplete="off" aria-hidden="true">'


def consent_line(what="respond to my request"):
    return f"""<label class="consent"><input type="checkbox" name="consent" value="yes" required>
<span>I agree to the <a href="{{R}}terms.html">Terms</a> and <a href="{{R}}privacy.html">Privacy Policy</a> and consent to BiLoans contacting me by email or phone to {what}. Consent is not a condition of any purchase.</span></label>"""


def page_hero(eyebrow, h1, lead, crumbs=None, root=""):
    c = ""
    if crumbs:
        c = '<nav class="crumbs" aria-label="Breadcrumb"><a href="' + root + 'index.html">Home</a> › ' + " › ".join(
            (f'<a href="{root}{h}">{esc(l)}</a>' if h else esc(l)) for l, h in crumbs) + "</nav>"
    return f"""<section class="page-hero"><div class="container">{c}<span class="eyebrow">{eyebrow}</span><h1>{h1}</h1><p class="lead" style="max-width:760px">{lead}</p></div></section>"""


def write(path, title, desc, body, schema=None, extra_js="", noindex=False, priority="0.7", root=None):
    depth = path.count("/")
    root = "../" * depth if root is None else root
    body = body.replace("{R}", root)
    doc = head(title, desc, path, root, schema, noindex) + header(root) + body + footer(root, extra_js.replace("{R}", root))
    full = os.path.join(OUT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(doc)
    if not noindex:
        PAGES.append((path, priority))


def cta_band(root="{R}"):
    return f"""<section class="section-sm"><div class="container"><div class="cta-band">
<div><h2 style="margin-bottom:6px">Ready to see what you qualify for?</h2><p style="margin:0">Free, no obligation, and checking options won't affect your credit score.</p></div>
<a class="btn btn-white btn-lg" href="{root}apply.html">Get Matched →</a></div></div></section>"""
