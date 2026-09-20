# Personal Tech Blog

Clean, fast, and responsive personal blog built with [Hugo Extended](https://gohugo.io/) and the [FeelIt](https://github.com/khusika/FeelIt) theme. Automatically deployed to GitHub Pages via GitHub Actions.

🌐 **Live Site**: [https://dytruong.github.io/blogs/](https://dytruong.github.io/blogs/)

---

## 📚 Runbooks & Guides

We have prepared step-by-step runbooks in the [`runbooks/`](runbooks/) directory:

- 🚀 [**Runbook 01: Quick Start**](runbooks/01-quick-start.md) — 5-minute guide to write, preview, and deploy your first post.
- ✍️ [**Runbook 02: Blog Authoring Guide**](runbooks/02-blog-authoring-guide.md) — Comprehensive reference for frontmatter, markdown, code highlighting, admonition callouts, math formulas, and images.
- ⚙️ [**Runbook 03: Deployment & FAQ**](runbooks/03-deployment-and-faq.md) — GitHub Pages auto-deploy setup, submodule handling, and troubleshooting tips.

---

## ⚡ Quick Cheatsheet

```bash
# 1. Preview site locally with drafts enabled (live reloading)
hugo server -D

# 2. Create a new blog post
hugo new posts/my-post-title/index.md

# 3. Publish to GitHub Pages
git add .
git commit -m "feat: add my new post"
git push origin main
```

---

## 📁 Repository Structure

```
blogs/
├── .github/
│   └── workflows/
│       └── deploy.yml              # CI/CD: Auto-deploy to GitHub Pages
├── archetypes/
│   └── default.md                  # New post template used by 'hugo new'
├── assets/                         # Custom styles and scripts (optional)
├── content/
│   ├── posts/                      # Your blog articles
│   │   ├── _index.md               # Posts archive page settings
│   │   └── my-first-post/          # Post bundle folder
│   │       └── index.md            # Post Markdown file
│   └── about/
│       └── index.md                # About Me page
├── layouts/                        # Custom layout overrides (optional)
├── runbooks/                       # Step-by-step guides for authoring & deployment
│   ├── 01-quick-start.md
│   ├── 02-blog-authoring-guide.md
│   └── 03-deployment-and-faq.md
├── static/                         # Static files served directly at site root
│   └── images/                     # Global images and assets
├── themes/
│   └── FeelIt/                     # FeelIt theme git submodule
├── hugo.toml                       # Site configuration file
├── .gitignore                      # Git ignore rules
└── README.md                       # Project overview & documentation
```
