"""
Matthew Herriman
@03130572
"""


class Boggle:
    # The eight neighbors of a tile, including diagonals.
    DIRECTIONS = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1), (0, 1),
                  (1, -1), (1, 0), (1, 1)]

    def __init__(self, grid, dictionary):
        self.grid = grid
        self.dictionary = dictionary
        self.solutions = []

    def setGrid(self, grid):
        # Set the game grid.
        self.grid = grid

    def setDictionary(self, dictionary):
        # Set the dictionary of words.
        self.dictionary = dictionary

    def validInput(self):
        # Check that the grid is a non-empty list of lists.
        if not isinstance(self.grid, list) or len(self.grid) == 0:
            return False

        for row in self.grid:
            if not isinstance(row, list):
                return False

        # Check that rows are non-empty, the same length,
        # and that every tile is a non-empty string.
        columns = len(self.grid[0])
        if columns == 0:
            return False

        for row in self.grid:
            if len(row) != columns:
                return False
            for tile in row:
                if not isinstance(tile, str) or tile == "":
                    return False

        # Check that the dictionary is a list of strings.
        if not isinstance(self.dictionary, list):
            return False

        for word in self.dictionary:
            if not isinstance(word, str):
                return False

        return True

    def getSolution(self):
        # Start fresh so repeated calls do not duplicate results.
        self.solutions = []

        if not self.validInput():
            return self.solutions

        # Search for every dictionary word in the grid.
        for word in self.dictionary:
            # Skip words already found (duplicates in the dictionary).
            if word in self.solutions:
                continue
            if len(word) >= 3 and self.findWord(word):
                self.solutions.append(word)

        return self.solutions

    def findWord(self, word):
        # Lowercase once here instead of on every recursive call.
        word = word.lower()

        # Try every tile as a starting point.
        for row in range(len(self.grid)):
            for col in range(len(self.grid[row])):
                if self.search(row, col, word, 0, set()):
                    return True

        return False

    def search(self, row, col, word, index, used):
        # The whole word has been matched.
        if index == len(word):
            return True

        # Make sure the position is inside the grid.
        if not (0 <= row < len(self.grid)):
            return False
        if not (0 <= col < len(self.grid[row])):
            return False

        # A tile cannot be used more than once.
        if (row, col) in used:
            return False

        # The tile must match the word at the current position.
        tile = self.grid[row][col].lower()
        if not word.startswith(tile, index):
            return False

        used.add((row, col))

        # Move forward by the number of letters in the tile,
        # so tiles like Qu, St, and Ie are handled.
        next_index = index + len(tile)

        # Try all eight neighbors; stop at the first success.
        found = any(
            self.search(row + d_row, col + d_col, word, next_index, used)
            for d_row, d_col in self.DIRECTIONS
        )

        # Backtrack: free this tile for other paths.
        used.remove((row, col))
        return found


def main():
    grid = [["T", "W", "Y", "R"], ["E", "N", "P", "H"],
            ["G", "Z", "Qu", "R"], ["O", "N", "T", "A"]]
    dictionary = ["art", "ego", "gent", "get", "net", "new", "newt",
                  "prat", "pry", "qua", "quart", "quartz", "rat",
                  "tar", "tarp", "ten", "went", "wet", "arty",
                  "rhr", "not", "quar"]

    mygame = Boggle(grid, dictionary)
    print(mygame.getSolution())


if __name__ == "__main__":
    main()
