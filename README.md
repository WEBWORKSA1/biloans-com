# BiLoans.com: Business & Individual Loans in One Place

A static, zero-backend comparison, calculator and lead-generation website for personal and business loans. It is hosted free on GitHub Pages.

**Live:** https://webworksa1.github.io/biloans-com/

## What's inside
- **Lead generation.** `apply.html` is a multi-step "Get Matched" wizard with Personal, Business and Both paths. It includes a TCPA-style consent line, UTM capture, client-side lead scoring (A–D tier) and autosave.
- **9 calculators.** Payment/EMI with amortization, true APR, affordability, DTI, consolidation savings, business loan, SBA 7(a), MCA factor rate to APR, and Offer A vs B. All support multiple currencies.
- **Money pages.** Personal and business hubs, a sortable and filterable lender-type comparison with Featured Partner slots, a rate tracker, and loans by country (US/CA/UK/IN).
- **Content engine.** 8 long-form guides with Article, FAQ and Breadcrumb schema, a 60-term glossary and a video hub.
- **Community.** Donations/pledges with allocation goals (operations, marketing, hiring, contests), contests with official rules, careers and talent pool, and advertise/partner pages.
- **Trust and legal.** Advertiser disclosure, methodology, privacy (cookies/AdSense), terms, and not-a-lender, trademark and copyright disclosures.
- **Every page** has the top strip linking to https://web.works/contact for website, domain, sponsorship, advertisement and partnership inquiries.

## Configure (`assets/js/config.js`)

| Setting | What it does |
|---|---|
| `adsenseClient` | Paste `ca-pub-…` to switch all ad slots to AdSense. When empty, slots show "Advertise here" house ads. |
| `formAlias` | Optional FormSubmit alias string. It replaces the built-in obfuscated inbox. |
| `payments` | PayPal, Buy Me a Coffee, Stripe or Ko-fi links for the Support page. |
| `youtube.featured.id` | An 11-character YouTube video ID to feature on the home and video pages. |
| `goals` | Donation goal progress bars. |

### Forms
All forms post through FormSubmit (AJAX) to the owner's inbox. The address never appears in HTML or in visible text; it is assembled at runtime.

On the **very first submission**, FormSubmit sends a one-time activation email to that inbox. Click **Activate**, and all later submissions arrive normally.

After activation, you can paste FormSubmit's random alias into `formAlias`.

Also add `ads.txt` after AdSense approval.

## Edit and rebuild
Pages are generated from `tools/*.py`:

```bash
python3 tools/build.py
```

## Custom domain (when ready)
1. Add a `CNAME` file containing `biloans.com`.
2. Point the DNS A records to `185.199.108.153`, `185.199.109.153`, `185.199.110.153` and `185.199.111.153`.
3. Set `BASE` in `tools/blsite.py` and `siteUrl` in `config.js`.
4. Update the `/biloans-com/` root in the 404 page, then rebuild.
5. Enable "Enforce HTTPS" in Settings → Pages.

## Legal
"BiLoans" and the Bi|Loans wordmark identify this independent website only. It is not affiliated with any lender, bank, bureau or agency. All third-party marks belong to their owners. © 2026 BiLoans.com / Webworks Media Network. See `disclosures.html`.

Strategy and the phase-wise build prompt are in [`docs/STRATEGY-AND-BUILD-PROMPT.md`](docs/STRATEGY-AND-BUILD-PROMPT.md).
