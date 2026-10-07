# Project 3: Code Review Summary
**Jared Percy | CSCI 375 | October 3, 2026**

## Overview

This assignment focused on using a professional software engineering
workflow to review and improve a Boggle solver. The main tasks included
creating a GitHub branch and pull request, exchanging peer reviews,
checking code style, making improvements, and testing the solver again.

I started with my Python Boggle solver from Assignment 2. I created
the Jared-Percy-review branch in the class repository and added my
files to the Jared-Percy folder. I opened pull request #13 so my work
could be reviewed before being merged into main. I also preserved an
unchanged copy of my original solver as boggle_solver.py.orig.

My approach was to keep the working solver intact while checking for
style problems. This allowed me to make small, traceable changes and
compare the final file with the original version. I used Codio to
check that the solver still worked in the required environment.

## Feedback Received

My assigned partner was Rami Hassen Osman. I contacted him to request
a code review and his pull request link. I also contacted my professor
to explain that the peer-review exchange was still pending and to ask
how to proceed before the deadline.

At the time of writing this report, I had not received a response
from either my partner or my professor. Therefore, I did not receive
peer feedback that I could apply to my solver. The changes described
below came from the style-checking process, rather than a completed
partner review.

The peer-review portion remains incomplete. I have documented that
status honestly instead of presenting my own changes as suggestions
from my partner.

## Feedback Given

I had not received my partner’s code or pull request link by the
time I prepared this submission. As a result, I could not examine
his implementation or submit the required inline comments and
overall review summary.

For a completed review, I would examine correctness, edge cases,
efficiency, naming, readability, and maintainability. I would make
comments specific to the code and explain why each suggestion could
help. I would also phrase suggestions respectfully as questions and
recognize parts of the implementation that were clear or effective.

These are my intended review criteria, not feedback that I have
already given. I understand that preparing to review code does not
replace completing the actual review.

## Improvements Implemented

The changes I completed were small formatting corrections identified
while checking the solver in Codio. First, I removed trailing
whitespace at the end of line 159. Extra spaces at the end of a line
are unnecessary and can create distracting differences when comparing
versions of a file.

After removing those spaces, the style checker reported that the
file did not end with a newline. I added a final newline and saved
the file again. This corrected the second warning without changing
the solver’s logic.

I kept boggle_solver.py.orig unchanged and updated boggle_solver.py
with the corrected version. Preserving both versions provides a
record of what changed. I did not make major algorithm changes or
claim that these formatting fixes improved the solver’s performance.

## Static Analysis Results

I ran the following command in the Codio terminal:

    pycodestyle boggle_solver.py

The first reported issue was:

    W291 trailing whitespace

After fixing it, the next reported issue was:

    W292 no newline at end of file

I corrected both issues and ran the command again. The final run
returned to the terminal prompt without printing any warnings.
This showed that Pycodestyle found no remaining issues under the
checks used in that environment.

Pycodestyle checks formatting against Python’s PEP 8 style guide.
A clean result does not prove that a program is correct or that
every part of its design is easy to maintain. For that reason, I
also used the Codio tests to check the solver’s behavior.

The tool run documented here was Pycodestyle. I did not complete
a separate automatic formatter run.

## Regression Testing

Before the formatting changes, the Codio test run reported:

    Ran 26 tests in 0.018s
    OK

After correcting the whitespace and final newline, I submitted the
solver to the Codio autograder again. All 26 tests passed again.
This was my regression check to confirm that the changes did not
break behavior covered by the supplied tests.

The successful result supports that the solver continued to work
for those tested cases. It does not establish that every possible
input is handled correctly. However, running the tests again after
editing was important because even a small accidental change could
introduce a problem.

## Reflection

This assignment helped me practice using branches and pull requests
to organize changes. A branch gave me a place to prepare my work,
while the pull request provided a location for review and discussion.
Keeping the original file also made the changes easier to trace.

I learned that style checking and functional testing serve different
purposes. The tests passed even when the file contained a style
warning. Pycodestyle identified that warning, and regression testing
then confirmed that fixing it preserved the tested behavior.

The incomplete peer-review exchange also showed me that collaboration
requires communication and time. In future projects, I would arrange
the exchange earlier so both partners have more time to review,
respond, and revise their work.

I completed the independent checks available to me and documented
the remaining limitation. My submission includes the original solver,
the corrected solver, and this report. Receiving and giving peer
feedback remain pending as of this report.
