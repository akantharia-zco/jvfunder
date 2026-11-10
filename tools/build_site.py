#!/usr/bin/env python3
"""Builds the generated pages: one page per opportunity, the dashboard preview and the thank-you page.
Edit tools/projects.json to change opportunity details, then run:  python3 tools/build_site.py
It also writes projects.js, which the home page uses for the opportunity cards."""
import json, html, os
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EMAIL='investors@jvfunder.com'
E=html.escape
projects=json.load(open(os.path.join(ROOT,'tools','projects.json'),encoding='utf-8'))

def nav():
    return '''<nav aria-label="Main navigation">
<a class="logo" href="index.html" aria-label="JvFunder — Ownership with oversight"><img src="assets/logo.png" alt="JvFunder — Ownership with oversight" width="900" height="180"></a>
<div class="links" id="site-links"><a href="index.html#opportunities">Opportunities</a><a href="index.html#oversight">Our approach</a><a href="index.html#ethical">Ethical funding</a><a href="index.html#questions">FAQs</a><a class="access" href="investor-access.html">Investor access</a><a class="btn menu-cta" href="investor-access.html#request">Request packet <span>↗</span></a></div>
<a class="btn" href="investor-access.html#request">Request packet <span>↗</span></a><button type="button" class="menu-toggle" aria-label="Menu" aria-expanded="false" aria-controls="site-links"><span></span><span></span><span></span></button>
</nav>'''

def footer():
    return '''<footer>
<div class="top">
<a class="logo" href="index.html" aria-label="JvFunder"><img src="assets/logo-light.png" alt="JvFunder — Ownership with oversight" width="900" height="180"></a>
<span class="small">Joint venture investing.<br><br>Active project oversight.</span>
</div>
<div class="foot-cols">
<div><h4>Platform</h4><a href="index.html#opportunities">Opportunities</a><a href="index.html#oversight">Our approach</a><a href="index.html#ethical">Ethical funding</a><a href="index.html#questions">FAQs</a></div>
<div><h4>Investors</h4><a href="investor-access.html">Investor access</a><a href="investor-dashboard.html">Dashboard preview</a><a href="investor-access.html#request">Request packet</a><a href="mailto:%(e)s">%(e)s</a></div>
<div><h4>Legal</h4><a href="legal.html#terms">Terms of use</a><a href="legal.html#privacy">Privacy policy</a><a href="legal.html#risk">Risk disclosures</a><a href="legal.html#disclosures">Important disclosures</a></div>
<div><h4>Sponsor</h4><a href="https://www.z-co.info" rel="noopener">Z-Co Development Corp</a><span class="foot-note">JvFunder is a Z-Co. company.</span></div>
</div>
<p>JvFunder is a proposed Z-Co. investor platform. This website presents a business concept and potential project pipeline. It is not an offer to sell or a solicitation to buy securities. Any future investment must be made through the applicable offering materials and approved process. Private investments involve risk, including loss of capital and limited liquidity. Project review and oversight do not guarantee performance. Proposed platform features are subject to implementation and validation.</p>
<p class="fwd">Certain statements on this website, including descriptions of proposed projects, structures, timelines and potential outcomes, are forward-looking and are not guarantees. Actual results may differ materially. Past performance of Z-Co. or its affiliates is not indicative of future results.</p>
<div class="copyright"><span>© 2026 JvFunder · A Z-Co. initiative</span><a href="index.html#questions">Platform status &amp; questions ↗</a></div>
</footer>''' % {'e':EMAIL}

def page(title,desc,body,image='assets/dovetrails-hero.jpg',robots=None,path=''):
    meta='<meta name="robots" content="noindex">' if robots else ''
    return '''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="description" content="%(d)s">
<title>%(t)s</title>
<meta property="og:type" content="website"><meta property="og:site_name" content="JvFunder"><meta property="og:title" content="%(t)s"><meta property="og:description" content="%(d)s"><meta property="og:image" content="https://jvfunder.com/%(img)s">
%(m)s
<link rel="icon" type="image/png" href="assets/favicon.png">
<link rel="stylesheet" href="styles.css">
</head>
<body>
%(nav)s
<main>
%(b)s
</main>
%(f)s
<script src="site.js"></script>
<script src="inquiry.js"></script>
</body>
</html>
''' % {'d':E(desc),'t':E(title),'img':image,'m':meta,'nav':nav(),'b':body,'f':footer()}

def project_page(p,idx):
    others=[q for q in projects if q['slug']!=p['slug']][:3]
    facts=[['Sponsor','Z-Co Development Corp'],['Status','Pipeline candidate · Not open for investment'],['Category',p['category']],['Type','Real estate' if p['type']=='real' else 'Operating business']]+p.get('facts',[])
    fx=''.join('<div><dt>%s</dt><dd>%s</dd></div>'%(E(a),E(b)) for a,b in facts)
    over='<p class="lead-p">%s</p>'%E(p['desc'])
    if p.get('detail'): over+='<p>%s</p>'%E(p['detail'])
    cards=''.join('<a class="mini-card" href="project-%s.html"><img src="%s" alt="%s project concept rendering" loading="lazy"><div><span class="small">%s</span><strong>%s</strong></div></a>'%(q['slug'],q['pageImage'],E(q['name']),E(q['category']),E(q['name'])) for q in others)
    body='''<section class="project-hero">
<div class="project-hero-text"><a class="crumb" href="index.html#opportunities">← All opportunities</a><span class="small">%(cat)s</span><h1>%(name)s</h1><p>%(desc)s</p><div class="hero-btns"><a class="btn light" href="investor-access.html#request">Request packet <span>↗</span></a></div></div>
<div class="project-hero-img"><img src="%(img)s" alt="%(name)s project concept rendering"><span class="badge">Planned opportunity</span></div>
</section>
<section class="project-body">
<div class="project-main">
<span class="small">Overview</span><h2>About %(name)s</h2>
%(over)s
<p class="note">Concept renderings illustrate the proposed project; final designs may change. This is a concept pipeline entry only. It is not an open offering, an investment recommendation, or a confirmation of ethical funding approval. Availability, terms, and eligibility will be defined in the applicable offering documents.</p>
</div>
<aside class="project-side">
<span class="small">Project facts</span>
<dl class="facts">%(fx)s</dl>
</aside>
</section>
<section class="project-info">
<div><span class="small">Sponsor</span><h3>Z-Co Development Corp</h3><p>Z-Co Development Corp is a privately held, vertically integrated real estate company. Founded by Mike Butte in 2003, the firm has completed more than 50 projects across six asset classes, through multiple economic cycles, with zero abandonments.</p><a class="textlink" href="index.html#about">About the sponsor <span>↗</span></a></div>
<div><span class="small">Investment information</span><h3>Terms are not yet published.</h3><p>Offering structure, capital requirements, investor economics, fees, risks, and any ethical funding review status must be established before participation. No investment terms are presented here. Offering materials are provided to eligible investors on request.</p><a class="textlink" href="legal.html#risk">Risk disclosures <span>↗</span></a></div>
<div><span class="small">Oversight</span><h3>Ownership with Oversight.</h3><p>Our proposed oversight model follows a venture from initial review through execution and exit: feasibility, budget and capital structure review, milestone reporting, and defined responsibilities and corrective actions.</p><a class="textlink" href="investor-dashboard.html">Dashboard preview <span>↗</span></a></div>
</section>
<section class="project-cta"><div><span class="small">Interested in %(name)s?</span><h2>Request an investor packet.</h2></div><a class="btn" href="investor-access.html#request">Request packet <span>↗</span></a></section>
<section class="project-more"><span class="small">Other opportunities</span><div class="mini-grid">%(cards)s</div></section>''' % {'cat':E(p['category']),'name':E(p['name']),'desc':E(p['desc']),'img':p['pageImage'],'over':over,'fx':fx,'cards':cards}
    return page('%s — JvFunder'%p['name'],p['desc'],body,p['pageImage'])

for i,p in enumerate(projects):
    open(os.path.join(ROOT,'project-%s.html'%p['slug']),'w',encoding='utf-8').write(project_page(p,i))

# projects.js for the home page cards
js=[{k:p[k] for k in ('slug','name','image','type','category','desc','color') if k in p}|({'fund':True} if p.get('fund') else {}) for p in projects]
open(os.path.join(ROOT,'projects.js'),'w',encoding='utf-8').write('// Generated by tools/build_site.py from tools/projects.json. Do not edit by hand.\nconst ventures='+json.dumps(js,ensure_ascii=False)+';\n')

# thank-you page
ty='''<section class="page-hero"><span class="small">Request received</span><h1>Thank you.</h1><p>A member of the JvFunder team will follow up with eligibility information and next steps. Submitting a request does not create an investment commitment or reservation.</p><div class="hero-btns"><a class="btn light" href="index.html">Back to home <span>↗</span></a><a class="btn light" href="index.html#opportunities">Explore opportunities <span>↗</span></a></div></section>'''
open(os.path.join(ROOT,'thank-you.html'),'w',encoding='utf-8').write(page('Thank you — JvFunder','Your request has been received.',ty,robots=True))

# dashboard preview
rows=[('Sample Venture A','Real estate','In development','Milestone report posted'),('Sample Venture B','Operating business','Operating','Quarterly update available'),('Sample Venture C','Real estate','Planned','Offering documents posted')]
tr=''.join('<div class="dash-row"><span><strong>%s</strong><em>%s</em></span><span><i class="st"></i>%s</span><span>%s</span><span class="lnk">View</span></div>'%r for r in rows)
dash='''<section class="page-hero"><span class="small">Investor dashboard</span><h1>One relationship. One view of your investments.</h1><p>An illustrative preview of the secure investor portal planned for JvFunder, showing what approved investors will be able to see.</p></section>
<section class="dash-section">
<div class="dash-note"><strong>Illustrative preview.</strong> Everything below is sample content for design purposes only. It does not show real investments, performance, or investor data. The investor portal will be provided through a secure third-party platform, and its features and availability are subject to implementation and compliance review.</div>
<div class="dash-frame" role="img" aria-label="Illustrative preview of the JvFunder investor dashboard with sample data">
<div class="dash-bar"><span class="dash-dots"><i></i><i></i><i></i></span><span class="dash-url">portal.jvfunder.com</span><span class="dash-tag">SAMPLE DATA</span></div>
<div class="dash-app">
<div class="dash-side"><b>JvFunder</b><span class="on">Overview</span><span>My investments</span><span>Documents</span><span>Distributions</span><span>Updates</span><span>Opportunities</span><span>Profile</span></div>
<div class="dash-main">
<div class="dash-stats"><div><small>Active investments</small><b>3</b></div><div><small>New documents</small><b>2</b></div><div><small>Unread updates</small><b>4</b></div><div><small>Next report</small><b>Quarterly</b></div></div>
<div class="dash-cols">
<div class="dash-panel"><h4>Investments</h4><div class="dash-table"><div class="dash-row head"><span>Investment</span><span>Status</span><span>Latest update</span><span></span></div>%s</div></div>
<div class="dash-panel"><h4>Project progress</h4>
<div class="bar-row"><span>Milestones</span><div class="bar"><i style="width:70%%"></i></div></div>
<div class="bar-row"><span>Budget used</span><div class="bar"><i style="width:55%%"></i></div></div>
<div class="bar-row"><span>Reporting</span><div class="bar"><i style="width:85%%"></i></div></div>
<h4 class="mt">Recent updates</h4>
<ul class="feed"><li><b>Milestone report</b><span>Sample · Venture A</span></li><li><b>Quarterly investor report</b><span>Sample · Venture B</span></li><li><b>Documents added</b><span>Sample · Venture C</span></li></ul></div>
</div></div></div></div>
</section>
<section class="dash-features">
<span class="small">What investors will be able to see</span>
<h2>Everything in one secure place.</h2>
<div class="feat-grid">
<div><h3>Holdings overview</h3><p>A single view of each investment you hold across the Z-Co. pipeline.</p></div>
<div><h3>Project milestones</h3><p>Planned versus actual progress for each venture.</p></div>
<div><h3>Capital deployment</h3><p>How capital is being used against the approved budget.</p></div>
<div><h3>Documents</h3><p>Offering materials, subscription documents, reports and tax documents.</p></div>
<div><h3>Distributions</h3><p>Distribution history and statements, when applicable.</p></div>
<div><h3>Updates and alerts</h3><p>Management updates and notices about material changes.</p></div>
<div><h3>Future opportunities</h3><p>New ventures from the Z-Co. pipeline, shown to approved investors.</p></div>
<div><h3>Secure access</h3><p>Sign-in and protections provided by a secure investor platform.</p></div>
</div>
<div class="dash-cta"><a class="btn" href="investor-access.html#request">Request packet <span>↗</span></a><a class="btn outline" href="investor-access.html">Investor access <span>↗</span></a></div>
</section>''' % tr
open(os.path.join(ROOT,'investor-dashboard.html'),'w',encoding='utf-8').write(page('Investor dashboard preview — JvFunder','An illustrative preview of the secure JvFunder investor portal, showing what approved investors will be able to see.',dash))
print('built',len(projects),'project pages')
