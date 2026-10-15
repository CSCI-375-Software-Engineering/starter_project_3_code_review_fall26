Project 3: Code Review and Static Analysis Summary

Autumn Knox
CSCI-375 Software Engineering

Overview

For Project 3, I worked on improving my Boggle Solver by going through the code review and static analysis process. For this project, I created my own branch on GitHub, opened a pull request, reviewed another student’s code, received feedback on my own code, and then made changes based on that feedback. I also used static analysis and testing to make sure my final code was formatted correctly and still worked after I made changes.

My Boggle Solver takes a grid of letters and a dictionary and finds the words that can actually be made using the board. The program checks the letters around each tile in all eight directions and makes sure that the same tile is not used twice when creating a word. It also works with special tiles such as “Qu.” My main goal during this project was to keep my code working while also making it cleaner and easier for someone else to understand.

Feedback I Received

My partner for the code review was Nylah Shepherd. She gave me feedback on different parts of my Boggle Solver and also pointed out things that I did well. For example, she liked that I separated the row and column boundary checks instead of putting everything into one long condition. She also said that variable names like row_change and col_change made the code easier to follow. She also liked how I listed all eight possible directions and included comments explaining important parts of my search method.

One of her suggestions was to add separate setGrid() and setDictionary() methods so the grid and dictionary could be updated more easily. She also noticed that I had an import re statement that was not actually being used. Another thing she noticed in an earlier version of my code was that main() was being called twice, which could cause my results to print twice. She also suggested adding more comments around the part of my code that searches through the grid because that is one of the more important parts of the solver.

Feedback I Gave

I also reviewed Nylah’s Boggle Solver and gave her feedback on what I thought worked well and what could possibly be improved. One thing I liked was how she had all eight directions in a list because it made it easy to see all of the different directions the program could search. I also thought her boundary checks were helpful because they stopped the program from searching outside of the grid.

For one of my suggestions, I mentioned that she could use a separate variable for the lowercase version of a word instead of changing the original word variable. I thought this would make that section a little easier to read. I also suggested possibly moving some of the grid validation into its own method. That could make the main method less crowded and separate the validation from the actual searching. I tried to make sure that my review did not only focus on what could be changed, but also what I thought was already done well.

Improvements I Implemented

After I received my feedback, I went back through my code and made changes based on Nylah’s suggestions. I added setGrid() and setDictionary() methods so the grid and dictionary can be changed separately if needed. I also removed import re because I was not actually using it anywhere in my program.

I fixed the duplicate main() issue so the program would only run once. I also added more comments around the search portion of my code to explain what the loops are doing. I kept my comments for the row and column boundaries, tile matching, visited tiles, and the special tiles because those parts are important for understanding how my search works. I did not change everything about my program because some of the feedback showed that parts of my original organization were already clear.

Static Analysis Results

For static analysis, I used pycodestyle to check my final Boggle Solver. This helped me find formatting and PEP 8 issues that I might not notice just by looking at the code myself. When I ran it, I had a small issue involving the newline at the end of my file. I fixed that issue and ran pycodestyle again.

After fixing it, I ran the check again and there were no more errors shown. I think this part was useful because even though something small like a newline does not completely stop the program from working, it still matters when trying to keep code clean and properly formatted.

Regression Testing

After making my changes, I tested my Boggle Solver again because I wanted to make sure that fixing and cleaning up my code did not mess up anything that was already working. I used the Codio tests to check my final version.

My final test run completed 26 tests and all 26 passed. The result came back as OK. The tests checked normal grids, different grid sizes, different directions, duplicate letters, empty grids, and special cases involving tiles such as “Qu” and “St.” I also ran the Codio correctness check and received a passing result. This showed me that I was able to make changes based on the code review without breaking the actual solver.

Reflection

This project helped me understand code review better because before this, I mainly thought about whether my code worked or not. With this assignment, I had to look at my code from the perspective of someone else who might have to read it or work on it later. Something can work correctly but still be confusing or harder to maintain than it needs to be.

I also liked being able to see someone else’s approach to the same assignment because there can be different ways to solve the same problem. Reviewing Nylah’s code made me pay more attention to things like organization, variable names, comments, and how methods are separated. Getting feedback on my own code also helped because she noticed things that I did not really think about when I first wrote it.

The static analysis and regression testing were also important because they showed me that reviewing code is not just about manually reading it. Tools can help catch smaller issues, and tests help make sure that changes do not create new problems. Overall, I feel like this project gave me a better understanding of how code review, GitHub, testing, and static analysis would be used when working with other people on a software project.
