"""
Name: Rami Osman
SID: 004003896

This program finds dictionary words on a Boggle board.
"""

MIN_WORD_LENGTH = 3

# The eight neighbors of a tile: (row change, column change).
DIRECTIONS = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1), (0, 1),
    (1, -1), (1, 0), (1, 1),
]


class Boggle:
    """Stores a Boggle grid and dictionary and finds the words in it."""

    def __init__(self, grid, dictionary):
        """Sets up the grid, dictionary, and solution list."""
        self.grid = grid
        self.dictionary = dictionary
        self.solution = []

    @property
    def dictionary(self):
        """The list of words to look for."""
        return self._dictionary

    @dictionary.setter
    def dictionary(self, dictionary):
        """Stores the dictionary and lowercases it once, here.

        Doing this when the dictionary is set means getSolution() does
        not repeat the conversion on every call. Invalid dictionaries
        leave _entries as None so getSolution() can return [].
        """
        self._dictionary = dictionary
        self._entries = None
        self._words = set()
        self._prefixes = set()

        if not self._is_word_list(dictionary):
            return

        # Each entry pairs the caller's spelling with its lowercase form.
        self._entries = [(word, word.lower()) for word in dictionary]
        self._words = {lowered for _, lowered in self._entries
                       if len(lowered) >= MIN_WORD_LENGTH}
        self._prefixes = self._build_prefixes(self._words)

    def setGrid(self, grid):
        """Replaces the grid and clears any old solution."""
        self.grid = grid
        self.solution = []

    def setDictionary(self, dictionary):
        """Replaces the dictionary and clears any old solution."""
        self.dictionary = dictionary
        self.solution = []

    @staticmethod
    def _is_word_list(dictionary):
        """Returns True if the dictionary is a list of strings."""
        if not isinstance(dictionary, list):
            return False
        return all(isinstance(word, str) for word in dictionary)

    def _is_valid_input(self):
        """Returns True if the grid is a square list of non-empty
        strings and the dictionary is a list of strings."""
        if self._entries is None:
            return False
        if not isinstance(self.grid, list) or len(self.grid) == 0:
            return False

        size = len(self.grid)
        for row in self.grid:
            if not isinstance(row, list) or len(row) != size:
                return False
            for tile in row:
                if not isinstance(tile, str) or tile == "":
                    return False
        return True

    def _build_prefixes(self, words):
        """Returns every prefix of every word, so dead paths stop early."""
        prefixes = set()
        for word in words:
            for end in range(1, len(word) + 1):
                prefixes.add(word[:end])
        return prefixes

    def _search(self, row, column, current, used, found):
        """Extends the path through (row, column) using depth-first search.

        current is the text spelled so far, used holds the tiles on the
        path, and found collects every dictionary word reached.
        """
        size = len(self.grid)
        if row < 0 or row >= size or column < 0 or column >= size:
            return
        if (row, column) in used:
            return

        current = current + self.grid[row][column].lower()
        if current not in self._prefixes:
            return

        if current in self._words:
            found.add(current)

        used.add((row, column))
        for row_move, column_move in DIRECTIONS:
            self._search(row + row_move, column + column_move,
                         current, used, found)
        used.remove((row, column))

    def getSolution(self):
        """Returns the dictionary words found on the grid.

        Returns an empty list if nothing is found or the input is invalid.
        """
        self.solution = []
        if not self._is_valid_input():
            return []

        found = set()
        for row in range(len(self.grid)):
            for column in range(len(self.grid)):
                self._search(row, column, "", set(), found)

        # Keep the caller's spelling and the dictionary's order.
        for word, lowered in self._entries:
            if lowered in found and word not in self.solution:
                self.solution.append(word)
        return self.solution


def main():
    """Runs the Boggle solver on a sample grid."""
    grid = [["A", "B", "C", "D"],
            ["E", "F", "G", "H"],
            ["Ie", "J", "K", "L"],
            ["A", "B", "C", "D"]]
    dictionary = ["ABEF", "AFJIEB", "DGKD", "DGKA"]

    mygame = Boggle(grid, dictionary)
    print(mygame.getSolution())


if __name__ == "__main__":
    main()