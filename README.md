# SHHA website

The static website for the Somali Haemophilia and Haemoglobinopathies Association. It is plain HTML, CSS and a small script, with no framework. Pages load quickly on phones and slow connections.

## Folders

- `src/pages/`: one file per page. Edit page content here.
- `src/partials/`: shared pieces such as the emergency line, the help strip, the inheritance diagrams and the latest-news cards. Pages pull them in with `{{> name}}`.
- `src/layout.html`: the header, menu and footer that every page shares.
- `static/`: the stylesheet, the script and the images. The doodle illustrations are in `static/img/art/`.
- `tools/art/`: the scripts that draw the doodle illustrations.
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

## Publish

The site is live on GitHub Pages at https://mohstaf.github.io/shha-website/. The source is on the `main` branch of https://github.com/mohstaf/shha-website, and the built site is on the `gh-pages` branch. To publish changes, build, commit, then push both branches:

```bash
python3 build.py && git add -A && git commit -m "Update site" && git push && git push origin `git subtree split --prefix public main`:gh-pages --force
```

## Before launch

- **Forms:** forms show the WhatsApp and email alternatives until they are connected. To connect them, set `FORM_ENDPOINT` at the top of `static/js/main.js` to a form service endpoint, such as Formspree.
- **Somali:** `so.html` must be checked by a native speaker. Full Somali translations of every page are still to come.
- **Illustrations:** the site uses its own doodle illustrations instead of photos, so there are no stock photos to replace. They live in `static/img/art/`. To change a drawing, edit `tools/art/doodles.py` (the figures) or `tools/art/scenes.py` (the layouts), then run `python3 tools/art/generate.py` and `python3 build.py`. The President's profile photo on `president.html` is a real photo. The Data Scientist profile uses a doodle portrait until a photo is added at `static/img/mohamed-mustaf-ahmed.jpg`.
- **Social links:** the footer has no social media links yet. Add a "Follow us" column in `src/layout.html` once SHHA has its Facebook, LinkedIn, X or WhatsApp channel pages.
- **Email:** choose one official address. The site uses info@haemophilia-somalia.org.
- **Medical review:** the Medical Advisory Committee should review the condition pages before they are published.
