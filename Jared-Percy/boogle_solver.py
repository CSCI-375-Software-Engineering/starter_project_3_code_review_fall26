"""
Name: Jared Percy
SID: 004003288

This program finds words on a Boggle board.
"""


class Boggle:
    """This class stores and solves one Boggle game."""

    def __init__(self, grid, dictionary):
        """Sets up the grid, dictionary, and answer list."""
        self.grid = grid
        self.dictionary = dictionary
        self.solutions = []

    def setGrid(self, grid):
        """Changes the grid."""
        self.grid = grid
        self.solutions = []

    def setDictionary(self, dictionary):
        """Changes the dictionary."""
        self.dictionary = dictionary
        self.solutions = []

    def validInput(self):
        """Checks if the grid and dictionary can be used."""

        if not isinstance(self.grid, list) or len(self.grid) == 0:
            return False

        if not isinstance(self.dictionary, list):
            return False

        size = len(self.grid)

        # Make sure the grid is square.
        for row in self.grid:
            if not isinstance(row, list) or len(row) != size:
                return False

            for tile in row:
                if not isinstance(tile, str) or tile == "":
                    return False

        # Make sure every word is a string.
        for word in self.dictionary:
            if not isinstance(word, str):
                return False

        return True

    def findWord(self, word):
        """Tries to start the word from every tile."""

        for row in range(len(self.grid)):
            for column in range(len(self.grid[row])):
                used = set()

                if self.search(word, row, column, 0, used):
                    return True

        return False

    def search(self, word, row, column, position, used):
        """Searches the tiles around the current tile."""

        # Return True once every letter is found.
        if position == len(word):
            return True

        # Return False if the position is outside the grid.
        if row < 0 or row >= len(self.grid):
            return False

        if column < 0 or column >= len(self.grid[row]):
            return False

        # Do not use a tile that was already used.
        if (row, column) in used:
            return False

        tile = self.grid[row][column].lower()

        # Check if the tile matches the next part of the word.
        # This also works for Qu, St, and Ie.
        if not word.startswith(tile, position):
            return False

        next_position = position + len(tile)
        used.add((row, column))

        # Check the eight tiles around the current tile.
        for row_move in [-1, 0, 1]:
            for column_move in [-1, 0, 1]:

                if row_move == 0 and column_move == 0:
                    continue

                if self.search(
                    word,
                    row + row_move,
                    column + column_move,
                    next_position,
                    used
                ):
                    used.remove((row, column))
                    return True

        # Remove the tile so it can be used in another path.
        used.remove((row, column))
        return False

    def getSolution(self):
        """Finds and returns all valid words."""

        self.solutions = []

        if not self.validInput():
            return []

        for word in self.dictionary:

            # Words must be strings with at least three letters.
            if len(word) < 3:
                continue

            lowercase_word = word.lower()

            if self.findWord(lowercase_word):
                if word not in self.solutions:
                    self.solutions.append(word)

        return self.solutions


def main():
    grid = [
        ["T", "W", "Y", "R"],
        ["E", "N", "P", "H"],
        ["G", "Z", "Qu", "R"],
        ["O", "N", "T", "A"]
    ]

    dictionary = [
        "art", "ego", "gent", "get", "net", "new", "newt",
        "prat", "pry", "qua", "quart", "quartz", "rat",
        "tar", "tarp", "ten", "went", "wet", "arty",
        "rhr", "not", "quar"
    ]

    mygame = Boggle(grid, dictionary)
    print(mygame.getSolution())


if __name__ == "__main__":
    main()

