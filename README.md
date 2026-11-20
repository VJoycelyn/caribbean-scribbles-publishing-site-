# Caribbean Scribbles Publishing Website

This repository contains the code for the **Caribbean Scribbles Publishing** website – a digital-first Caribbean publishing and story studio.

## Live site

The site is live at:

**https://vjoycelyn.github.io/caribbean-scribbles-publishing-site-/**

### Restoring the custom domain

`caribbeanscribblespublishing.com` expired on 16 November 2026. Namecheap replaced its DNS
records with a parking page. The domain was renewed the next day (valid until 16 November 2027),
but the DNS zone was never restored, so the domain stopped loading the site over both HTTP and
HTTPS.

The site was therefore moved to the free `github.io` address above, and the `CNAME` file was
removed. To switch back to the custom domain once DNS is repaired:

1. In Namecheap → **Domain List** → `caribbeanscribblespublishing.com` → **Advanced DNS**,
   delete the parking records and add:

   | Type  | Host | Value             |
   | ----- | ---- | ----------------- |
   | A     | @    | 185.199.108.153   |
   | A     | @    | 185.199.109.153   |
   | A     | @    | 185.199.110.153   |
   | A     | @    | 185.199.111.153   |
   | CNAME | www  | vjoycelyn.github.io |

2. In GitHub → **Settings** → **Pages**, set the custom domain to
   `caribbeanscribblespublishing.com` and enable **Enforce HTTPS**.
3. Re-create a `CNAME` file in this repository containing only
   `caribbeanscribblespublishing.com`.
4. Point the newsletter form's `_next` field in `index.html` and the `Website` links in
   `scripts/email_templates.py` back at the custom domain.

---

## About Caribbean Scribbles Publishing

Caribbean Scribbles Publishing is a small, Caribbean-rooted press and digital space that:

- Publishes children’s books, workbooks, and storybooks with a Caribbean focus  
- Supports new and emerging authors with coaching and self-publishing guidance  
- Creates resources for schools, churches, and community organisations  

This site is a simple, static front page built with **HTML, CSS and a little JavaScript**.

## Homepage chatbot

The main homepage includes **Island Guide**, a lightweight publishing-assistance chatbot. It helps visitors with:

- Publishing services, manuscript coaching, editing, layout, and KDP/IngramSpark setup
- School, NGO, church, workshop, author-talk, and community-project enquiries
- Book recommendations by age and interest
- Amazon and WhatsApp ordering guidance
- Newsletter, contact, location, rights, and project-request routing

The chatbot is intentionally client-side and does not send or store chat messages. Its answers are curated in `chatbot.js`, so no API key is exposed in the public GitHub Pages site. Project-specific requests, quotes, manuscript reviews, and rights questions are routed to the existing contact form or `caribbeanscribbles@gmail.com`.

To update chatbot wording or supported questions, edit `chatbot.js`. The launcher and dialog markup and styling are in `index.html`.

---

## How to update the website

1. Open the file `index.html` in this repository.
2. Click the **pencil icon** (Edit this file).
3. Make your changes (text, links, prices, etc.).
4. Scroll down and click **“Commit changes”**.
5. GitHub Pages will automatically rebuild and update the live site.

---

## Shop & book links

In `index.html`, you can update:

- **Shop section** – change prices and “Buy” button links to:
  - Amazon book pages  
  - WhatsApp order link  
  - Email order link  

Search in the file for `#shop` or for the book titles (e.g. `The Jingle of the Sugar Mas Bells`) and replace the `href="#"` with your real links.

---

## Contact

For updates, collaborations, or questions about the site:

- GitHub: [@VJoycelyn](https://github.com/VJoycelyn)
- Instagram: `@caribbeanscribbles` (update when your handle is ready)
- Email: `info@caribbeanscribbles.com` (or your preferred email)
