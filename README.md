# Git Repo Migrator

*Git Repo Migrator* is a Python tool designed to simplify the process of migrating existing, locally saved git repositories from one server to another. It eliminates the hassle of manually removing old remote repositories and adding new ones by automating the entire process.

## Background
I originally hosted my self-managed git repositories on [Gitea](https://github.com/go-gitea/gitea) but decided to migrate to [Soft Serve](https://github.com/charmbracelet/soft-serve) for its intuitive terminal user interface (TUI). Moving my repositories manually was tedious and error-prone, so I developed this program to streamline the migration process. This project was not only practical but also a fun way to practice my Python skills.

## Features
- Automatically removes the existing remote repository.
- Adds a new remote repository to your locally saved git repositories.
- Assumes:
  - The current remote is named `origin`.
  - The default branch is `main`.

## Requirements
- [Python 3.12.7](https://www.python.org/)
- [Git](https://git-scm.com/) installed and available in your system's PATH.
- Your repositories must already exist locally, preferably in a single directory.

## Installation
1. Clone the repository:
```bash
   git clone https://github.com/xjwllmsx/git-repo-migrator.git
   cd git-repo-migrator
```

## Usage
1. Make sure your existing repositories are locally stored.
2. Run the program:
```bash
python git-repo-migrator.py
```
3. Follow the prompts to complete the migration.

## Limitations
* Assumes the remote repository name is `origin` and the main branch is `main`.
* Only supports repositories already cloned locally.
* Does not validate authentication for the new server (make sure your SSH keys or credentials are set up beforehand).

## Contributing
Contributions are welcome! Feel free to submit issues or pull requests on the [GitHub repository](https://github.com/xjwllmsx/git-repo-migrator).

## License
This project is licensed under the MIT License. See the [LICENSE](https://github.com/xjwllmsx/git_repo_migrator/blob/main/LICENSE.md) file for details.

## Acknowledgments
Thanks to the Soft Serve team for creating a fantastic TUI-based git server.
