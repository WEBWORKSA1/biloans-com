# BiLoans.com — Strategy & Phase-Wise Build Prompt

_Prepared September 2026. Figures are planning estimates, not guarantees._

---

## 1. The idea (decision)

**BiLoans = "Both sides of borrowing": Business + Individual loans, in one comparison, calculator, and matching hub.**

Tagline: **"One place for Business & Individual loans."**

### Why this beats the alternatives

| Interpretation of "Bi" | Search demand | CPC / lead value | Competition | Verdict |
|---|---|---|---|---|
| **Business + Individual loans hub** | Very high (personal-loan + business-loan head terms) | Highest in AdSense (finance/loans routinely $5–$50+ CPC in US/CA/UK); business leads worth 3–10× personal leads | High, but most sites are split: NerdWallet/Credible lean personal, Lendio/Fundera lean business. The **self-employed / freelancer / sole-prop** borrower sits between both and is underserved | **Chosen** |
| Bi-weekly payment loans | Low, niche | Medium | Low | Too small; becomes one calculator on the main site |
| Bilingual loans (EN/ES, EN/FR) | Medium | Medium–high | Low–medium | Strong **Phase 5 expansion** on top of the chosen idea, not the core |
| Bridge / "BI" business-interruption loans | Low | High | Low | Content cluster, not a brand |

**The wedge:** a single "Get Matched" flow that asks *"Is this for you, your business, or both?"* in step 1. The "both" path is for owner-operators, freelancers, gig workers, and small-business founders who currently bounce between two kinds of sites. That is the differentiated position; everything else matches market standard.

### Revenue engine (in order of expected $ per visitor)

1. **Lead generation.** Multi-step forms for personal and business loans. You sell leads to lender networks and affiliate programs, or route them to partners.
2. **Sponsored placements.** "Featured Partner" slots in comparison tables and calculators, sold directly.
3. **Google AdSense** on high-intent content: guides, glossary, rate pages, calculators. Loans is one of the highest-RPM verticals.
4. **YouTube.** Explainer videos embedded on guides feed your own channel's watch time and AdSense for YouTube, and pull video search traffic back to the site.
5. **Supporter donations.** These fund operations, promotions and marketing, hiring, and contests with prizes. The pledge flow is built in.
6. **Domain / site sale, sponsorship, partnership.** There is a banner on every page for this.

### Scenario model (month 12, assumptions stated)

| Input | Conservative | Aggressive |
|---|---|---|
| Monthly sessions | 15,000 | 80,000 |
| AdSense RPM (finance, mixed geo) | $15 | $35 |
| **AdSense / month** | **$225** | **$2,800** |
| Lead form completion rate | 0.8% | 2.0% |
| Leads / month | 120 | 1,600 |
| Sellable share × average payout (personal ≈ $15–40, business ≈ $75–300) | 50% × $30 | 60% × $45 |
| **Lead revenue / month** | **$1,800** | **$43,200** |
| Sponsored slots | $0 | $2,000 |

Lead generation is roughly 85–90% of the upside. **Optimize the form before anything else.** AdSense alone won't make this a business.

### Hard constraints you need to know

- **You are a publisher/broker, not a lender.** US: TCPA consent language on forms, Truth in Lending (Reg Z) rules when you advertise a rate or payment, and state lead-gen rules. UK: brokering credit needs FCA authorisation or appointed-representative status; until you have it, keep UK pages educational only. Canada: the 35% APR criminal-rate cap. India: route leads only to RBI-regulated lenders and show the DPDP consent notice.
- **Google YMYL.** Loans content is "Your Money or Your Life". It needs named authors and reviewers, methodology, dated updates, and disclosures. These are built into the site.
- **Domain status (as of research, Sep 2026):** biloans.com showed a "for sale" landing page. Confirm the registration is in your account before you point DNS.

---

## 2. Competitive audit summary (38 finance/loan reference sites reviewed)

**Sites reviewed:**
- **US personal-loan publishers:** NerdWallet, Bankrate, LendingTree, Credit Karma, Credible, Forbes Advisor, ValuePenguin, Finder, Money.com, CNBC Select, Experian, SmartAsset.
- **US lenders:** SoFi, Upstart, LendingClub/Happen, Prosper, Upgrade, Discover, Marcus.
- **US business lending:** Fundera, Lendio, Nav, Bluevine, Fundbox, LendingTree Business, SBA.gov.
- **UK:** MoneySuperMarket, Compare the Market, Uswitch, ClearScore, Experian UK.
- **Canada:** Loans Canada, Ratehub, Borrowell.
- **India:** Paisabazaar, BankBazaar, Bajaj Finserv, Policybazaar.
- **Donation / microfinance UX:** Kiva, GoFundMe, Buy Me a Coffee.

**Patterns every market leader shares, and which BiLoans implements:**

- **Hero with a single low-friction first field** (purpose or amount) plus "Won't affect your credit score." _(Happen, Upgrade, Lendio, MoneySuperMarket)_
- **Multi-step form.** Purpose → amount → credit band → income → contact details, with a progress bar on every step and personal details asked last.
- **"Best for…" cards and a sortable comparison table** with a clearly labelled "Promoted/Featured" tag. _(CNBC Select, Finder, Bankrate)_
- **Representative APR example** on rate pages _(Upgrade, Prosper)_, and **"as of" dates** on every rate.
- **Advertiser disclosure** at the top of money pages; **"We are not a lender"** near every form.
- **Calculator library:** payment/EMI, APR with fees, affordability, DTI, consolidation savings, business loan, SBA 7(a), MCA factor-rate to APR.
- **Rate tracker by credit band.** _(Credible weekly, NerdWallet averages)_
- **Content signals:** methodology page, author and reviewer bylines, key-takeaways boxes, FAQ with schema, glossary.
- **Anti-scam notice:** "Never pay a fee before approval." _(Finder, Policybazaar)_
- **Mobile sticky CTA**; trust strip (encryption, free, no obligation).
- **Donation UX:** preset amounts, a goal progress bar, and allocation transparency. _(Kiva, Buy Me a Coffee, GoFundMe)_

---

## 3. Phase-wise build prompt

Copy each phase into your AI builder in order. Each phase is self-contained and ends with acceptance criteria.

### PHASE 0 — Global rules (prepend to every phase)

```
You are building BiLoans.com — "One place for Business & Individual loans" —
a static, zero-backend website hosted free on GitHub Pages (repo WEBWORKSA1/biloans-com).
Hard rules:
1. Pure HTML/CSS/vanilla JS. No build step required to serve. Add .nojekyll. All links relative
   so the site works at https://webworksa1.github.io/biloans-com/ AND later at https://biloans.com/.
2. Every page begins with a top strip: "Contact, if you are interested in this website / domain name /
   Sponsorship / Advertisement / Partnership" linking to https://web.works/contact.
3. The ONLY contact inbox is the owner's designated email (set privately) and it must NEVER appear in visible text, HTML
   source, mailto links, or meta tags. Assemble it at runtime in JS from char codes and submit all
   forms via AJAX to FormSubmit (formsubmit.co/ajax/…). Support swapping to a FormSubmit hashed alias
   in config so even the obfuscated address can be removed.
4. BiLoans is a publisher/connector, NOT a lender. Show "not a lender" + advertiser disclosure
   on every money page. Avoid third-party trademarks/logos; use lender categories, not brand logos.
5. Mobile-first, WCAG 2.1 AA, Lighthouse 90+ targets, light/dark theme, cookie consent,
   JSON-LD (Organization, WebSite, FAQPage, Article, BreadcrumbList), OG/Twitter tags.
6. Monetization hooks: AdSense slots (config-driven; house-ad fallback "Advertise here"),
   YouTube lite-embeds (click-to-load), Featured Partner slots, donation/pledge flows.
```

### PHASE 1 — Foundation & design system

```
Create: /assets/css/style.css (design tokens: navy #0B1F3A, trust-blue #1557FF, growth-green #12B76A,
amber accent #F5A524; Inter font; 8px spacing grid; cards, buttons, badges, tables, tabs, accordions,
steppers, sliders, progress bars), /assets/js/config.js (site settings), /assets/js/main.js
(nav, theme, cookie consent, AdSense loader, YouTube facade, FAQ accordion, forms engine).
Build a page generator (tools/build.py) with shared header/footer partials so 25+ pages stay consistent.
Header: logo "Bi|Loans" wordmark (original, text-based), mega-nav (Personal, Business, Compare,
Calculators, Rates, Learn, Community), CTA "Get Matched". Footer: 4 link columns, disclosures,
trademark/copyright notice, social placeholders.
Acceptance: header/footer identical on all pages; strip visible on all pages; no email in source.
```

### PHASE 2 — Home page & lead-generation engine (highest priority)

```
Home: hero with audience toggle [For Me | For My Business | Both], one-field starter (amount) →
deep-links into /apply.html with prefilled values. Sections: trust strip, rate snapshot cards,
"How it works" 3 steps, Personal vs Business split cards, featured calculators, comparison preview,
video row, guides row, community (contests, careers, support), newsletter, FAQ, final CTA.
/apply.html: 3-branch multi-step form (Personal 9 steps / Business 10 steps / Both = combined),
tap-tile answers, progress bar, back button, inline validation, autosave in sessionStorage,
consent checkbox with TCPA-style language, hidden fields (UTM source/medium/campaign, landing page,
referrer, lead score). Compute a lead score client-side (credit band, income, time-in-business,
revenue) and include it in the submission. Success screen with next steps + calculator links + share.
Sticky mobile "Get Matched" bar sitewide. Exit-intent modal (desktop) offering the rate guide.
Acceptance: form submits to FormSubmit AJAX; all fields reach inbox; works with JS-free fallback message.
```

### PHASE 3 — Comparison, rates & calculators

```
/personal-loans.html and /business-loans.html hubs: loan types, typical APR tables by credit band /
product (dated "as of"), eligibility, documents checklist, "Best for" category cards, FAQ.
/compare.html: sortable/filterable table of lender CATEGORIES (online lenders, banks, credit unions,
P2P, fintech LOC, SBA lenders, equipment financiers, invoice factoring, MCA, NBFCs India) with
APR range, amounts, speed, min credit, best-for; plus 3 "Featured Partner — slot available" rows.
/calculators.html: 9 calculators in tabs — Payment/EMI + amortization, APR incl. origination fee,
Affordability, DTI, Debt consolidation savings, Business term loan, SBA 7(a) (prime-plus cap),
MCA factor → APR, Offer A vs B. Each shows a CTA into /apply.html with values carried over.
/rates.html: rate tracker with a canvas/SVG chart by credit band, business product table, methodology.
```

### PHASE 4 — Content, video & SEO engine

```
/guides.html hub + 8 long-form guides in /guides/ (key takeaways, TOC, AdSense in-article slots,
YouTube facade, FAQ with schema, related links, author/reviewer bylines, updated date):
personal-loan basics, debt consolidation, business loan types, SBA loans, loans for self-employed,
credit scores & loans, avoiding loan scams, loans by country (US/CA/UK/IN).
/glossary.html (50+ terms, A–Z jump), /videos.html (YouTube hub with playlist config),
/global.html (US, Canada, UK, India sections with local rules/currency),
sitemap.xml, robots.txt, ads.txt placeholder, 404.html.
```

### PHASE 5 — Community, donations, careers, contests, advertising

```
/support.html: donation/pledge with preset amounts ($5/$10/$25/$50/$100/custom), one-time or monthly,
allocation selector (Operations, Promotions & Marketing, Hiring Talent, Contests & Prizes),
transparent allocation bars and funding goals, supporter wall opt-in, configurable payment links
(PayPal.me / Buy Me a Coffee / Stripe Payment Link) set in config.js, pledge form to inbox.
/contests.html: live contests (Debt-Freedom Story, Best Budget Hack Video, Student Financial-Literacy
Essay, Refer-a-Business), prize pool, timeline, official rules, entry form.
/careers.html: open roles (finance writers, credit-expert reviewers, YouTube editor, SEO,
partnerships, campus ambassadors) + application form. /advertise.html: packages (sponsored slot,
newsletter, calculator sponsorship, video integration, domain/site acquisition) + inquiry form.
```

### PHASE 6 — Trust, legal & launch

```
/about.html, /how-we-make-money.html (advertiser disclosure, methodology, editorial standards),
/contact.html (general form), /privacy.html, /terms.html, /disclosures.html (not-a-lender, APR/
representative example, TCPA, UK/CA/IN notes, trademark & copyright disclosure), cookie policy.
Launch: push to GitHub, enable Pages (gh-pages branch or main /root), verify every page loads,
submit sitemap to Google Search Console, apply for AdSense once 20+ quality pages are live,
activate FormSubmit (first submission sends a confirmation email to the inbox).
Later: point biloans.com DNS (A records 185.199.108-111.153 + CNAME file), enable HTTPS.
```

### PHASE 7 — Growth roadmap (post-launch)

```
- Spanish (/es/) and French (/fr/) versions → the "bilingual" angle of "Bi".
- Programmatic pages: business loans by industry (20) and by state/province (60+) — only with real local data.
- Lender partnerships → replace category rows with real partner offers + tracking links.
- Serverless lead router (Cloudflare Worker) to ping-post leads to multiple buyers.
- Email nurture sequences, rate-alert newsletter, weekly YouTube rate-update video.
```

---

## 4. Trademark & copyright disclosure (as used on the site)

"BiLoans", "BiLoans.com" and the Bi|Loans wordmark are used as the name of this independent website. BiLoans is not affiliated with, endorsed by, or sponsored by any bank, lender, credit bureau, government agency, or other company named or referred to on this site. All third-party names, trademarks, and brands belong to their respective owners and are used for identification only. Site content, design, calculators, and code © 2026 BiLoans.com / Webworks Media Network. All rights reserved.

**Clearance note:** research found no live "BiLoans" consumer brand. Nearby marks exist in unrelated or adjacent spaces, for example "Power BI" and "BI Banco Industrial". Run a USPTO (tmsearch.uspto.gov), CIPO, UK IPO and IP India search for BILOANS / BI LOANS in classes 35 and 36 before you file or spend on branding.
