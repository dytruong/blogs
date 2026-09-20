---
title: "My First Blog Post"
subtitle: "Welcome to my Hugo blog powered by FeelIt"
date: 2026-09-20T21:00:00+07:00
draft: false
author: "TruongTD"
description: "A quick introduction to my new blog and writing workflow."
tags: ["Welcome", "Hugo", "Guide"]
categories: ["General"]
featuredImage: ""
toc:
  enable: true
  auto: true
code:
  copy: true
  maxShownLines: 50
---

Hello world! This is my first blog post written in Markdown and rendered using Hugo and the FeelIt theme.

<!--more-->

## Writing in Markdown

Hugo allows you to write articles cleanly using standard Markdown. Here is what you can do:

### Code Snippets

```go
package main

import "fmt"

func main() {
    fmt.Println("Hello from Hugo!")
}
```

### Callouts / Admonitions

{{< admonition tip "Quick Tip" >}}
You can see all available writing guides in the `runbooks/` folder of this repository.
{{< /admonition >}}

### Mathematics Support

Inline formula: $f(x) = ax^2 + bx + c$

Block formula:
$$
\sum_{k=1}^{n} k = \frac{n(n+1)}{2}
$$

## Next Steps

To add more articles, run:

```bash
hugo new posts/your-title/index.md
```

Check out [`runbooks/01-quick-start.md`](https://github.com/dytruong/blogs/blob/main/runbooks/01-quick-start.md) for full instructions!
