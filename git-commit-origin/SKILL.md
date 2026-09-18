---
name: git-commit-origin
description: When explicitly invoked, shows and confirms a commit-and-push plan for origin before executing it in the current repository, without running tests.
---

# Git Commit Origin

Explicit invocation of this skill starts the commit-and-push workflow in the current repository without running tests. It does not authorize mutations until the user confirms the plan.

1. Check for changes, identify the current branch, and confirm that the `origin` remote exists.
2. If there are no changes, report that and stop without creating an empty commit.
3. Before changing files or repository state, clearly state that you will run `git add .`, create a commit with a short, descriptive message, and run `git push origin HEAD`; include the branch and proposed commit message.
4. Ask for the user's explicit confirmation. Do not run `git add`, `git commit`, or `git push` until it is received.
5. After confirmation, run `git add .`, create the commit with the approved message, and run `git push origin HEAD`.
6. Report the short commit hash, branch, and push result.

Never use `--force`, `--force-with-lease`, `commit --amend`, rebase, reset, or any command that rewrites history. If the push is rejected, keep the local commit and report the cause without automatically pulling, merging, or rebasing.
