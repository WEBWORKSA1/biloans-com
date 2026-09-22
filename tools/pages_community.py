"""Community (donate, contests, careers, advertise), company & legal pages."""
from blsite import *  # noqa


def support():
    body = page_hero("Support BiLoans", "Keep borrowing help free for everyone",
                     "BiLoans is independent. Your support funds free tools, honest guides, community contests and the people who build them.", [("Support", "")]) + f"""
<section style="padding-top:10px"><div class="container split">
 <div class="form-card">
  <h2 style="font-size:1.5rem">Make a contribution</h2>
  <form data-bl-form="Donation pledge" data-ok="Thank you! We've received your pledge and will email you secure payment instructions and a receipt shortly.">{form_extras()}
   <div class="tabs" style="margin-bottom:12px"><label class="tile" style="flex:1"><input type="radio" name="frequency" value="one-time" checked><span>One-time</span></label><label class="tile" style="flex:1"><input type="radio" name="frequency" value="monthly"><span>Monthly</span></label></div>
   <div class="amounts">{"".join(f'<button type="button" class="btn {"btn-primary" if a == 25 else "btn-ghost"}" data-amount="{a}">${a}</button>' for a in (5, 10, 25, 50, 100, 250))}</div>
   <div class="field" style="margin-top:14px"><label for="donAmount">Amount (USD)</label><input id="donAmount" name="amount" type="number" min="1" value="25" required></div>
   <div class="field"><label for="alloc">Direct my support to</label><select id="alloc" name="allocation"><option>Where it's needed most</option><option>Operations &amp; hosting</option><option>Promotions &amp; marketing</option><option>Hiring talent (writers, reviewers, creators)</option><option>Contests &amp; prizes</option><option>Free financial-literacy education</option></select></div>
   <div class="row2"><div class="field"><label for="dname">Name</label><input id="dname" name="name" required autocomplete="name"></div><div class="field"><label for="demail">Email</label><input id="demail" name="email" type="email" required autocomplete="email"></div></div>
   <div class="field"><label for="dmsg">Message (optional)</label><textarea id="dmsg" name="message" rows="2"></textarea></div>
   <label class="consent" style="margin-bottom:10px"><input type="checkbox" name="supporter_wall" value="yes"><span>List my first name on the supporter wall.</span></label>
   <label class="consent"><input type="checkbox" name="consent" value="yes" required><span>I understand contributions support BiLoans' operations and are not tax-deductible charitable donations unless stated on my receipt.</span></label>
   <button class="btn btn-green btn-lg btn-block" style="margin-top:16px" type="submit">Pledge my support 💙</button>
   <div class="form-msg"></div>
  </form>
  <div style="margin-top:16px;display:flex;gap:8px;flex-wrap:wrap">
   <a class="btn btn-ghost btn-sm" data-pay="paypal" href="#">PayPal</a><a class="btn btn-ghost btn-sm" data-pay="buymeacoffee" href="#">Buy Me a Coffee</a><a class="btn btn-ghost btn-sm" data-pay="stripe" href="#">Card (Stripe)</a><a class="btn btn-ghost btn-sm" data-pay="kofi" href="#">Ko-fi</a>
  </div>
 </div>
 <div>
  <h2 style="font-size:1.5rem">Where your support goes</h2>
  <div id="goals"></div>
  <div class="grid g2" style="margin-top:20px">
   <div class="card"><div class="ico">⚙️</div><h3>Operations</h3><p class="muted">Hosting, data, security and keeping every tool free.</p></div>
   <div class="card green"><div class="ico">📣</div><h3>Promotions &amp; marketing</h3><p class="muted">Reaching borrowers who need unbiased guidance.</p></div>
   <div class="card amber"><div class="ico">🧑‍🤝‍🧑</div><h3>Hiring talent</h3><p class="muted">Writers, credit reviewers, video creators and developers.</p></div>
   <div class="card"><div class="ico">🏆</div><h3>Contests &amp; prizes</h3><p class="muted">Rewarding financial-literacy stories and creativity.</p></div>
  </div>
  <div class="notice green" style="margin-top:20px"><strong>Other ways to help:</strong> share BiLoans, <a href="{{R}}contests.html">enter a contest</a>, <a href="{{R}}careers.html">volunteer your skills</a>, or <a href="{{R}}advertise.html">sponsor a tool</a>.</div>
 </div>
</div></section>
<section class="bg-alt"><div class="container narrow">
 <h2>Supporter FAQ</h2>{faq([("Is my contribution tax-deductible?", "BiLoans is not a registered charity, so contributions are generally not tax-deductible. Your receipt will state this clearly."), ("How do I pay?", "Use a payment button above if shown, or submit the pledge form and we'll email secure payment options (card, PayPal, bank transfer)."), ("Can I cancel a monthly contribution?", "Yes, anytime. Just reply to any receipt or use the contact page."), ("Do sponsors influence your content?", "No. Donations and sponsorships never affect our editorial ratings.")])[0]}</div></section>"""
    write("support.html", "Support BiLoans: Donate to Keep Loan Help Free",
          "Support BiLoans with a one-time or monthly contribution. Fund operations, marketing, hiring talent and community contests with prizes.", body, priority="0.6")


def contests():
    C = [("Debt-Freedom Story", "Tell us how you paid off debt or turned your finances around, in 300–800 words.", "$500 / $250 / $100", "Open", "green"),
         ("Best Budget Hack Video", "A 60-second video (Reels/Shorts/TikTok) sharing your best money-saving or budgeting hack.", "$750 / $300 / $150", "Open", ""),
         ("Student Financial-Literacy Essay", "Students 18+: 'What I wish I knew about borrowing before I turned 18'.", "$1,000 scholarship-style prize", "Coming soon", "amber"),
         ("Refer-a-Business Challenge", "Refer small businesses to BiLoans. Top referrers each quarter win.", "$1,000 pool", "Coming soon", "amber")]
    cards = "".join(f'<div class="card {c}"><span class="badge {c}">{s}</span><h3 style="margin-top:10px">{t}</h3><p class="muted">{d}</p><p><strong>Prizes:</strong> {p}</p></div>' for t, d, p, s, c in C)
    body = page_hero("Contests &amp; prizes", "Win prizes for smart money moves",
                     "Share your story, your best budget hack or your creativity, and inspire thousands of borrowers.", [("Contests", "")]) + f"""
<section style="padding-top:10px"><div class="container">
 <div class="grid g2">{cards}</div>
 {ad("inArticle")}
 <div class="split" style="margin-top:30px">
  <div class="form-card"><h2 style="font-size:1.5rem">Enter a contest</h2>
   <form data-bl-form="Contest entry" data-ok="Entry received! We'll confirm by email. Good luck!">{form_extras()}
    <div class="field"><label for="ct">Contest</label><select id="ct" name="contest" required>{"".join(f"<option>{t}</option>" for t, *_ in C)}</select></div>
    <div class="row2"><div class="field"><label for="cn">Full name</label><input id="cn" name="name" required></div><div class="field"><label for="ce">Email</label><input id="ce" name="email" type="email" required></div></div>
    <div class="row2"><div class="field"><label for="cc">Country</label><input id="cc" name="country" required></div><div class="field"><label for="cl">Link to entry (video / doc / post)</label><input id="cl" name="entry_link" type="url" placeholder="https://"></div></div>
    <div class="field"><label for="cs">Your entry or summary</label><textarea id="cs" name="entry_text" rows="5" required></textarea></div>
    <label class="consent" style="margin-bottom:8px"><input type="checkbox" name="age_confirm" value="18+" required><span>I confirm I am 18 or older (or the age of majority where I live).</span></label>
    {consent_line("administer this contest, and I agree to the Official Rules")}
    <button class="btn btn-primary btn-lg btn-block" style="margin-top:14px" type="submit">Submit entry</button><div class="form-msg"></div>
   </form></div>
  <div><h2 style="font-size:1.5rem">Official rules (summary)</h2>
   <ol><li><strong>No purchase necessary.</strong> A purchase or loan application does not improve your chances of winning.</li>
   <li>Open to individuals 18+ (or the age of majority) where contests are legal. Void where prohibited. Residents of Québec: entries accepted where compliant with local rules.</li>
   <li>Entries must be original and owned by the entrant. By entering, you grant BiLoans a non-exclusive licence to publish the entry with credit.</li>
   <li>Winners are chosen by a judging panel on originality (40%), usefulness (40%) and clarity (20%). Skill-testing question may apply (Canada).</li>
   <li>Prizes are paid within 30 days of verification. Winners are responsible for applicable taxes.</li>
   <li>Each contest's dates are announced on this page and by email.</li>
   <li>BiLoans may cancel or modify a contest if fraud or technical issues compromise its integrity.</li></ol>
   <div class="notice blue">Want to <strong>sponsor a prize</strong>? Lenders, fintechs and brands can fund prize pools. <a href="{{R}}advertise.html">Become a contest sponsor →</a></div>
  </div>
 </div>
</div></section>"""
    write("contests.html", "Contests & Prizes: Share Your Money Story and Win | BiLoans",
          "Enter BiLoans contests, including debt-freedom stories, budget-hack videos and financial-literacy essays, and win cash prizes.", body, priority="0.6")


def careers():
    R = [("Personal Finance Writer", "Freelance · Remote", "Write clear, accurate guides on loans, credit and budgeting."),
         ("Credit & Lending Expert Reviewer", "Contract · Remote", "Fact-check content; CFP, CFA, CPA, lending or credit-counselling background preferred."),
         ("YouTube Video Editor / Creator", "Freelance · Remote", "Produce short explainers and weekly rate-update videos."),
         ("SEO & Content Strategist", "Part-time · Remote", "Own keyword strategy, programmatic pages and internal linking."),
         ("Partnerships Manager", "Commission + base · Remote", "Sign lenders, lead buyers and sponsors."),
         ("Front-end Developer", "Contract · Remote", "Build calculators and interactive tools in vanilla JS."),
         ("Campus / Community Ambassador", "Volunteer + rewards", "Run financial-literacy workshops and share BiLoans in your community.")]
    cards = "".join(f'<div class="card"><span class="badge">{t}</span><h3 style="margin-top:10px">{r}</h3><p class="muted">{d}</p></div>' for r, t, d in R)
    body = page_hero("Careers &amp; talent", "Help millions borrow smarter",
                     "BiLoans is a remote-first team of writers, reviewers, creators and builders. Freelancers, experts and ambassadors welcome.", [("Careers", "")]) + f"""
<section style="padding-top:10px"><div class="container">
 <div class="grid g3">{cards}</div>
 <div class="split" style="margin-top:34px">
  <div><h2>Why work with BiLoans</h2><ul class="checks" style="flex-direction:column"><li>Remote-first, flexible hours</li><li>Byline credit and a growing audience</li><li>Performance bonuses funded by partner revenue</li><li>Work that helps people make better money decisions</li></ul>
   <div class="notice">BiLoans will never ask applicants for payment, bank logins or equipment purchases. Report suspicious "BiLoans" job offers via our contact page.</div></div>
  <div class="form-card"><h2 style="font-size:1.5rem">Apply or join the talent pool</h2>
   <form data-bl-form="Career application" data-ok="Thanks! Your application is in. We review every submission and will be in touch if there's a fit.">{form_extras()}
    <div class="field"><label for="role">Role</label><select id="role" name="role" required>{"".join(f"<option>{r}</option>" for r, *_ in R)}<option>Other / open application</option></select></div>
    <div class="row2"><div class="field"><label for="an">Full name</label><input id="an" name="name" required></div><div class="field"><label for="ae">Email</label><input id="ae" name="email" type="email" required></div></div>
    <div class="row2"><div class="field"><label for="al">Portfolio / LinkedIn</label><input id="al" name="portfolio" type="url" placeholder="https://"></div><div class="field"><label for="ac">Country / timezone</label><input id="ac" name="location"></div></div>
    <div class="field"><label for="am">Why you? (experience, availability, rate)</label><textarea id="am" name="message" rows="5" required></textarea></div>
    {consent_line("review my application")}
    <button class="btn btn-primary btn-lg btn-block" style="margin-top:14px" type="submit">Send application</button><div class="form-msg"></div>
   </form></div>
 </div>
</div></section>"""
    write("careers.html", "Careers at BiLoans: Writers, Reviewers, Creators & Ambassadors",
          "Join BiLoans: remote roles for finance writers, expert reviewers, YouTube creators, SEO, partnerships, developers and community ambassadors.", body, priority="0.5")


def advertise():
    P = [("Featured Partner slot", "Top placement in comparison tables and hub pages with a 'Sponsored' label.", "From $499/mo"),
         ("Calculator sponsorship", "Your brand on a calculator used at the moment of decision.", "From $299/mo"),
         ("Lead partnership", "Receive consented, pre-screened personal or business leads (CPL / CPA / rev-share).", "Custom"),
         ("Newsletter &amp; video", "Sponsored segment in the monthly rate report or a YouTube explainer.", "From $199"),
         ("Contest sponsorship", "Fund a prize pool and get featured across contest pages.", "From $500"),
         ("Acquire the site / domain", "BiLoans.com and this platform are open to acquisition or joint-venture offers.", "Make an offer")]
    cards = "".join(f'<div class="card"><h3>{t}</h3><p class="muted">{d}</p><p style="font-weight:800;color:var(--blue)">{p}</p></div>' for t, d, p in P)
    body = page_hero("Advertise &amp; partner", "Reach borrowers at the moment they decide",
                     "Personal borrowers, self-employed professionals and small-business owners, all in high-intent research mode.", [("Advertise", "")]) + f"""
<section style="padding-top:10px"><div class="container">
 <div class="grid g3">{cards}</div>
 <div class="split" style="margin-top:34px">
  <div><h2>Audience</h2><ul class="checks" style="flex-direction:column"><li>High commercial intent: loans, credit, business funding</li><li>Dual audience: individuals and business owners</li><li>Core markets: US, Canada, UK, India</li><li>Brand-safe, compliance-first editorial environment</li></ul>
  <p class="muted">All paid placements are clearly labelled. Sponsors cannot buy editorial ratings.</p>
  <a class="btn btn-ghost" href="https://web.works/contact" target="_blank" rel="noopener">Domain / acquisition inquiries →</a></div>
  <div class="form-card"><h2 style="font-size:1.5rem">Request the media kit</h2>
   <form data-bl-form="Advertising / partnership inquiry" data-ok="Thanks! We'll send the media kit and availability within one business day.">{form_extras()}
    <div class="row2"><div class="field"><label for="vn">Name</label><input id="vn" name="name" required></div><div class="field"><label for="vc">Company</label><input id="vc" name="company" required></div></div>
    <div class="row2"><div class="field"><label for="ve">Work email</label><input id="ve" name="email" type="email" required></div><div class="field"><label for="vw">Website</label><input id="vw" name="website" type="url" placeholder="https://"></div></div>
    <div class="field"><label for="vi">Interested in</label><select id="vi" name="interest"><option>Featured partner slot</option><option>Lead partnership</option><option>Calculator sponsorship</option><option>Newsletter / video</option><option>Contest sponsorship</option><option>Buying the domain / website</option><option>Joint venture / partnership</option></select></div>
    <div class="field"><label for="vb">Monthly budget</label><select id="vb" name="budget"><option>Under $500</option><option>$500–$2,000</option><option>$2,000–$10,000</option><option>$10,000+</option></select></div>
    <div class="field"><label for="vm">Message</label><textarea id="vm" name="message" rows="4"></textarea></div>
    {consent_line("respond to my inquiry")}
    <button class="btn btn-primary btn-lg btn-block" style="margin-top:14px" type="submit">Send inquiry</button><div class="form-msg"></div>
   </form></div>
 </div>
</div></section>"""
    write("advertise.html", "Advertise, Sponsor or Partner with BiLoans",
          "Advertising, sponsorship, lead partnerships and acquisition opportunities with BiLoans, a high-intent personal and business loan audience.", body, priority="0.6")


def contact():
    body = page_hero("Contact", "Get in touch", "Questions, corrections, partnership ideas or feedback. We read every message.", [("Contact", "")]) + f"""
<section style="padding-top:10px"><div class="container split">
 <div class="form-card"><form data-bl-form="Contact" data-ok="Thanks! Your message has been sent. We usually reply within 1–2 business days.">{form_extras()}
  <div class="row2"><div class="field"><label for="n">Name</label><input id="n" name="name" required autocomplete="name"></div><div class="field"><label for="e">Email</label><input id="e" name="email" type="email" required autocomplete="email"></div></div>
  <div class="field"><label for="t">Topic</label><select id="t" name="topic"><option>General question</option><option>Help with my loan request</option><option>Content correction</option><option>Complaint</option><option>Advertising / sponsorship</option><option>Buying this website / domain</option><option>Partnership</option><option>Press</option><option>Privacy / data request</option></select></div>
  <div class="field"><label for="m">Message</label><textarea id="m" name="message" rows="6" required></textarea></div>
  {consent_line("respond to my message")}
  <button class="btn btn-primary btn-lg btn-block" style="margin-top:14px" type="submit">Send message</button><div class="form-msg"></div>
 </form></div>
 <div>
  <div class="card"><div class="ico">💼</div><h3>Domain, sponsorship &amp; partnerships</h3><p class="muted">Interested in this website, the BiLoans.com domain, sponsorship, advertising or a partnership?</p><a class="btn btn-primary" href="https://web.works/contact" target="_blank" rel="noopener">Contact via web.works</a></div>
  <div class="card" style="margin-top:18px"><div class="ico">🛡️</div><h3>Safety reminder</h3><p class="muted">BiLoans will never ask for upfront fees, passwords, OTPs or gift cards. BiLoans is not a lender and cannot approve loans.</p></div>
  <div class="card" style="margin-top:18px"><div class="ico">⏱️</div><h3>Response times</h3><p class="muted">General: 1–2 business days · Complaints: acknowledged within 3 business days · Privacy requests: within 30 days.</p></div>
 </div>
</div></section>"""
    write("contact.html", "Contact BiLoans", "Contact BiLoans with questions, corrections, complaints, advertising, partnership or domain inquiries.", body, priority="0.5")


def about():
    body = page_hero("About", "Both sides of borrowing, in one place",
                     "BiLoans (\"Bi\" for Business &amp; Individual) exists because real people's finances don't fit neatly into one box.", [("About", "")]) + f"""
<section style="padding-top:10px"><div class="container narrow article-body">
 <h2>Our mission</h2><p>Help every borrower, whether a family, a freelancer or a growing business, understand their options, see the true cost, and choose confidently. For free.</p>
 <h2>What makes BiLoans different</h2>{"<ul>" + "".join(f"<li>{x}</li>" for x in ["<strong>Dual focus.</strong> Personal and business loans compared side by side, with a dedicated path for the self-employed.", "<strong>Honest math.</strong> Nine calculators that expose fees, factor rates and total cost.", "<strong>Compliance-first.</strong> Clear disclosures, labelled sponsorships and no upfront fees, ever.", "<strong>Global lens.</strong> Guidance for the US, Canada, UK and India."]) + "</ul>"}
 <h2>Editorial standards</h2><p>Guides are researched from primary sources (regulators, lender disclosures, government programs), reviewed for accuracy, and updated regularly. Sponsors can't buy ratings or coverage. See <a href="{{R}}how-we-make-money.html">how we make money</a>.</p>
 <h2>Community</h2><p>BiLoans is supported by readers through <a href="{{R}}support.html">contributions</a>, and gives back through <a href="{{R}}contests.html">contests and prizes</a> and <a href="{{R}}careers.html">paid opportunities for talent</a>.</p>
 <p class="muted">BiLoans is a Webworks Media Network property.</p>
</div></section>{cta_band()}"""
    write("about.html", "About BiLoans: Business & Individual Loans in One Place", "BiLoans helps individuals, freelancers and businesses compare loans, understand true costs and borrow confidently.", body, priority="0.5")


def money():
    body = page_hero("Transparency", "How we make money", "Advertiser disclosure, methodology and editorial guidelines.", [("How we make money", "")]) + f"""
<section style="padding-top:10px"><div class="container narrow article-body">
 <h2 id="disclosure">Advertiser disclosure</h2><p>BiLoans is an independent, advertising-supported comparison and education service. We may receive compensation when you click links, submit a request that is shared with a partner, or are approved for a product. This compensation may affect which products appear and where (for example, "Sponsored" or "Featured partner" placements), but it does not influence our editorial content, guides or calculator results. We don't include every lender or offer on the market.</p>
 <h2>Our revenue sources</h2><ul><li><strong>Lead and referral partnerships</strong>: when you consent, we may share your request with lending or marketing partners, who may pay us.</li><li><strong>Advertising</strong>: display ads (such as Google AdSense) and clearly labelled sponsorships.</li><li><strong>Video</strong>: YouTube content and sponsorships.</li><li><strong>Community contributions</strong>: voluntary support from readers.</li></ul>
 <h2 id="methodology">Methodology</h2><p>Lender-type comparisons and rate ranges are compiled from lenders' published APR disclosures, public marketplace averages, and government program rules (e.g. SBA), and reviewed monthly. We evaluate cost (APR and fees), eligibility, speed, flexibility, transparency and customer protections. Ranges are benchmarks, not offers.</p>
 <h2>Editorial guidelines</h2><ul><li>Accuracy first: primary sources and dated updates</li><li>Separation of editorial and commercial teams</li><li>Corrections policy: report errors via <a href="{{R}}contact.html">contact</a>; material fixes are noted</li><li>Plain language and accessibility</li></ul>
 <h2>BiLoans is not a lender</h2><p>We do not make loans or credit decisions, and we don't charge borrowers fees. Lenders set rates and terms and may run credit checks when you apply with them.</p>
</div></section>"""
    write("how-we-make-money.html", "How BiLoans Makes Money: Advertiser Disclosure & Methodology", "BiLoans advertiser disclosure, revenue sources, rate methodology and editorial guidelines.", body, priority="0.5")


def legal_page(path, title, desc, h1, sections):
    s = "".join(f'<h2 id="{i}">{h}</h2>{c}' for i, h, c in sections)
    body = page_hero("Legal", h1, f"Last updated {ASOF}.", [(h1, "")]) + f'<section style="padding-top:10px"><div class="container narrow article-body">{s}</div></section>'
    write(path, title, desc, body, priority="0.3")


def legal():
    legal_page("privacy.html", "Privacy Policy | BiLoans", "How BiLoans collects, uses and protects your information.", "Privacy policy", [
        ("collect", "Information we collect", "<ul><li><strong>You provide:</strong> form details such as name, email, phone, location, loan needs, income or revenue ranges, and messages.</li><li><strong>Automatically:</strong> device, browser, pages viewed, referral and campaign (UTM) data, and cookies.</li><li>We do <strong>not</strong> ask for SSN, SIN, PAN, bank logins or card numbers in our forms.</li></ul>"),
        ("use", "How we use it", "<ul><li>To respond to you and, with your consent, share your loan request with lending or marketing partners that may help</li><li>To operate, secure and improve the site</li><li>To send newsletters you opt into</li><li>To show and measure ads</li><li>To comply with law</li></ul>"),
        ("share", "Sharing", "<p>We share personal information with (a) lending/marketing partners <strong>only when you consent</strong> on a form, (b) service providers that process data for us (e.g. form delivery, hosting, analytics, advertising), and (c) authorities when legally required. We do not sell personal information for money outside of these consented partner referrals.</p>"),
        ("cookies", "Cookies &amp; advertising", "<p>We use essential cookies and, with your consent, analytics and advertising cookies. Third-party vendors, including Google, use cookies to serve ads based on prior visits to this and other websites. Google's use of advertising cookies enables it and its partners to serve ads based on your visits. You can opt out of personalized advertising at Google Ads Settings (adssettings.google.com) or aboutads.info. Choosing 'Essential only' in our banner requests non-personalized ads.</p>"),
        ("rights", "Your rights", "<p>Depending on where you live (e.g. GDPR/UK GDPR, CCPA/CPRA, PIPEDA and Québec Law 25, India's DPDP Act), you may have rights to access, correct, delete or port your data, object to or restrict processing, withdraw consent and opt out of 'sale/sharing'. Submit requests through our <a href='{R}contact.html'>contact page</a> (topic: Privacy / data request).</p>"),
        ("retention", "Retention &amp; security", "<p>We keep data only as long as necessary for the purposes above or as required by law, and use encryption in transit (HTTPS) and access controls. No method is 100% secure.</p>"),
        ("children", "Children", "<p>BiLoans is intended for adults 18+ and does not knowingly collect data from minors.</p>"),
        ("changes", "Changes &amp; contact", "<p>We may update this policy and will revise the date above. Contact us via the <a href='{R}contact.html'>contact page</a>.</p>")])
    legal_page("terms.html", "Terms of Use | BiLoans", "Terms of use for BiLoans.com.", "Terms of use", [
        ("accept", "Acceptance", "<p>By using BiLoans.com you agree to these terms. If you don't agree, please don't use the site.</p>"),
        ("service", "Our service", "<p>BiLoans provides educational content, calculators and a matching request service. <strong>BiLoans is not a lender</strong>, does not make credit decisions, and does not guarantee that you'll be matched, receive offers, or be approved. Any loan is solely between you and the lender.</p>"),
        ("noadvice", "No financial advice", "<p>Content and calculator results are general information and estimates, not financial, legal or tax advice. Consult a qualified professional for advice about your situation.</p>"),
        ("eligible", "Eligibility &amp; accuracy", "<p>You must be 18+ (or the age of majority where you live) and provide accurate information. Don't submit information about another person without authorization.</p>"),
        ("comms", "Communications consent", "<p>If you consent on a form, BiLoans and its partners may contact you by email, phone or text, including via automated technology. Consent is not a condition of purchase. You can opt out at any time by replying STOP to texts, using unsubscribe links, or contacting us.</p>"),
        ("ip", "Intellectual property", "<p>Site content, design, calculators and code are © BiLoans.com / Webworks Media Network. You may share links and short quotes with attribution. Don't copy, scrape or republish substantial portions without permission.</p>"),
        ("third", "Third-party sites", "<p>Links to lenders and other sites are provided for convenience. We aren't responsible for their content, products or privacy practices.</p>"),
        ("liability", "Disclaimers &amp; limitation of liability", "<p>The site is provided 'as is' without warranties. To the fullest extent permitted by law, BiLoans is not liable for indirect or consequential damages arising from your use of the site or any third-party product.</p>"),
        ("contests", "Contests &amp; contributions", "<p>Contests are governed by their Official Rules. Contributions support BiLoans' operations and are non-refundable except where required by law or at our discretion.</p>"),
        ("law", "Changes &amp; governing law", "<p>We may update these terms. Continued use means acceptance. These terms are governed by the laws applicable where the site operator is established, without regard to conflict-of-law rules.</p>")])
    legal_page("disclosures.html", "Disclosures, Trademark & Copyright Notice | BiLoans", "BiLoans not-a-lender disclosure, APR and representative examples, communications consent, regional notes and trademark/copyright notice.", "Disclosures &amp; trademarks", [
        ("lender", "Not a lender", "<p>BiLoans is an independent publisher and connector. We are not a lender, bank, credit broker (where licensing is required), or financial adviser, and we don't make credit decisions or charge borrowers fees. Submitting a request does not guarantee an offer or approval.</p>"),
        ("apr", "Rates &amp; representative examples", "<p>Rates and ranges shown are illustrative market benchmarks as of " + ASOF + " and are not offers. APRs depend on credit, income, amount, term, state/province/country and lender criteria. Representative example: a $10,000 loan over 36 months at 17.59% APR (13.94% interest, 5% origination fee deducted from proceeds) has 36 monthly payments of about $341.48; you'd receive $9,500 and repay about $12,293. For illustration only.</p>"),
        ("credit", "Credit checks", "<p>BiLoans' forms don't pull your credit. Lenders may perform soft or hard inquiries when you proceed with them; hard inquiries may affect your credit score.</p>"),
        ("tcpa", "Communications consent (US)", "<p>By submitting a form with the consent box checked, you provide express written consent for BiLoans and its partners to contact you as described, including by autodialed/prerecorded calls and texts. Consent is not a condition of purchase.</p>"),
        ("regions", "Regional notes", "<ul><li><strong>Canada:</strong> the federal criminal interest rate is capped at 35% APR; provincial rules apply to high-cost credit.</li><li><strong>United Kingdom:</strong> BiLoans provides information only and does not broker regulated credit. Always check a lender's FCA authorisation.</li><li><strong>India:</strong> loans are provided by RBI-regulated banks and NBFCs; review the Key Facts Statement (KFS) before accepting.</li><li><strong>United States:</strong> loan availability, terms and licensing vary by state.</li></ul>"),
        ("ads", "Advertising", "<p>BiLoans may display Google AdSense and other ads and receive compensation from partners. Sponsored placements are labelled. See <a href='{R}how-we-make-money.html'>How we make money</a>.</p>"),
        ("tm", "Trademark notice", "<p>\"BiLoans\", \"BiLoans.com\" and the Bi|Loans wordmark are used to identify this independent website, operated by Webworks Media Network. BiLoans is <strong>not affiliated with, endorsed by, or sponsored by</strong> any bank, lender, credit bureau, card network, government agency (including the U.S. Small Business Administration, FCA, RBI or any regulator), or other company referenced. Any third-party names, trademarks, service marks and logos mentioned belong to their respective owners and are used for identification and informational purposes only (nominative fair use). No endorsement is implied. If you believe any content infringes your trademark, please contact us and we'll respond promptly.</p>"),
        ("copyright", "Copyright notice &amp; DMCA", "<p>© " + YEAR + " BiLoans.com / Webworks Media Network. All rights reserved. Original text, calculators, code, graphics and site design are protected by copyright. No third-party logos or copyrighted images are used on this site. Icons are standard Unicode emoji. To report alleged copyright infringement, send a notice via our <a href='{R}contact.html'>contact page</a> identifying the work, the infringing material and URL, your contact details, and a good-faith statement. We'll remove infringing material promptly.</p>"),
        ("accuracy", "Accuracy", "<p>We work hard to keep information accurate and current, but laws, rates and products change. Verify details directly with lenders and official sources before deciding.</p>")])


def notfound():
    body = """<section class="page-hero center"><div class="container"><div style="font-size:4rem">🧭</div><h1>Page not found</h1><p class="lead">The page you're looking for moved or never existed.</p>
<p><a class="btn btn-primary" href="{R}index.html">Go home</a> <a class="btn btn-ghost" href="{R}calculators.html">Calculators</a> <a class="btn btn-ghost" href="{R}apply.html">Get matched</a></p></div></section>"""
    # 404 must use absolute root for GitHub Pages (served at any depth)
    write("404.html", "Page not found | BiLoans", "Page not found.", body, noindex=True, root="/biloans-com/")
