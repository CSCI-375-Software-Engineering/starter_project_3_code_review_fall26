# Project 3 Code Review Summary Report

**Name:** Kwesi [Last Name]
**Course:** CSCI 375 Software Engineering
**Reviewer / Review Partner:** [Partner Name]

## Overview

This project simulated the code review process used on real software teams. I took my Boggle solver from the earlier assignment, pushed it to my own branch in the shared class repository, and opened a pull request into main. My partner and I reviewed each other's pull requests on GitHub, leaving inline comments and an overall summary. After the review, I saved my original file as `boggle_solver.py.orig`, updated the solver based on the feedback, and then ran it through Prettier and Pycodestyle in Codio to clean up any remaining style issues.

My approach was to treat the review like I would at an internship: read every comment, decide what change it called for, make the change, and confirm the solver still passed all the tests before pushing again.

## Feedback I Received

My partner's feedback focused on two main areas:

1. **Comments.** Several functions had little or no explanation of what they did. The search logic in particular was hard to follow without stepping through it, since it wasn't clear what each part of the traversal was responsible for or why certain checks were there.
2. **PEP 8 style.** Parts of the file didn't follow PEP 8, including inconsistent spacing, lines that ran too long, and naming that didn't match Python conventions.

Neither point was about the solver giving wrong answers. Both were about how easy the code was for someone else to read and work with, which ended up being the main theme of this whole assignment.

## Feedback I Gave

The issues I found in my partner's code were similar to the ones raised in mine. My main comments were:

1. **Missing or thin comments.** Some functions needed a short docstring or inline comment explaining their purpose, inputs, and return values.
2. **PEP 8 adherence.** I pointed out spacing, line length, and naming inconsistencies that didn't line up with the style guide.
3. **Refactoring for clarity.** A few sections packed a lot of logic into one place. I suggested breaking them into smaller helper functions and giving some variables more descriptive names so the intent of the code was obvious at a glance.

I tried to follow the review guidelines from class by phrasing suggestions as questions, using "we" instead of "you," and calling out parts of the code that were already done well.

## Improvements I Implemented

Based on my partner's review, I made these changes:

- **Added docstrings and comments.** Every function now has a docstring explaining what it does, and I added inline comments in the search logic so the steps of the traversal are easier to follow.
- **Renamed variables.** I replaced short or vague names with names that describe what the variable holds, using snake_case to match PEP 8.
- **Reformatted to PEP 8.** I fixed indentation, spacing around operators and commas, and blank lines between functions, and I broke up long lines.
- **Cleaned up structure.** I removed anything that wasn't being used and made sure related logic was grouped together so the file reads from top to bottom more naturally.

The goal of these changes was readability and maintainability. The solver's behavior stayed the same.

## Static Analysis Results

After the manual changes, I ran the code through Prettier for formatting and Pycodestyle for PEP 8 checks, then submitted to the Codio auto-grader. The main issues flagged were:

- **E501, line too long:** lines over the 79 character limit, which I split across multiple lines.
- **E302 / E305, expected 2 blank lines:** missing blank lines around function definitions.
- **E231 / E225, missing whitespace:** missing spaces after commas and around operators.
- **W291 / W293, trailing whitespace:** extra spaces at the end of lines and on blank lines.

I fixed each issue and resubmitted until the linter came back clean.

## Regression Testing

Since every change touched working code, I wanted to make sure nothing broke. After each round of edits, both from the review and from the linter, I resubmitted to the Codio auto-grader so the full test suite ran against the updated file. I only moved on once all the tests passed. This was especially important for the variable renames and refactoring, because a missed rename or a misplaced line could break the solver even though the change looked purely cosmetic.

## Reflection

The biggest takeaway for me was that code working correctly isn't the same as code being good. My solver passed the tests before the review, but my partner still had trouble following parts of it. On a real team, other people have to read, debug, and extend your code, so clarity matters as much as correctness.

Giving feedback taught me something too. Since my partner and I made similar mistakes, reviewing their code made me notice the same habits in my own. I also learned that how you phrase feedback matters. Asking questions and pointing out strengths makes it easier for someone to take the criticism well, which is important when you'll keep working with that person after the review.

Finally, the branch, pull request, review, and merge workflow made sense to me in a way it hadn't before. Keeping work off main until it's been reviewed protects the shared codebase, and tools like Pycodestyle catch the small style issues automatically so reviewers can focus on bigger questions like logic and design.
