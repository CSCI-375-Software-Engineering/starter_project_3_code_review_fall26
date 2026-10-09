"""Boggle solver that uses a trie to find every valid word in a grid."""

# Words shorter than this do not count as solutions.
MIN_WORD_LENGTH = 3

# Marks the end of a complete word inside the trie.
END_OF_WORD = "$"

# The eight neighbors of a tile as (row change, column change).
DIRECTIONS = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1), (0, 1),
    (1, -1), (1, 0), (1, 1),
]


class Boggle:
    """Finds all dictionary words that can be traced through a grid."""

    def __init__(self, grid, dictionary):
        self.grid = grid
        self.dictionary = dictionary
        self.solutions = []
        self.trie = {}

    def validate_grid(self, grid):
        """Return True if grid is a non-empty rectangle of strings."""
        if not grid:
            return False
        row_length = None
        for row in grid:
            if not row:
                return False
            if row_length is None:
                row_length = len(row)
            elif len(row) != row_length:
                return False
            for tile in row:
                if not isinstance(tile, str) or not tile:
                    return False
        return True

    def validate_dict(self, dictionary):
        """Return True if dictionary is a non-empty collection of strings."""
        if not dictionary:
            return False
        for word in dictionary:
            if not isinstance(word, str) or not word:
                return False
        return True

    def build_trie(self, dictionary):
        """Build a nested-dict trie from the words in dictionary."""
        root = {}
        for word in dictionary:
            node = root
            for letter in word.upper():
                if letter not in node:
                    node[letter] = {}
                node = node[letter]
            node[END_OF_WORD] = True
        return root

    def find_words(self, prefix, row, col, grid, visited, node, found):
        """Extend the current path into the tile at (row, col).

        prefix is the word built so far along this path, visited holds the
        tiles already used on this path, node is where the path sits in the
        trie, and found collects every complete word.
        """
        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
            return
        if (row, col) in visited:
            return

        # Walk the tile's letters through the trie one character at a time.
        # A tile like "Qu" uses two trie levels in a single move.
        current = node
        for letter in grid[row][col].upper():
            if letter not in current:
                return
            current = current[letter]

        prefix = prefix + grid[row][col]
        visited.add((row, col))

        if (END_OF_WORD in current and len(prefix) >= MIN_WORD_LENGTH
                and prefix not in found):
            found.append(prefix)

        for d_row, d_col in DIRECTIONS:
            self.find_words(prefix, row + d_row, col + d_col, grid, visited,
                            current, found)

        # Backtrack so other paths can reuse this tile.
        visited.remove((row, col))

    def getSolution(self):
        """Return the list of words found in the grid."""
        if not (self.validate_grid(self.grid)
                and self.validate_dict(self.dictionary)):
            return self.solutions

        self.trie = self.build_trie(self.dictionary)

        for row in range(len(self.grid)):
            for col in range(len(self.grid[0])):
                self.find_words("", row, col, self.grid, set(), self.trie,
                                self.solutions)

        return self.solutions


def main():
    grid = [["T", "W", "Y", "R"],
            ["E", "N", "P", "H"],
            ["G", "Z", "Qu", "R"],
            ["O", "N", "T", "A"]]
    dictionary = ["art", "ego", "gent", "get", "net", "new", "newt", "prat",
                  "pry", "qua", "quart", "quartz", "rat", "tar", "tarp",
                  "ten", "went", "wet", "arty", "rhr", "not", "quar"]

    mygame = Boggle(grid, dictionary)
    print(mygame.getSolution())


if __name__ == "__main__":
    main()