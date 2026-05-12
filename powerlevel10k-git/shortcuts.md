# Powerlevel10k & Git Aliases

Oh My Zsh git plugin aliases commonly used with Powerlevel10k.

---

## Add

| Alias | Command |
|-------|---------|
| `g` | `git` |
| `ga` | `git add` |
| `gaa` | `git add --all` |
| `gapa` | `git add --patch` |
| `gau` | `git add --update` |
| `gav` | `git add --verbose` |

---

## Branch

| Alias | Command |
|-------|---------|
| `gb` | `git branch` |
| `gba` | `git branch -a` |
| `gbd` | `git branch -d` |
| `gbD` | `git branch -D` |
| `gbnm` | `git branch --no-merged` |
| `gbr` | `git branch --remote` |
| `gbs` | `git bisect` |
| `gbsb` | `git bisect bad` |
| `gbsg` | `git bisect good` |
| `gbsr` | `git bisect reset` |
| `gbss` | `git bisect start` |

---

## Commit

| Alias | Command |
|-------|---------|
| `gc` | `git commit -v` |
| `gc!` | `git commit -v --amend` |
| `gcn!` | `git commit -v --no-edit --amend` |
| `gca` | `git commit -v -a` |
| `gca!` | `git commit -v -a --amend` |
| `gcam` | `git commit -a -m` |
| `gcmsg` | `git commit -m` |
| `gcsm` | `git commit -s -m` |
| `gcs` | `git commit -S` |

---

## Checkout / Switch

| Alias | Command |
|-------|---------|
| `gco` | `git checkout` |
| `gcb` | `git checkout -b` |
| `gcm` | `git checkout main` |
| `gcd` | `git checkout develop` |
| `gcor` | `git checkout --recurse-submodules` |
| `gsw` | `git switch` |
| `gswc` | `git switch -c` |
| `gswm` | `git switch main` |
| `gswd` | `git switch develop` |

---

## Clone / Config

| Alias | Command |
|-------|---------|
| `gcl` | `git clone --recurse-submodules` |
| `gcf` | `git config --list` |
| `gcount` | `git shortlog -sn` |

---

## Cherry-pick

| Alias | Command |
|-------|---------|
| `gcp` | `git cherry-pick` |
| `gcpa` | `git cherry-pick --abort` |
| `gcpc` | `git cherry-pick --continue` |

---

## Diff

| Alias | Command |
|-------|---------|
| `gd` | `git diff` |
| `gdca` | `git diff --cached` |
| `gdcw` | `git diff --cached --word-diff` |
| `gds` | `git diff --staged` |
| `gdw` | `git diff --word-diff` |
| `gdt` | `git diff-tree --no-commit-id --name-only -r` |

---

## Fetch

| Alias | Command |
|-------|---------|
| `gf` | `git fetch` |
| `gfa` | `git fetch --all --prune` |
| `gfo` | `git fetch origin` |

---

## Log

| Alias | Command |
|-------|---------|
| `gl` | `git pull` |
| `glg` | `git log --stat` |
| `glgp` | `git log --stat -p` |
| `glgg` | `git log --graph` |
| `glgga` | `git log --graph --decorate --all` |
| `glgm` | `git log --graph --max-count=10` |
| `glo` | `git log --oneline --decorate` |
| `glog` | `git log --oneline --decorate --graph` |
| `gloga` | `git log --oneline --decorate --graph --all` |
| `glol` | `git log --graph --pretty (with colors)` |
| `glola` | `git log --graph --pretty --all` |
| `glods` | `git log --graph --pretty --date=short` |

---

## Merge

| Alias | Command |
|-------|---------|
| `gm` | `git merge` |
| `gma` | `git merge --abort` |
| `gmom` | `git merge origin/main` |
| `gmum` | `git merge upstream/main` |
| `gmt` | `git mergetool --no-prompt` |

---

## Push

| Alias | Command |
|-------|---------|
| `gp` | `git push` |
| `gpd` | `git push --dry-run` |
| `gpf` | `git push --force-with-lease` |
| `gpf!` | `git push --force` |
| `gpv` | `git push -v` |
| `gpoat` | `git push origin --all && git push origin --tags` |
| `gpsup` | `git push --set-upstream origin <current-branch>` |
| `ggp` | `git push origin <current-branch>` |
| `ggpush` | `git push origin <current-branch>` |
| `ggfl` | `git push --force-with-lease origin <current-branch>` |

---

## Pull

| Alias | Command |
|-------|---------|
| `ggl` | `git pull origin <current-branch>` |
| `ggpull` | `git pull origin <current-branch>` |
| `gpr` | `git pull --rebase` |
| `gup` | `git pull --rebase` |
| `gupv` | `git pull --rebase -v` |
| `gupa` | `git pull --rebase --autostash` |
| `gupav` | `git pull --rebase --autostash -v` |
| `ggu` | `git pull --rebase origin <current-branch>` |
| `glum` | `git pull upstream main` |

---

## Rebase

| Alias | Command |
|-------|---------|
| `grb` | `git rebase` |
| `grba` | `git rebase --abort` |
| `grbc` | `git rebase --continue` |
| `grbd` | `git rebase develop` |
| `grbi` | `git rebase -i` |
| `grbm` | `git rebase main` |
| `grbo` | `git rebase --onto` |
| `grbs` | `git rebase --skip` |

---

## Remote

| Alias | Command |
|-------|---------|
| `gr` | `git remote` |
| `gra` | `git remote add` |
| `grv` | `git remote -v` |
| `grmv` | `git remote rename` |
| `grrm` | `git remote remove` |
| `grset` | `git remote set-url` |
| `grup` | `git remote update` |
| `ggsup` | `git branch --set-upstream-to=origin/<current-branch>` |

---

## Reset / Restore / Revert

| Alias | Command |
|-------|---------|
| `grh` | `git reset HEAD` |
| `grhh` | `git reset HEAD --hard` |
| `gru` | `git reset --` |
| `grev` | `git revert` |
| `grs` | `git restore` |
| `grss` | `git restore --source` |
| `grst` | `git restore --staged` |
| `gpristine` | `git reset --hard && git clean -dffx` |

---

## Remove / Move

| Alias | Command |
|-------|---------|
| `grm` | `git rm` |
| `grmc` | `git rm --cached` |

---

## Stash

| Alias | Command |
|-------|---------|
| `gsta` | `git stash push` |
| `gstaa` | `git stash apply` |
| `gstc` | `git stash clear` |
| `gstd` | `git stash drop` |
| `gstl` | `git stash list` |
| `gstp` | `git stash pop` |
| `gsts` | `git stash show --text` |
| `gstu` | `git stash --include-untracked` |
| `gstall` | `git stash --all` |

---

## Status

| Alias | Command |
|-------|---------|
| `gst` | `git status` |
| `gss` | `git status -s` |
| `gsb` | `git status -sb` |

---

## Show

| Alias | Command |
|-------|---------|
| `gsh` | `git show` |
| `gsps` | `git show --pretty=short --show-signature` |
| `gwch` | `git whatchanged -p --abbrev-commit --pretty=medium` |

---

## Submodule

| Alias | Command |
|-------|---------|
| `gsi` | `git submodule init` |
| `gsu` | `git submodule update` |

---

## Tags

| Alias | Command |
|-------|---------|
| `gts` | `git tag -s` |
| `gtv` | `git tag \| sort -V` |

---

## Misc / Utility

| Alias | Command |
|-------|---------|
| `gclean` | `git clean -id` |
| `gbl` | `git blame -b -w` |
| `gignore` | `git update-index --assume-unchanged` |
| `gunignore` | `git update-index --no-assume-unchanged` |
| `gignored` | `git ls-files -v \| grep "^[[:lower:]]"` |
| `gfg` | `git ls-files \| grep` |
| `grt` | `cd to git root directory` |
| `gwip` | `commit WIP (add all + commit --no-verify)` |
| `gunwip` | `undo last WIP commit` |
| `gk` | `gitk --all --branches` |
