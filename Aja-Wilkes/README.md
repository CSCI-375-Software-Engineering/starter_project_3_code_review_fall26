Overview:
The original solver was functionally correct and compiled successfully in  assignment 1; however,
it failed the style check with 41 errors (primarily indentation).

This review covers the Boggle solver from Assignment #2 and my test file.
The goal was to make both files follow PEP 8, Python's standard set of style rules, and I used
Codio's built-in code analysis to check them.


Partner Review: 
Before making any changes, I had a partner review my original code. Their main feedback was
that my indentation was incorrect, and may be flagged by Codio, and that the code did not check for uneven rows.
Their feedback did align with Codio's code analysis, where 24 of the 41 errors were indentation errors. I used my partner's code review
and the analysis results together to plan my fixes, starting with the indentation since it was the biggest problem. 

How I reviewed the Code:

1. Ran Codio's code analysis to get list of style errors.
2. Read through each method, ensuring logic was sound.
3. Fixed a few lines at a time, running the analysis after each.
4. Ran unit tests at the end to ensure corrections did not break anything.

Errors Found included: E111, E501, W293, E261, E231, E116, E301, E211
and W292. These are indent errors, blank lines with spaces, missing space after commas, comment indentation incorrect,
and no newline at the end of the file. 

Does the Code Work?

Yes, it works on the sample grid and finds all 20 words it should, including words that use the 
"Qu" or "St" tiles. It also correctly skips words that can't be made like "arty" or "not".

What works well?

- It skips dead ends
- Capital letters don't matter
- Two-letter tiles works
- No tile is used twice

What could be better?

- Checking for duplicates words is slow on big boards because the 
answers are stored in a list.
- The solver doesn't check that the grid is a square
- All methods do not include docstring explaining their functionally

What I Changed:
I only changed formatting, the logic, method names, and results are the same as before.
My indents were really off and I used ClaudeAI to fix them without changing the logic or existing code.

What I Learned?

The biggest thing I learned is to be careful moving Python code
from one source (Github) to another. This caused my indentation to be severely incorrect. Additionally,
I learned to always check unit tests after the move and fixing any formatting issues. Specifically, to check in sections and I
correct to ensure I don't mess anything up. I'd also look into adding docstrings and more detailed comments to my methods to help those reviewing my code understand my logic. 


 



