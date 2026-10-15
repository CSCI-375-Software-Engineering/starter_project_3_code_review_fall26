# Code Review Summary Report

**Name:** Rami Osman
**Project:** Starter Project 3 – Code Review (Boggle Solver)

## 1. Overview

The assignment was to run a real peer code review workflow on my Boggle solver: push my original solution on its own branch, open a pull request, review a partner's solver, apply my partner's feedback, run a formatter and linter, regression test, and write this report.

My solver is a Python `Boggle` class with `setGrid`, `setDictionary`, and `getSolution`. It uses depth-first search from every tile, and a precomputed set of word prefixes so any path that cannot become a dictionary word stops early. Multi-letter tiles (`Qu`, `St`, `Ie`) work because each tile's full text is appended to the current path. Words must be at least 3 letters, a tile cannot be reused within one word, and invalid input (bad grid or dictionary) returns an empty list. My original version is saved as `boggle_solver.py.orig`, and the improved version is `boggle_solver.py`.

## 2. Feedback I Received

My partner, Jared, left three inline comments and an overall summary on my pull request.

- **Prefix set (`_build_prefixes`):** He liked that the prefix set stops the DFS from following paths that cannot form a dictionary word, which makes the search more efficient.
- **`used` set (`_search`):** He liked that tiles are added before recursion and removed afterward, which keeps each DFS path separate and prevents tile reuse.
- **Suggestion (`getSolution`):** He suggested normalizing the dictionary to lowercase once, when it is set, instead of converting words to lowercase every time `getSolution()` runs, to avoid repeated work.
- **Overall:** He found the code organized and easy to follow, said the DFS correctly checks neighbors and prevents tile reuse, and liked that invalid input is handled before the search starts. His only suggestion was the lowercase normalization.

## 3. Feedback I Gave

I reviewed Jared's solver using the "we" and question style from the assignment, and included praise.

- **Praise:** `word.startswith(tile, position)` handles `Qu`, `St`, and `Ie` without special cases; the input validation is thorough; and the docstrings make the file easy to follow.
- **Correctness:** I asked him to double-check that `__init__` and `"__main__"` use double underscores, since without them the constructor and `main()` would not run, and to rename `solutions` to `solution` to match the assignment's data member.
- **Efficiency:** Each dictionary word was searched from every tile with no early stopping. I suggested a prefix set so a path can stop as soon as it is not a prefix of any word, and a set instead of a list for duplicate checks.
- **Readability and style:** I suggested `snake_case` names with leading underscores for helper methods, a `DIRECTIONS` list instead of nested loops with a `continue`, a named constant instead of the magic number 3, a single cleanup point instead of a duplicated `used.remove(...)`, and a docstring on `main()`.

## 4. Improvements I Implemented

I applied Jared's suggestion. The dictionary is now a property: whenever it is set (in the constructor or by `setDictionary`), it is validated and lowercased once, and the word set and prefix set are built at that moment. `getSolution()` no longer lowercases words or rebuilds those sets on each call, and results still keep the caller's original spelling and the dictionary's order.

A side effect of this change is that `_search` reads the word and prefix sets from `self`, so its parameter list dropped from seven to five, which is easier to read. I did not change anything else, because Jared had no other requests and I wanted the refactor to stay focused. I also verified the new version returns the same results as the original on 3,000 randomly generated boards and dictionaries.

## 5. Static Analysis Results

Prettier is a JavaScript formatter and does not format Python, so I used the Python equivalents:

- **Formatter:** `autopep8` (run with `--in-place`) reformats the file to PEP 8. It made no changes.
- **Linter:** `pycodestyle` checks PEP 8. It reported zero issues on the final `boggle_solver.py`.

The file already used consistent four-space indentation, lines under 80 characters, two blank lines between top-level definitions, and docstrings throughout, so there was nothing to fix. The Codio final check also passed.

## 6. Regression Testing

I verified correctness after the changes in three ways:

1. My 25-test `unittest` suite, generated with the Category Partition Method, covers invalid input, grid sizes, adjacency and tile reuse, word rules, and the `Qu`/`St`/`Ie` tiles. All 25 pass on the refactored solver.
2. The examples from the assignment still produce the expected output, including `['ABEF', 'AFJIEB', 'DGKD']`.
3. The Codio auto-grader (Boggle Assignment #3) passed on the final code.

## 7. Reflection

This project showed me how useful a second set of eyes is, even when the feedback is small. Jared's suggestion was minor, but acting on it made the code cleaner and the search setup happen once instead of on every call. Writing my own review made me read code more carefully and phrase suggestions as questions with "we", which made feedback feel collaborative. I also learned that the process matters as much as the code: branches, pull requests, re-requesting review, and keeping the original as `.orig` leave a clear record of what changed and why. Running a formatter and linter is quick, and it removes style arguments from reviews so people can focus on correctness and design. Setting up repository access took longer than expected, and I would ask for access earlier next time.