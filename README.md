# Kofi Ampomah — Personal PhD Portfolio Website

Live site: **[ampomah-kofi.github.io](https://ampomah-kofi.github.io/)**

Personal academic portfolio for Kofi Ampomah, PhD Student in Computer Science at the University of Alabama (UA-SPECTRAL Lab). Research focus: Usable Security & Privacy, Human-Centered Computing, Responsible AI, and AI Policy.

---

## Tech Stack

- **Hugo** — static site generator (theme: Ananke)
- **Vanilla HTML / CSS / JavaScript** — single-page portfolio (`docs/index.html`)
- **GitHub Pages** — hosting via GitHub Actions (`/.github/workflows/deploy.yml`)
- **Font Awesome 6** — icons
- **Google Fonts** — Roboto, Roboto Slab, Roboto Mono

---

## Project Structure

```
my_personalphd_website/
├── docs/                   # Published site (served by GitHub Pages)
│   ├── index.html          # Main portfolio page (edit this)
│   ├── job-cv.html         # Industry resume page
│   ├── images/             # Profile photo and assets
│   └── ananke/css/         # Theme CSS
├── .github/workflows/
│   └── deploy.yml          # GitHub Actions deployment workflow
├── themes/ananke/          # Hugo theme (git submodule)
├── hugo.toml               # Hugo configuration
└── serve.py                # Local preview server
```

---

## Local Development

Run a local preview server:

```bash
python serve.py
```

Then open `http://localhost:8000` in your browser.

---

## Making Changes

All portfolio content lives in **`docs/index.html`**. Edit it directly, then push to deploy.

```bash
git add docs/index.html
git commit -m "Your change description"
git push
```

GitHub Actions automatically deploys to GitHub Pages on every push to `master`.

---

## Deployment

Handled automatically via `.github/workflows/deploy.yml`. No manual steps needed — just push and the site updates within ~1 minute.

---

## Contact

- Email: [kampomah@crimson.ua.edu](mailto:kampomah@crimson.ua.edu)
- LinkedIn: [linkedin.com/in/kofi-ampomah](https://linkedin.com/in/kofi-ampomah)
- GitHub: [github.com/Ampomah-Kofi](https://github.com/Ampomah-Kofi)
