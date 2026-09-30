
    


"""
NAME: Nydeef Taylor
SID: 004003163

Boggle Solver
CSCI 363 - Large Scale Programming
"""

class Boggle:
    """
    Solves a Boggle board for words contained in a dictionary.

    A word can use adjacent tiles, including diagonals.
    A tile cannot be used more than once in the same word.
    The special tiles Qu, St, and Ie count as two letters.
    """

    def __init__(self, grid, dictionary):
        """Create a Boggle game with the given grid and dictionary."""
        self.grid = []
        self.dictionary = []
        self.solution = []

        self.setGrid(grid)
        self.setDictionary(dictionary)
        self.solution = self._findSolutions()

    def setGrid(self, grid):
        """Set the Boggle grid if it is a valid 2D list of strings."""
        if not isinstance(grid, list) or len(grid) == 0:
            self.grid = []
            return

        if not all(isinstance(row, list) for row in grid):
            self.grid = []
            return

        if not all(len(row) == len(grid[0]) for row in grid):
            self.grid = []
            return

        if len(grid[0]) == 0:
            self.grid = []
            return

        valid_tiles = {"QU", "ST", "IE"}

        for row in grid:
            for tile in row:
                if not isinstance(tile, str) or tile == "":
                    self.grid = []
                    return

                # Normal tiles are one letter. Special tiles are two letters.
                if len(tile) != 1 and tile.upper() not in valid_tiles:
                    self.grid = []
                    return

        # Store a copy so the original grid cannot accidentally be changed.
        self.grid = [row[:] for row in grid]

    def setDictionary(self, dictionary):
        """Set the dictionary if it is a valid list of words."""
        if not isinstance(dictionary, list):
            self.dictionary = []
            return

        for word in dictionary:
            if not isinstance(word, str):
                self.dictionary = []
                return

        # Store a copy and remove duplicate words.
        self.dictionary = list(dict.fromkeys(dictionary))

    def getSolution(self):
        """Return a list of all dictionary words found on the board."""
        return self.solution[:]

    def _findSolutions(self):
        """Find every valid dictionary word that can be made on the board."""
        if not self.grid or not self.dictionary:
            return []

        # Convert dictionary words to uppercase for case-insensitive matching.
        words = []
        for word in self.dictionary:
            word_upper = word.upper()

            # Words must be at least 3 letters long.
            if len(word_upper) >= 3:
                words.append(word_upper)

        found = []

        for word in words:
            if self._canMakeWord(word):
                found.append(word)

        return found

    def _canMakeWord(self, word):
        """Return True if the word can be made without reusing a tile."""
        rows = len(self.grid)
        cols = len(self.grid[0])

        for row in range(rows):
            for col in range(cols):
                if self._search(word, 0, row, col, set()):
                    return True

        return False

    def _search(self, word, position, row, col, used):
        """
        Recursively search for a word starting at one board tile.

        position is the character position currently being matched.
        used contains board positions that have already been used.
        """
        rows = len(self.grid)
        cols = len(self.grid[0])

        if row < 0 or row >= rows or col < 0 or col >= cols:
            return False

        if (row, col) in used:
            return False

        tile = self.grid[row][col].upper()

        # The tile must match the next part of the word.
        if not word.startswith(tile, position):
            return False

        new_position = position + len(tile)

        # The entire word has been matched.
        if new_position == len(word):
            return True

        used.add((row, col))

        # Check all 8 neighboring positions, including diagonals.
        for row_change in (-1, 0, 1):
            for col_change in (-1, 0, 1):
                if row_change == 0 and col_change == 0:
                    continue

                if self._search(
                    word,
                    new_position,
                    row + row_change,
                    col + col_change,
                    used
                ):
                    used.remove((row, col))
                    return True

        used.remove((row, col))
        return False


def main():
    """Create a Boggle game and print its solution."""
    grid = [
        ["A", "B", "C", "D"],
        ["E", "F", "G", "H"],
        ["Ie", "J", "K", "L"],
        ["A", "B", "C", "D"]
    ]

    dictionary = ["ABEF", "AFJIEB", "DGKD", "DGKA"]

    mygame = Boggle(grid, dictionary)
    print(mygame.getSolution())


if __name__ == "__main__":
    main()
  