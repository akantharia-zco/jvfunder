# JvFunder

Static site for JvFunder, a proposed Z-Co. joint venture investor platform. Files: `index.html`, `styles.css`, `app.js`, `assets/` (project renderings).

Project data (names, descriptions, images) lives in the `ventures` array at the top of `app.js`; render images are in `assets/`.

## Before launch
- Replace all concept/pipeline copy with counsel-approved language.
- The "investor interest" tool only downloads a text brief in the visitor's browser; nothing is sent anywhere. Connect it to a CRM/email system if you want inquiries.
- No Terms/Privacy pages exist in this version; add them if counsel requires.
- Add analytics/cookie consent as required.
- Do not accept securities subscriptions through this static site unless the final regulatory/intermediary workflow permits it.

## Editing opportunities
Project details live in `tools/projects.json`. After editing, run `python3 tools/build_site.py` to regenerate each `project-*.html` page, the dashboard preview, the thank-you page and `projects.js` (used by the home page cards). Commit the generated files.

## Lead capture
The Request packet form (`inquiry.js`) currently opens the visitor's email app addressed to `INQUIRY_EMAIL`, then shows the thank-you page. When the CRM (GoHighLevel) is ready, set `INQUIRY_ENDPOINT` to its webhook or form URL and submissions will be posted as JSON instead.

## Z-Co. logo
The Z-Co. logo is at `assets/zco-logo.png`. It appears in the "How it fits together" section and the footer Sponsor column.
