# Project 3 Code Review Summary Report

**Matthew Herriman | CSCI-375 Software Engineering**

## 1. Overview

This project simulated a real software engineering workflow. I took my Boggle solver, submitted it as a pull request on GitHub, and had a partner review it. I reviewed my partner's solver in return. I then used the feedback to improve my code, ran it through a style linter (pycodestyle) and my unit tests in Codio, and wrote this report.

My solver validates the grid and dictionary, then uses recursive backtracking to find every dictionary word of three or more letters that can be built from adjacent tiles (including diagonals) without reusing a tile. It also handles multi-letter tiles such as "Qu", "St", and "Ie". My original version is saved as `boggle_solver.py.orig` and the improved version is `boggle_solver.py`.

## 2. Feedback I Received

My partner's review included both praise and suggestions.

**Praise:** The overall structure was neat and easy to read. The `validInput()` method checked the grid and dictionary for invalid data before searching. The methods were separated logically for validation, word searching, and recursive traversal. The code handled edge cases such as empty grids, uneven rows, invalid data types, and tile reuse, and the method names and comments made it readable and maintainable.

**Suggestions:**
1. Track visited tiles with a set of `(row, col)` tuples instead of a list, which makes the "already used" check more efficient.
2. Reset `self.solutions` at the start of `getSolution()` so calling the method more than once does not add duplicate results.
3. Simplify some repeated logic in the code.

## 3. Feedback I Gave

I reviewed my partner's solver and left ten inline comments plus an overall summary comment.

**Strengths I pointed out:** the clear organization and the use of recursion with backtracking and a visited set; checking all eight neighbors, with a separate check that skips the current tile; having input validation in its own method; rejecting empty or invalid grids; validating the dictionary before searching; and using the grid length to enforce that rows are the same length. I noted that this prevents errors later when individual tiles are accessed.

**Suggestions I made, phrased as questions:**
- Validating against empty-string tiles, since an empty tile was currently treated as valid.
- Preventing duplicate words from being added if the dictionary contains the same word more than once.

## 4. Improvements I Implemented

Each change below is tied to what prompted it: a specific comment from my partner (Section 2) or something I identified myself.

### Changes made because of my partner's feedback

#### Change 1: Visited tiles are now a set of (row, col) tuples

**Prompted by:** Partner suggestion 1.

**Before:** `used` was a list of `[row, col]` lists, checked with `[row, col] in used` and updated with `append` and `pop`.

**After:** `used` is a set of tuples, updated with `add` and `remove`.

**Why:** Checking whether a tile was already used is now O(1) instead of scanning the list, which matters because the check runs on every recursive call.

#### Change 2: `self.solutions` is reset at the start of `getSolution()`

**Prompted by:** Partner suggestion 2.

**Before:** Results were appended to the existing list, so calling `getSolution()` twice returned each word twice.

**After:** `getSolution()` starts with `self.solutions = []`.

**Why:** Repeated calls now return a fresh, correct result.

#### Change 3: Repeated direction logic replaced with a `DIRECTIONS` constant and `any(...)`

**Prompted by:** Partner suggestion 3 (simplify repeated logic).

**Before:** Two nested loops over `[-1, 0, 1]`, a separate `(0, 0)` skip, and `used.pop()` repeated in two places.

**After:** A `DIRECTIONS` list of the eight neighbors and a single `any(...)` call, with one `remove` at the end.

**Why:** The neighbors are defined in one place, the skip check is gone, and the backtracking step happens in one spot instead of two.

### Changes I made myself

#### Change 4: `findWord()` lowercases the word once and no longer duplicates the starting-tile check

**Prompted by:** My own cleanup.

**Why:** `search()` already checks whether a tile matches, so the extra check in `findWord()` was redundant, and lowercasing on every recursive call was wasted work.

#### Change 5: `== False` replaced with `not`, and validation and bounds checks made more compact

**Prompted by:** My own cleanup, and a lint error (see Section 5).

**Why:** This is more idiomatic Python, and it fixed the E712 lint error.

#### Change 6: Empty-string tiles are rejected in `validInput()`

**Prompted by:** Reviewing my partner's code, where I suggested the same check.

**Before:** A tile of `""` passed validation and matched without consuming any letters, so it acted like a wildcard.

**After:** `validInput()` returns `False` if any tile is an empty string.

**Why:** Empty tiles can produce words that are not really on the board.

#### Change 7: Duplicate dictionary words are skipped in `getSolution()`

**Prompted by:** Reviewing my partner's code, where I suggested the same check.

**Before:** A word listed twice in the dictionary appeared twice in the results.

**After:** `getSolution()` skips any word already in `self.solutions`.

**Why:** Each word should be reported once.

## 5. Static Analysis Results

The pycodestyle analyzer in Codio reported these issues on my solver, and I fixed all of them:
- **E302:** expected two blank lines before the class definition.
- **W291:** trailing whitespace after the `__init__`, `search`, and `main` definitions.
- **E712:** comparison to `False` replaced with `not`.
- **W292:** no newline at end of file.

The analyzer also flagged my test file, which I cleaned up:
- **E261 / E262 / E501:** an inline comment with too little spacing, a malformed `#` comment, and a line over the length limit.
- Mixed tabs and spaces, 2-space indentation changed to 4 spaces, stray semicolons, missing spaces after commas, and missing blank lines between classes.

Both analyzers now report no errors.

## 6. Regression Testing

After each round of changes I submitted the solver to the Codio auto-grader and ran my unit tests to confirm nothing broke. I resubmitted after every set of fixes, 6 times in total. The tests check a normal 3x3 grid with a multi-letter tile, a 1x1 grid, and an empty grid. I also ran two quick checks in the Codio terminal, one with a duplicated dictionary word and one with an empty-string tile, to confirm that Changes 6 and 7 behave correctly. At one point the analyzer kept showing old results because my new code had not actually replaced the old file, so I learned to confirm that the file I edited is the one being checked (for example by running `pycodestyle` in the terminal). The final version passes all Codio tests and lint checks.

## 7. Reflection

Code review showed me how much I miss in my own code. I wrote the solver and read it many times, but my partner immediately saw an efficiency improvement and a bug I had not considered (duplicate results on repeated calls). Reviewing their code also made me think harder about edge cases, such as empty-string tiles and duplicate words in a dictionary. When I checked my own solver, I found it did not handle either one, and I fixed both.

I also learned that how feedback is written matters. Phrasing suggestions as questions and starting with what works well made the review easier to receive and easier to act on. Finally, the static analysis step showed that formatting and style are not cosmetic. Consistent style catches real problems, such as tabs mixed with spaces, and makes code easier for the next person to maintain. Running lint, tests, and review together is a workflow I would use on a real team.
