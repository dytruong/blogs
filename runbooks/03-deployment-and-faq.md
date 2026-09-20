# Runbook 03: Deployment & FAQ

Guide to GitHub Actions CI/CD automation, GitHub Pages settings, and common troubleshooting tips.

---

## 1. How Deployment Works

Every time code is pushed to the `main` branch of this repository, a GitHub Actions workflow defined in [`.github/workflows/deploy.yml`](../.github/workflows/deploy.yml) runs automatically:

1. **Checks out the repository**: Pulls the code and initializes the `themes/FeelIt` Git submodule recursively.
2. **Installs Hugo Extended**: Configures the latest version of Hugo with Sass/SCSS compilation support.
3. **Builds the site**: Executes `hugo --gc --minify` to produce optimized HTML, CSS, JS, and search indexes.
4. **Deploys to GitHub Pages**: Pushes the artifact to GitHub Pages with zero manual intervention.

---

## 2. One-Time Setup on GitHub

If this is your first deployment on GitHub:

1. Open your repository on GitHub: **https://github.com/dytruong/blogs**
2. Click on **Settings** (top navigation bar).
3. In the left sidebar, click on **Pages**.
4. Under **Build and deployment**:
   - **Source**: Change from "Deploy from a branch" to **GitHub Actions**.
5. Push a commit or trigger the workflow manually under **Actions** > **Deploy Hugo site to Pages** > **Run workflow**.

---

## 3. Cloning on a New Machine

Because the FeelIt theme is stored as a Git submodule, clone with `--recurse-submodules`:

```bash
git clone --recurse-submodules https://github.com/dytruong/blogs.git
```

If you already cloned without the flag:
```bash
git submodule update --init --recursive
```

---

## 4. FAQ & Troubleshooting

### Why is my post visible locally but missing on GitHub Pages?
Check the post's frontmatter:
1. `draft: true` — posts marked as draft are excluded from production builds. Change to `draft: false`.
2. `date: ...` — if the post date is in the future, Hugo excludes it by default unless configured otherwise.

### Why do images or styles look broken?
Check `baseURL` in `hugo.toml`. For GitHub project pages, it must end with the repository name and a trailing slash:
```toml
baseURL = "https://dytruong.github.io/blogs/"
```

### Port 1313 is already in use locally?
Run Hugo on another port:
```bash
hugo server -D -p 1314
```

### How do I customize site navigation or author details?
Edit `hugo.toml`:
- Update `[params.author]` for your name and links.
- Update `[languages.en.menu]` to add or rename navbar links.
- Update `[languages.en.params.home.profile]` to customize your avatar and bio.
