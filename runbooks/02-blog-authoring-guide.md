# Runbook 02: Blog Authoring Guide

Detailed reference for formatting, frontmatter, images, code blocks, and FeelIt theme features.

---

## 1. Post Folder Formats: Page Bundle vs Single File

Hugo supports two ways to organize posts:

### Option A: Page Bundle (Recommended ⭐)
```
content/posts/my-new-article/
├── index.md        # Post content
├── cover.jpg       # Featured cover image
└── diagram.png     # In-post diagram
```
- **Why use this?** All assets belonging to the post stay inside that post's directory.
- **How to reference images in Markdown:**
  ```markdown
  ![Diagram](diagram.png)
  ```
- **How to create:**
  ```bash
  hugo new posts/my-new-article/index.md
  ```

### Option B: Single Markdown File
```
content/posts/
└── quick-note.md
```
- **Why use this?** For short, text-only notes without local images.
- **How to create:**
  ```bash
  hugo new posts/quick-note.md
  ```

---

## 2. Frontmatter Reference

Every post starts with YAML frontmatter enclosed in `---`:

```yaml
---
# Required / Core
title: "Mastering Distributed Systems"
subtitle: "A practical guide to consensus and replication"
date: 2026-09-20T21:00:00+07:00
draft: false                    # Set to false to publish, true to hide from production
author: "TruongTD"
description: "An in-depth article about distributed systems."

# Taxonomies
tags: ["Go", "Architecture", "Distributed Systems"]
categories: ["Engineering"]

# Images
featuredImage: "cover.jpg"      # Banner shown at top of the post
featuredImagePreview: ""        # Optional preview card thumbnail on home page

# Table of Contents
toc:
  enable: true                  # Set false to disable TOC for this post
  auto: true                    # Auto-collapse subheadings

# Code Block Options
code:
  copy: true                    # Enable copy button
  maxShownLines: 50             # Max lines before folding code block
---
```

---

## 3. Writing Content & FeelIt Features

### Summary Splitter (`<!--more-->`)
Place `<!--more-->` after your introductory paragraph. Everything before it will be used as the preview excerpt on the homepage and archive lists:
```markdown
This paragraph is the preview excerpt shown on the homepage.

<!--more-->

This content is only visible when the reader clicks into the full article.
```

---

### Code Blocks with Syntax Highlighting

FeelIt highlights code with line numbers and a copy button:

````markdown
```go
package main

import "fmt"

func main() {
    fmt.Println("Clean syntax highlighting")
}
```
````

Common language identifiers: `go`, `python`, `javascript`, `typescript`, `bash`, `yaml`, `json`, `sql`, `dockerfile`.

---

### Callouts / Admonitions

The FeelIt theme includes custom admonition shortcodes (`note`, `abstract`, `info`, `tip`, `success`, `question`, `warning`, `failure`, `danger`, `bug`, `example`, `quote`):

```markdown
{{< admonition tip "Pro Tip" >}}
You can use `hugo server -D` to preview draft posts in real time.
{{< /admonition >}}

{{< admonition warning "Watch Out" >}}
Do not forget to switch `draft: false` before deploying!
{{< /admonition >}}
```

---

### Mathematical Formulas ($KaTeX$)

Inline math:
```markdown
Euler's identity is $e^{i\pi} + 1 = 0$.
```

Block math:
```markdown
$$
\int_{-\infty}^{\infty} e^{-x^2} dx = \sqrt{\pi}
$$
```

---

### Embedding Images

- **From Page Bundle**:
  ```markdown
  ![Architecture](architecture.png)
  ```
- **From Global `static/images/`**:
  If you save an image in `static/images/diagram.png`:
  ```markdown
  ![Diagram](/blogs/images/diagram.png)
  ```

---

### Font Awesome Icons

FeelIt supports Font Awesome icons directly:

```markdown
{{< icon "fa-solid fa-rocket" >}} Ready for takeoff!
```
