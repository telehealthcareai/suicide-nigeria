# Contributing

Your contributions are valued and play a significant role in the continuous
improvement of **Suicide Analysis in Nigeria**. We welcome contributions of all
forms and acknowledge all efforts.

## How You Can Contribute

Contributions can be made in various ways, outlined below:

### Report Bugs

If you encounter a bug in **Suicide Analysis in Nigeria**, please report it via
our GitHub issues page at:
[https://github.com/osl-incubator/suicide-nigeria/issues](https://github.com/osl-incubator/suicide-nigeria/issues).

When reporting a bug, kindly include the following information to aid in the
issue's resolution:

- The name and version of your operating system.
- Any relevant details about your setup that might assist in diagnosing the
  issue.
- A step-by-step guide to reproduce the bug.

### Fix Bugs

You can contribute by fixing bugs identified in the GitHub issues. Issues tagged
with both "bug" and "help wanted" are available for anyone to work on.

### Implement Features

Feature development is another way to contribute. Review the GitHub issues for
requested features. Issues labeled with "enhancement" and "help wanted" are open
for implementation.

### Write Documentation

There's always a need for more documentation for **Suicide Analysis in
Nigeria**. This could be through enhancing the official documentation,
contributing to docstrings, or sharing knowledge via blog posts, articles, and
other media.

### Submit Feedback

Feedback is crucial for project improvement. To submit feedback or propose a
feature:

- File an issue at
  [https://github.com/osl-incubator/suicide-nigeria/issues](https://github.com/osl-incubator/suicide-nigeria/issues).
- For feature proposals, please provide a detailed explanation of how the
  feature would function, aim for a narrow scope to facilitate easier
  implementation, and remember, **Suicide Analysis in Nigeria** is a
  volunteer-driven project, and we welcome contributions.

## Requirements

Before you begin contributing to the Suicide Analysis in Nigeria project, there
are several technical prerequisites and best practices you should be familiar
with. This section outlines the key requirements to ensure a smooth and
productive contribution process.

### Conda Environment

Conda is a versatile tool that provides package, dependency, and environment
management for various programming languages. In the Suicide Analysis in Nigeria
project, we leverage Conda to manage virtual environments and package
dependencies effectively.

- **Environment Setup**: We strongly advise using a Conda environment while
  working with Suicide Analysis in Nigeria. If Conda is not installed on your
  system, you can download it from
  [Miniforge](https://github.com/conda-forge/miniforge). For an introductory
  overview of Conda, consider watching this
  [Conda Basics video](https://learning.anaconda.cloud/conda-basics).
- **Best Practices**: Avoid installing packages in the base Conda environment.
  Always create and activate a new environment for each project to prevent
  dependency conflicts and ensure a clean workspace.

### Git

Our collaborative efforts are facilitated through Git and GitHub. Understanding
the fundamentals of Git is crucial for effective participation.

- **Learning Resources**: If you're new to Git, we recommend starting with the
  [Software Carpentry Git Lesson](https://swcarpentry.github.io/git-novice/),
  which covers essential Git concepts and workflows.
- **Quick Reference**: For a concise summary of common Git commands, refer to
  this
  [Git Cheat Sheet](https://education.github.com/git-cheat-sheet-education.pdf)
  provided by GitHub.
- **Configuration Tips**:
  - To streamline your workflow, configure Git to use `rebase` by default for
    pulling changes with `git config --global pull.rebase true`.
  - Familiarize yourself with the `git rebase` command for updating branches
    from a remote repository. Although more complex, it is preferred over the
    default merge commit strategy. For an in-depth explanation, visit
    [Atlassian's guide on merging vs. rebasing](https://www.atlassian.com/git/tutorials/merging-vs-rebasing).
- **Workflow**: The standard open-source development workflow includes forking a
  repository, cloning the fork locally, and configuring an `upstream` remote for
  the original repository. Detailed instructions can be found in
  [GitHub's guide to configuring a remote for a fork](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/configuring-a-remote-repository-for-a-fork).

### Python

Familiarity with Python and adherence to best practices is important for
contributing to Suicide Analysis in Nigeria.

- **Style Guide**: Follow the PEP 8 style guide for Python code, available at
  [PEP8](https://peps.python.org/pep-0008/).
- **Best Practices**: pyOpenSci offers a comprehensive guide for writing Python
  packages, which can be found
  [here](https://www.pyopensci.org/python-package-guide/index.html).
- **Advanced Learning**: To deepen your understanding of Python and general
  programming concepts, consider enrolling in the
  [Design of Computer Programs](https://www.udacity.com/course/design-of-computer-programs--cs212)
  course on Udacity. Though challenging and based on Python 2, it provides
  valuable insights into advanced Python usage and computer programming
  principles.

### How to Get Support

Should you require assistance, please join our community on the Open Science
Labs Discord server at
[https://opensciencelabs.org/discord](https://opensciencelabs.org/discord).
Here, you can participate in the incubator program and ask questions about
Suicide Analysis in Nigeria in its dedicated channel. You are also welcome to
explore and join other groups that align with your interests.

## Setting Up for Local Development

To contribute to `suicide-nigeria`, follow these steps to set up your
development environment:

1. **Fork the Repository**: Begin by forking the `suicide-nigeria` repository on
   GitHub to your own account.

2. **Clone Your Fork Locally**: Clone the forked repository to your local
   machine and navigate into the project directory.

   ```bash
   $ git clone git@github.com:your_username/suicide-nigeria.git
   $ cd suicide-nigeria
   ```

3. **Install Dependencies**: Use `mamba` to create a Conda environment and
   `poetry` for managing Python dependencies.

   ```bash
   $ mamba env create --file conda/dev.yaml --yes
   $ conda activate suicide-nigeria
   $ poetry config virtualenvs.create false
   $ poetry install
   ```

4. **Create a Development Branch**: Make a dedicated branch for your bugfix or
   feature.

   ```bash
   $ git checkout -b name-of-your-bugfix-or-feature
   ```

5. **Make Changes Locally**: You are now ready to implement your changes or
   improvements.

6. **Install and Use Pre-commit Hooks**: `suicide-nigeria` utilizes `pre-commit`
   hooks to ensure code quality. Install them locally and they will
   automatically run on each commit.

   ```bash
   $ pre-commit install
   $ pre-commit run --all-files
   ```

   To bypass the hooks temporarily, use `git commit` with `--no-verify`.

7. **Commit and Push Changes**: Stage, commit, and push your changes to GitHub.
   After setting the upstream branch once, subsequent pushes only require
   `git push`.

   ```bash
   $ git add .
   $ git commit -m "Detailed description of your changes."
   $ git push --set-upstream origin <branch name>
   ```

8. **Submit a Pull Request**: Once your changes are pushed, go to the GitHub
   website to submit a pull request for review.
