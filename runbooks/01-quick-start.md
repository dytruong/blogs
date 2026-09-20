# Runbook 01: Quick Start Guide

A 5-minute walkthrough to write, preview, and publish your first blog post.

---

## 1. Start the Local Development Server

Run this command in the project root:

```bash
hugo server -D
```

- `-D` includes draft posts so you can see your unfinished work.
- Open your browser at: **[http://localhost:1313/blogs/](http://localhost:1313/blogs/)**
- The server supports **hot reload** — any edits you save in your editor will immediately update in your browser.

---

## 2. Create a New Blog Post

Generate a new post using Hugo's archetype template:

```bash
hugo new posts/hello-world/index.md
```

> [!TIP]
> Using `posts/<post-name>/index.md` creates a **Page Bundle**. This is the recommended structure because you can store any images or assets for the post in the exact same folder!

---

## 3. Write Your Content

Open `content/posts/hello-world/index.md` in your editor.

1. Adjust the **frontmatter** metadata at the top:
   ```yaml
   ---
   title: "Hello World"
   date: 2026-09-20T21:00:00+07:00
   draft: false # <-- Change to false when ready to publish!
   tags: ["General"]
   categories: ["Updates"]
   ---
   ```

2. Add your content below the `---` separator:
   ```markdown
   This is my first blog post!

   <!--more-->

   Everything above the divider appears in post previews on the home page.
   Everything below is the full article content.
   ```

---

## 4. Publish Your Post to GitHub Pages

Once you're happy with your preview:

1. Ensure `draft: false` is set in the frontmatter.
2. Commit and push to `main`:
   ```bash
   git add .
   git commit -m "feat: add hello-world post"
   git push origin main
   ```
3. GitHub Actions will automatically build and publish your post to:
   **https://dytruong.github.io/blogs/**
