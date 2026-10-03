#Project 3: Code Review Summary Report
**Name:** Ohene Baffoe Osei
**Review partner:** Amaia Murat (amaiamurat)
**Branch:** ohene-osei-review
**Pull request:** Project 3 Code Review — Ohene Osei (https://github.com/CSCI-375-Software-Engineering/starter_project_3_code_review_fall26/pull/2)

##Overview

This assignment is software engineering workflow through GitHub branches, pull requests, peer reviews, static analysis, and regression testing. I worked on my Boggle solver in the Ohene-Osei subfolder of the class repository, using a separate branch to keep proposed changes out of main until review.
My solver uses a trie to stop searches when a path is not a dictionary prefix. Recursive backtracking explores all eight neighboring positions and prevents tile reuse within a word. It handles multi-letter tiles such as Qu, St, and Ie, excludes words shorter than three characters, and returns unique matches in dictionary order. I preserved the original solver as boggle_solver.py.orig and verified that it matched my initial Git commit before preparing the final version.
Feedback You Received
My partner praised the input validation and handling of multi-letter tiles. Her main suggestions were to remove redundant result attributes, use consistent indentation, replace the minimum word length and trie end marker with named constants, and give the search method a clearer name. She also suggested returning results directly rather than keeping unnecessary state on the object. These comments focused on making the existing algorithm easier to understand and maintain.

#Feedback I Gave To My Partner

I suggested improving my partner's input validation and error handling because a bare except: can hide unexpected programming errors by returning an empty list. I also suggested using a set for duplicate checks while retaining a list for results, and reusing the visited matrix instead of allocating it for every starting position. Backtracking already restores the visited entries between paths.
I praised the trie prefix check and explanatory comments. My inline feedback and overall summary explained the reasons behind the suggestions, using questions to keep the discussion constructive. 

#Improvements I Implemented

I removed self.solution and self.solutions, using a local solutions list inside getSolution() instead. Each call now builds fresh results without requiring the setters to reset stored output. I introduced MIN_WORD_LENGTH = 3 and END_OF_WORD = "#" to explain the repeated values and provide one place to change them.
I renamed dfs to search_from_tile, updated its calls, standardized indentation to four spaces, and added concise docstrings and comments. I also replaced membership-tracking dictionaries with sets. Public methods such as getSolution, setGrid, and setDictionary retained their names so the existing tests could call them.

#Static Analysis Results

I formatted the final solver and Assignment #2 tests with autopep8, then checked both with pycodestyle. The solver initially lacked a final newline. An attempted fix introduced a whitespace-only blank line and an extra trailing blank line; I corrected these and reran the check. Both final files passed without reported style violations. Codio's solver and unit-test analysis checks also passed.

#Regression Testing

I ran all 25 Assignment #2 Boggle tests against the improved solver. They checked invalid inputs, word length, adjacency, tile reuse, capitalization, duplicates, multi-letter tiles, and board sizes up to 7×7. All 25 passed, and the instructor's Codio correctness suite passed as well.

#Verification

I discovered that the workspace initially contained five starter tests, including two placeholders that only compared True with True. I replaced that file with my completed Boggle suite and confirmed the test names and count. This prevented a misleading passing result from being treated as sufficient verification.

#Reflection

I learned that a working solution can still benefit from clearer names, consistent formatting, and less stored state. Peer review helped me understand how another reader experiences my code and why suggestions should explain their purpose.
The workflow also clarified Git's role: commits preserve local versions, pushes share them, and pull requests support discussion before merging. Comparing the original file with Git history gave me confidence that the pre-review version was preserved. In future projects, I will check the exact files being edited and tested, inspect test summaries carefully, and rerun checks after refactoring. I will approach reviews as collaborative discussions supported by explanations and evidence.

