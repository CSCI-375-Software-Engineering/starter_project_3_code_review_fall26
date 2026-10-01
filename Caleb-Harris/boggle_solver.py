"""
Name: Caleb Harris
SID: 003091457

Boggle Solver
This program searches a Boggle grid for valid words
from a provided dictionary.
"""


class Boggle:
    def __init__(self, grid, dictionary):
        self.grid = grid
        self.dictionary = dictionary
        self.solution = []

    def setGrid(self, grid):
        self.grid = grid

    def setDictionary(self,dictionary):
        self.dictionary = dictionary 

    def isValid(self):
        if not isinstance(self.grid, list) or len(self.grid) == 0:
            return False 

        if not isinstance(self.dictionary, list) or len(self.dictionary) == 0:
            return False

        size = len(self.grid) 

        for row in self.grid:
             
            if not isinstance(row, list):
                return False 

            if len(row) != size:
                return False

            for tile in row:
                if not isinstance(tile, str):
                    return False 

        for word in self.dictionary:
            if not isinstance(word, str):
                return False

        return True 

    def getSolution(self):
        if not self.isValid():
            return []

        self.solution = []

        for word in self.dictionary:
            if len(word) >= 3:
                if self.wordExists(word):
                    self.solution.append(word)

        return self.solution

    def wordExists(self, word):
        word = word.lower()

        for row in range(len(self.grid)):
            for col in range(len(self.grid[row])):
                if self.search(row, col, word, 0, set()):
                    return True

        return False

    def search(self, row, col, word, index, visited):
        # Make sure we are still inside the board
        if row < 0 or row >= len(self.grid):
            return False

        if col < 0 or col >= len(self.grid[row]):
            return False

        # Cannot use the same tile twice
        if (row, col) in visited:
            return False

        tile = self.grid[row][col].lower()

        # Check whether this tile matches the part of the word we need
        if not word.startswith(tile, index):
            return False

        # Move forward by the number of letters in the tile
        nextIndex = index + len(tile)

        # If we matched the entire word, we found it
        if nextIndex == len(word):
            return True

        # Mark this tile as used
        visited.add((row, col))

        # Check all 8 neighboring squares
        for rowChange in [-1, 0, 1]:
            for colChange in [-1, 0, 1]:

                # Don't stay on the current square
                if rowChange == 0 and colChange == 0:
                    continue

                if self.search(
                    row + rowChange,
                    col + colChange,
                    word,
                    nextIndex,
                    visited
                ):
                    return True

        # Backtrack: allow this square to be used on another possible path
        visited.remove((row, col))

        return False

def main():
    grid = [
        ["A", "B", "C", "D"],
        ["E", "F", "G", "H"],
        ["IE", "J", "K", "L"],
        ["A", "B", "C", "D"]
    ]

    dictionary = ["ABEF", "AFJIEEB", "DGKD", "DGKA"]

    mygame = Boggle(grid, dictionary)
    print(mygame.getSolution())


if __name__ == "__main__":
    main()