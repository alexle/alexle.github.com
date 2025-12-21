---
layout: post
title: My Neovim Keybindings
date: 2025-12-21
tags: programming
---

I switched from Vim to [Neovim][1] a few years ago and haven't looked back. The Lua configuration, better defaults, and plugin ecosystem make it a joy to use.

My config is split across multiple files in `~/.config/nvim/lua/`. Here are the keybindings I use daily.

## General

| Keybinding | Description |
| --- | --- |
| `Space` | Leader key |
| `jj` | Exit insert mode (instead of Esc) |
| `<leader>w` | Save all files |
| `<leader>q` | Quit all |
| `<leader>wq` | Save and quit all |
| `Ctrl+a` | Select all text in file |
| `<leader>;` | Copy text inside double quotes |

## Window Navigation

| Keybinding | Description |
| --- | --- |
| `Ctrl+h` | Move to left window |
| `Ctrl+l` | Move to right window |
| `<leader>v` | Vertical split |
| `<leader>x` | Close window |
| `Ctrl+b` | Jump to previous window |
| `Alt+w` | Go to previous location (jump list) |

## Tabs

| Keybinding | Description |
| --- | --- |
| `Tab` | Next tab |

## File Explorer & Search (Snacks.nvim)

| Keybinding | Description |
| --- | --- |
| `Ctrl+n` | Toggle Neo-tree file explorer |
| `<leader><space>` | Smart find files |
| `<leader>,` | List open buffers |
| `Alt+f` | Grep search in project |

## LSP Navigation

| Keybinding | Description |
| --- | --- |
| `Alt+d` | Go to definition |
| `gD` | Go to declaration |
| `Alt+r` | Find references |
| `gI` | Go to implementation |
| `gy` | Go to type definition |
| `<leader>l` | List LSP symbols |
| `<leader>sS` | List workspace symbols |
| `<leader>ff` | Format file |
| `]]` | Jump to next reference |
| `[[` | Jump to previous reference |

## Git (Snacks.nvim + Lazygit)

| Keybinding | Description |
| --- | --- |
| `<leader>gg` | Open Lazygit |
| `<leader>gb` | Git branches |
| `<leader>gl` | Git log |
| `<leader>gL` | Git log for current line |
| `<leader>gs` | Git status |
| `<leader>gS` | Git stash |
| `<leader>gd` | Git diff (hunks) |
| `<leader>gf` | Git log for current file |
| `<leader>gm` | Git blame line |

## Copilot Chat

| Keybinding | Description |
| --- | --- |
| `<leader><Tab>` | Open Copilot Chat prompt |
| `Alt+c` | Toggle Copilot Chat |
| `<leader>ce` | Explain selected code |
| `<leader>cf` | Fix selected code |
| `<leader>co` | Optimize selected code |

## Terminal

| Keybinding | Description |
| --- | --- |
| `Ctrl+/` | Toggle terminal |
| `Ctrl+t` | Exit terminal mode |
| `Esc` | Close floating windows |

## Why These Bindings?

A few notes on my choices:

**Space as leader** - Easy to hit with either thumb. Most of my common actions flow from here.

**jj to escape** - A classic. Your fingers rarely need to leave home row.

**Alt key combos** - I use Alt for frequent LSP actions (definition, references, grep). I got used to using them in VSCode. Plus they're slightly faster than leader combos.

**Snacks.nvim** - Replaced Telescope. The picker is fast and the git integration is solid.

You can find my full config on [GitHub][2].

NOTE: Of course, my main IDE is still VSCode. But Neovim is my go-to for quick edits and terminal work!

[1]: https://neovim.io/
[2]: https://github.com/alexle/neovim-config
