# Caribbean Scribbles Publishing Website

This repository contains the code for the **Caribbean Scribbles Publishing** website – a digital-first Caribbean publishing and story studio.

## Live site

The site is served by GitHub Pages at the custom domain:

**https://caribbeanscribblespublishing.com/**

The `CNAME` file in this repository pins that domain. While a custom domain is set, the
`vjoycelyn.github.io` address redirects to it rather than serving the site directly.

### DNS records

The domain is registered with **Namecheap** (renewed through 16 November 2027). If the site ever
shows a Namecheap parking page instead of the website, the DNS zone has been reset and these
records need to be restored under **Domain List** → **Advanced DNS**:

| Type  | Host | Value               |
| ----- | ---- | ------------------- |
| A     | @    | 185.199.108.153     |
| A     | @    | 185.199.109.153     |
| A     | @    | 185.199.110.153     |
| A     | @    | 185.199.111.153     |
| CNAME | www  | vjoycelyn.github.io |

Delete any parking `A` records pointing at `104.219.250.37` or `203.161.32.252` first. In
GitHub → **Settings** → **Pages**, confirm the custom domain and keep **Enforce HTTPS** enabled.
GitHub re-issues the TLS certificate automatically once the domain resolves to its servers.

### Temporary fallback

If the domain needs to be taken out of service, deleting the `CNAME` file makes GitHub Pages
serve the site at `https://vjoycelyn.github.io/caribbean-scribbles-publishing-site-/`. Also
update the newsletter form's `_next` field in `index.html` and the `Website` links in
`scripts/email_templates.py` so they don't point at the unavailable domain.

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
