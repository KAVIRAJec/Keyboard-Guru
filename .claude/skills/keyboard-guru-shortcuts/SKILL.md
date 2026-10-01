---
name: keyboard-guru-shortcuts
description: Add, update, or look up keyboard shortcuts in the Keyboard-guru reference repo, following its exact folder/table/update-log conventions. Use this whenever the user wants to record a new shortcut, document a new app/tool's shortcuts, reorganize an existing shortcuts.md file, or asks "where do shortcuts for X go" in this repo — even if they just paste a shortcut and say "add this" without mentioning the skill by name.
---

# Keyboard Guru Shortcuts

This repo (`Keyboard-guru`) is Kaviraj's personal, tool-by-tool keyboard shortcut reference. Every change must keep the repo internally consistent: the right folder, the right table format, and a matching Update Log entry. Read `CLAUDE.md` at the repo root first if it's not already in context — it's the source of truth for structure and conventions, and this skill should stay consistent with it (if they ever diverge, `CLAUDE.md` wins).

## Repo layout

```
Keyboard-guru/
├── general/           # OS-level / universal (macOS) shortcuts
├── vs-code/           # VS Code editor shortcuts
├── powerlevel10k-git/ # Oh My Zsh git plugin aliases + Powerlevel10k
└── arc-browser/       # Arc browser shortcuts
```

Each folder holds one or more `.md` files (usually just `shortcuts.md`) grouping shortcuts for that tool.

## Adding a shortcut to an existing tool

1. Find that tool's folder and its `shortcuts.md` (or other `.md` file grouping the relevant shortcuts).
2. Append a row to the existing table rather than creating a new table, unless the file is organized into H2 sections (see below).
3. Match the table format already used in that file:
   - Most files: a single table with header `| Shortcut | Action |`.
   - `powerlevel10k-git/shortcuts.md` is organized differently — it's grouped into H2 sections (`## Add`, `## Commit`, `## Push`, etc.) separated by `---` horizontal rules, each with its own `| Alias | Command |` table. If adding a git alias, put it in the matching section (create a new `## Section` + `---` + table if no section fits) rather than appending to an unrelated one.
4. Keep rows sorted the way the surrounding rows already are (most files aren't strictly alphabetical — just don't break an existing order if there is one).
5. Use the same symbol conventions already present in the file (e.g. ⌘ ⌃ ⌥ ⇧ for Mac modifiers, backtick-quoted CLI aliases for the git file).

## Adding a brand-new tool/app

If the shortcut is for a tool that doesn't have a folder yet:

1. Create `new-tool-name/shortcuts.md` (kebab-case folder name, matching the existing `arc-browser`, `vs-code` style).
2. Start the file with an H1 title and a one-line description of context, e.g.:
   ```markdown
   # <Tool> Shortcuts

   Keyboard shortcuts for <Tool>.

   | Shortcut | Action |
   |----------|--------|
   | ... | ... |
   ```
3. Register the new folder in **both**:
   - `CLAUDE.md` — add it to the `Structure` code block.
   - `readme.md` — add a row to the `## Structure` table, linking to the new file, e.g. `| [\`new-tool-name/\`](new-tool-name/shortcuts.md) | <Tool> shortcuts |`.

## Always update the Update Log

Every change that adds/modifies shortcuts or repo structure must get a new row in the `## Update Log` table at the bottom of `CLAUDE.md`. Append (don't rewrite history):

```markdown
| YYYY-MM-DD | <short description of the change> |
```

Use today's actual date and a description in the same terse past-tense style as existing entries (e.g. "Added Mac app window switching shortcuts to general/shortcuts.md").

## Quick checklist before finishing

- [ ] Shortcut added to the correct file, matching its existing table/section format
- [ ] New folder (if any) also added to `CLAUDE.md` Structure and `readme.md` Structure table
- [ ] `CLAUDE.md` Update Log has a new dated row describing the change
- [ ] No unrelated formatting changes to surrounding rows
