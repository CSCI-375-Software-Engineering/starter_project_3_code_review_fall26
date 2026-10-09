# CSCI-375 Project 3: Code Review Summary

**Student:** Nydeef Taylor
**Course:** CSCI-375 Software Engineering
**Repository:** `starter_project_3_code_review_fall26`
**Branch:** `nydeef-taylor-review`

## 1. Overview

The purpose of this assignment was to practice a professional software development workflow involving Git, GitHub pull requests, peer code reviews, code improvements, and testing. I reviewed a classmate's Boggle solver and received feedback on my own implementation. I used that feedback to improve the correctness, reliability, and maintainability of my code.

My implementation uses a `Boggle` class to validate a board and dictionary, search for dictionary words, and return the words found. The recursive search checks neighboring tiles, including diagonals, while preventing a tile from being reused within the same word.

## 2. Feedback Received

My reviewer identified three areas for improvement:

* **Refreshing solutions:** The solution list was originally calculated during initialization. Updating the board or dictionary could leave the stored results outdated.
* **Duplicate dictionary entries:** Dictionary words were deduplicated before being converted to uppercase. As a result, entries such as `"cat"` and `"CAT"` could become duplicate results after normalization.
* **Tile validation:** The board validation accepted any single-character string, including digits and punctuation, even though ordinary tiles should be letters.

This feedback helped me identify edge cases that were not handled by my original implementation.

## 3. Feedback Given

I reviewed my classmate's Boggle solver and provided feedback about Python naming conventions, dictionary variable clarity, and the recursive search's visited-set behavior. I recommended clearer variable names and comments to make the code easier to understand and maintain.

After my classmate made improvements, I reviewed the changes and approved the updated pull request. This experience demonstrated how specific, constructive feedback can improve code readability without requiring a complete rewrite.

## 4. Improvements Implemented

I updated my `boggle_solver.py` file to address the feedback I received.

First, I added solution refreshes when the board or dictionary is updated. Invalid input also clears the stored solution, preventing previous results from being returned after invalid data is supplied.

Second, I normalized dictionary words to uppercase before removing duplicates. This ensures that words differing only in capitalization are treated as the same entry.

Third, I strengthened board validation so single-character tiles must be alphabetic. Invalid tiles such as `"1"` are rejected, while the special two-letter tiles `Qu`, `St`, and `Ie` remain supported.

I preserved my original implementation as `boggle_solver.py.orig` and committed the updated solver and backup to my existing GitHub branch. The changes were pushed successfully in commit `ff68977`.

## 5. Static Analysis Results

Static analysis with `pycodestyle` has not yet been run. The code should be checked with the assignment's required formatter or linter, and any reported issues should be addressed before final submission.

I also used Python's compilation check to verify that the updated file had valid syntax. The program ran successfully with its example board and dictionary.

## 6. Regression Testing

I performed manual checks for the three reported issues:

* **Case-insensitive duplicates:** Supplying `["cat", "CAT"]` produced `["CAT"]` rather than duplicate results.
* **Invalid tile rejection:** Supplying a board containing `"1"` caused the board to be rejected.
* **Dictionary refresh:** Changing the dictionary to `["TAX"]` refreshed the solution, which returned `["TAX"]` for the test board.

These checks passed. However, they were executed as manual tests rather than saved as a permanent automated test suite. Additional assignment-required tests and a board-update test should be run before the final submission.

## 7. Reflection

This assignment helped me understand that code review is not simply about finding mistakes. It is an opportunity to improve software by considering edge cases, readability, maintainability, and the behavior of code after changes are made.

I also gained experience using Git to preserve an original file, commit improvements, and push changes to an existing pull request branch. One important lesson was that a program running successfully does not guarantee that every requirement is satisfied. Targeted tests are needed to verify individual behaviors, and automated tests make those checks repeatable.

In future projects, I would write tests for edge cases earlier in development and run the required linting tools before requesting a final review. Overall, this assignment gave me practical experience with collaborative software development and the importance of reviewing, testing, and documenting changes.
