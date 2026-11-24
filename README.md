# SHHA website

The static website for the Somali Haemophilia and Haemoglobinopathies Association. It is plain HTML, CSS and a small script, with no framework. Pages load quickly on phones and slow connections.

## Folders

- `src/pages/`: one file per page. Edit page content here.
- `src/partials/`: shared pieces such as the emergency line, the help strip, the inheritance diagrams and the latest-news cards. Pages pull them in with `{{> name}}`.
- `src/layout.html`: the header, menu and footer that every page shares.
- `static/`: the stylesheet, the script and the images.
- `public/`: the finished site, created by the build. Upload this folder to the web host. Don't edit it by hand.
- `docs-content-plan.md`: the content plan the pages were written from.

## Build and preview

```bash
python3 build.py
```

```bash
python3 -m http.server 8765 --directory public
```

Then open http://localhost:8765. To check that every page renders without writing anything, run `python3 build.py --check`.

## Before launch

- **Forms:** forms show the WhatsApp and email alternatives until they are connected. To connect them, set `FORM_ENDPOINT` at the top of `static/js/main.js` to a form service endpoint, such as Formspree.
- **Somali:** `so.html` must be checked by a native speaker. Full Somali translations of every page are still to come.
- **Photos:** pages across the site use free stock photos from Unsplash as placeholders (the home page, blood disorder pages, Get help, About, Programmes, Get involved, For health workers and news). They show models, not SHHA patients, and must be replaced with SHHA's own photos, taken with written consent, before launch. To swap one: save the photo in `static/img/`, replace the matching Unsplash address in the page under `src/pages/` with `img/your-file.jpg`, and run `python3 build.py`. The placeholders:
  - https://images.unsplash.com/photo-1609834017540-11372c013f98
  - https://images.unsplash.com/photo-1664874322412-66e589265c15
  - https://images.unsplash.com/photo-1664874332383-f14c222b0dde
  - https://images.unsplash.com/photo-1721713809615-eb79bf7d324b
  - https://images.unsplash.com/photo-1721713809682-38f6935d5a48
  - https://images.unsplash.com/photo-1723151684036-d014403c33b2
  - https://images.unsplash.com/photo-1729356650188-c89c401ebc48
  - https://images.unsplash.com/photo-1729356650250-83503d5b5a64
  - https://images.unsplash.com/photo-1741868159744-159b83484687
  - https://images.unsplash.com/photo-1741868643652-ff857430225b
  - https://images.unsplash.com/photo-1774870088892-714199a76e56
  - https://images.unsplash.com/photo-1774870292182-d59afbebf09e
- **Social links:** the footer has no social media links yet. Add a "Follow us" column in `src/layout.html` once SHHA has its Facebook, LinkedIn, X or WhatsApp channel pages.
- **Email:** choose one official address. The site uses info@haemophilia-somalia.org.
- **Medical review:** the Medical Advisory Committee should review the condition pages before they are published.
