"""Build BiLoans.com static site:  python3 tools/build.py"""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import blsite as S
import pages_core, pages_tools, pages_content, pages_community

pages_core.home(); pages_core.apply_page(); pages_core.personal(); pages_core.business(); pages_core.compare()
pages_tools.calculators(); pages_tools.rates(); pages_tools.global_page()
pages_content.build_articles(); pages_content.guides_hub(); pages_content.glossary(); pages_content.videos()
pages_community.support(); pages_community.contests(); pages_community.careers(); pages_community.advertise()
pages_community.contact(); pages_community.about(); pages_community.money(); pages_community.legal(); pages_community.notfound()

out = S.OUT
urls = "".join(f"<url><loc>{S.BASE}{p.replace('index.html', '')}</loc><lastmod>2026-09-22</lastmod><priority>{pr}</priority></url>" for p, pr in S.PAGES)
open(os.path.join(out, "sitemap.xml"), "w").write(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>\n')
open(os.path.join(out, "robots.txt"), "w").write(f"User-agent: *\nAllow: /\n\nSitemap: {S.BASE}sitemap.xml\n")
open(os.path.join(out, "ads.txt"), "w").write("# Add your AdSense line after approval, e.g.:\n# google.com, pub-0000000000000000, DIRECT, f08c47fec0942fa0\n")
open(os.path.join(out, ".nojekyll"), "w").write("")
print(f"Built {len(S.PAGES) + 1} pages")
