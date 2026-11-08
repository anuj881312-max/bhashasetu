# Publish BhashaSetu on GitHub

GitHub publishing is intentionally a manual step so the repository stays under the maintainer's account.

## Option A: GitHub CLI

From this directory:

```bash
git init
git add .
git commit -m "Initial BhashaSetu MVP"
gh auth login
gh repo create bhashasetu --public --source . --remote origin --push
```

## Option B: GitHub website and Git

1. Create a new **public** repository named `bhashasetu` on GitHub. Do not add another README or license; this repository already contains both.
2. Run:

```bash
git init
git add .
git commit -m "Initial BhashaSetu MVP"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/bhashasetu.git
git push -u origin main
```

Replace `YOUR-USERNAME` with your GitHub username. Use GitHub authentication or a credential manager; never put a personal access token in the remote URL or a file.

## Before submitting an application

- Replace placeholder contacts in `SECURITY.md`, `CODE_OF_CONDUCT.md`, and `GRANT_PROPOSAL.md`.
- Add your real maintainer name, GitHub URL, and prior open-source links.
- Run `python -m pytest` and include the passing result in the application.
- Add a short demo GIF or terminal recording after testing the tool with synthetic data.
- Do not claim that OpenAI has approved or endorsed the project.
