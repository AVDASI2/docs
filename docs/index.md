# AVDASI 2 docs

Welcome to the offical documentation for the University of Bristol's Aerospace Vehicular Design and Systems Integration 2 course.


This site contains general documentation for the [AVDASI 2](https://github.com/AVDASI2) course.

It's hosted on the [AVDASI 2 GitHub org](https://github.com/AVDASI2), and uses [MkDocs](https://www.mkdocs.org) auto-compiled via a GitHub Action. Code from the [AVDASI 2 Example_Code repo](https://github.com/AVDASI2/Example_Code) is also auto-synced to the docs using GitHub Action so code snippets can be displayed and will update after every new push. AVDASI 2 members can push changes to the docs which will be approved by an owner and published. If you want to trial stuff locally first just clone the repo and do:

```bash
pip install mkdocs-material mkdocs-implicit-index
mkdocs serve
```

Then open [http://127.0.0.1:8000](http://127.0.0.1:8000).

## Navigation structure

This MkDocs is configured to use [mkdocs-literate-nav](https://oprypin.github.io/mkdocs-literate-nav/) to pull nav and page ordering from a list in _index.md_ within each folder, like this:

- [Avionics](Avionics/)
- [Aerodynamics](Aerodynamics/)
- [Structures](Structures/)
