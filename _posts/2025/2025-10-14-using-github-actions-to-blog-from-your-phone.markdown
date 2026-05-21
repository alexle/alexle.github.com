---
layout: post
title: "Using GitHub Actions To Blog From Your Phone"
date: 2025-10-14 01:01:23
tags:
---

I haven't kept up with getting my thoughts onto this blog lately. In an effort to get more ideas out, I implemented a workflow which lets me create blog posts from any mobile device with a GitHub app.

No computer required.

## How it works

1. Create a GitHub issue from my phone with the blog post title and content
2. Add a `new-post` label to the issue
3. GitHub Actions automatically converts it to a properly formatted Jekyll post
4. The post is committed to the repository and the static site is rebuilt

That's it! The entire publishing workflow handled through the GitHub mobile app.

## Draft mode

For the times I need to start a draft without publishing, there's an alternative workflow:

1. Create a GitHub issue with the post content
2. Add a `draft` label — the post is saved to `_drafts/` but not published
3. When ready, add the `publish` label — the draft moves to `_posts/` and goes live

This gives a scratchpad for half-formed thoughts that I can revisit and finish later.

The workflows can be found in [create-post-from-issue.yml](https://github.com/alexle/alexle.github.com/blob/main/.github/workflows/create-post-from-issue.yml) and [draft-post-from-issue.yml](https://github.com/alexle/alexle.github.com/blob/main/.github/workflows/draft-post-from-issue.yml).

## Why I love this workflow

The beauty of this approach is in its simplicity. No need for special apps or services. It leverages tools I already use every day. And best of all it's on the same platform which this static site is hosted on. Chef's kiss.

Writing blog posts can now be as simple as writing an email or text message. And with draft mode, I can jot down ideas whenever inspiration strikes without the pressure of publishing right away.

Sometimes the best solutions aren't about adding complexity. But about reducing friction.

Have you automated any of your content workflow? I'd love to hear about it!

Note: This post was written on my iPhone 15 Pro
