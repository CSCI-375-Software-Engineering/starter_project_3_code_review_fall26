Here's the full report as plain text — paste it into Google Docs or Word.

---

# Code Review Summary — Project 3

**Chase Medy** · CSCI 375 Software Engineering · October 7, 2026

## Overview

Project 3 paired each student with a classmate to review a Boggle solver written in Python. The solver takes a grid of letter tiles and a dictionary, and returns every dictionary word that can be formed by walking through adjacent tiles with 8-way adjacency and no tile reuse. Qu, St, and Ie are treated as single tiles that each count for two letters, and words shorter than three characters are ignored. My implementation builds a trie from the dictionary once, then runs a depth-first search from every grid cell, pruning any path whose prefix is not in the trie. A visited set handles backtracking across the 8 neighbors.

## Feedback You Received

My partner called out five issues on the first draft:

1. Internal names did not follow PEP 8. Methods and local variables used camelCase instead of snake_case.
2. Magic values were scattered through the code. The string sentinel for word endings, the minimum word length of three, and the eight direction offsets all appeared inline.
3. Tile validation was too loose. The existing check accepted any alphabetic string, so a cell like "Hello" would pass.
4. The nested helpers inside `getSolution` made the method long and hard to test. They belonged as private methods on the class.
5. The trie was being rebuilt on every call to `getSolution`. It should be built once when the dictionary is set.

The backtracking, docstrings, and overall trie plus DFS structure were called out as working well.

## Feedback You Gave

I left four inline comments on my partner's solver and one summary comment covering the full rubric:

1. Magic number extraction. The minimum word length and the grid dimension bounds were hardcoded in several places. Pulling them into named constants would make the intent obvious and the file easier to retune.
2. PEP 8 method naming. Several internal methods used camelCase where the external contract did not require it. Converting them to snake_case would match standard Python style.
3. A clarifying comment on lone-Q rejection. The code silently skipped bare Q tiles under the assumption Q always travels with U, but the logic was not obvious from reading the method. A single line of explanation would prevent a future maintainer from undoing the behavior.
4. Missing class docstring. The solver class had no top-level description of what it does or how to use it.

The summary comment hit all four rubric areas (correctness and edge cases, algorithm efficiency, readability and naming, code style and maintainability) at a level the reviewer could triage, without duplicating the inline comments.

## Improvements You Implemented

I addressed every point in the received feedback:

1. Constants pulled to module level: `MIN_WORD_LENGTH`, `WORD_END`, `MULTI_CHAR_TILES`, `VALID_TILES`, and `DIRECTIONS`. The direction tuple replaced the nested loop over `(-1, 0, 1)` ranges inside the neighbor helper.
2. Tile validation tightened with a `VALID_TILES` allowlist covering a-z plus the three multi-character tiles. Any other string now fails `_is_valid_input` rather than silently passing.
3. Trie construction moved into `_build_trie`, called from `__init__` and from `setDictionary`. The trie is now cached on the instance as `self._trie` instead of being rebuilt on every solve. Both setters also clear `self.solution` so a stale cached result cannot be returned after the inputs change.
4. Three private methods extracted from `getSolution`: `_step_through`, `_neighbors`, and `_search`. The public method now reads top to bottom in under 20 lines and the recursive walk can be tested in isolation.
5. Internal helpers and locals renamed to snake_case (`next_node`, `grown_path`, `_is_valid_input`). The three public methods `getSolution`, `setGrid`, and `setDictionary` stayed in camelCase to match the external contract the grader uses.

I also added a `main()` smoke test with assertions on the sample grid as a cheap regression check for future edits.

## Static Analysis Results

I ran flake8 with the default pycodestyle rules on the revised file. The pass surfaced a few residual issues the manual pre-review had missed:

1. Two lines over 79 characters in the `_search` signature after the parameters grew to include `tiles`, `rows`, `cols`, `visited`, and `found`. Fixed by breaking the recursive call onto a continuation line.
2. Missing blank lines around the module-level `DIRECTIONS` definition (E302). Added.
3. Trailing whitespace on a comment line near the setter block (W291). Removed.

After cleanup, flake8 returned no warnings on the final file. I kept the default 79-character line limit rather than widening it, since the course style guide treats PEP 8 as the baseline.

## Regression Testing

To confirm the refactor preserved behavior, I verified against two layers of tests:

1. The 35-case unittest suite from the earlier phase of the project, split across four classes covering algorithmic scalability, simple edge cases, complete coverage, and the Qu/St/Ie special-tile handling. The suite ran against the refactored solver with no changes to the test file. All 35 tests passed.
2. The in-file `main()` smoke test with assertions on the sample grid. The assertions confirm that `abef`, `afjieb`, and `dgkd` resolve, and that `dgka` is correctly excluded. The `afjieb` case specifically exercises the multi-character `Ie` tile, which is the piece of logic most likely to break under the extract-to-helpers refactor.

One of the assertions caught a mistake I made while drafting the smoke test. I had initially asserted that `dgka` should resolve, but tracing the grid shows no `A` tile is adjacent to the `K` at position (2,2). The solver was correct to exclude it, and the assertion was wrong. I corrected the assertion to document the exclusion rather than silently remove it.

## Reflection

The review loop taught me that the most useful feedback is specific enough to act on at a particular line. The trie-caching note was the clearest example. One sentence from my partner changed how the solver scales on repeated calls, and I would not have caught it on my own because I had stopped seeing the code the way a new reader does.

On the giving side, I had to work at telling my own preferences apart from issues that were actually wrong. When I first drafted my review of my partner's solver, I flagged single-letter variable names like `n` and `t`. On a second pass I realized they stood for the grid size and the tile, and the context made that obvious. I dropped the comment. Learning to defend my own style choices and give others room to defend theirs is the main thing I want to carry into professional code review, where the stakes and the social dynamics are both higher than they are in a class exercise.