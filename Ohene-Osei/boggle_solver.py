# Name: Ohene Baffoe Osei
# Student ID: 004001870
"""Solve Boggle boards using a trie and recursive backtracking."""

MIN_WORD_LENGTH = 3
END_OF_WORD = "#"


class Boggle:
    """Find dictionary words on a square Boggle board."""

    def __init__(self, grid, dictionary):
        self.grid = grid
        self.dictionary = dictionary

    def setGrid(self, grid):
        """Replace the board."""
        self.grid = grid

    def setDictionary(self, dictionary):
        """Replace the dictionary."""
        self.dictionary = dictionary

    def validGrid(self):
        """Check that the board is a nonempty square of string tiles."""
        if not isinstance(self.grid, list) or not self.grid:
            return False

        size = len(self.grid)

        for row in self.grid:
            if not isinstance(row, list) or len(row) != size:
                return False

            for tile in row:
                if not isinstance(tile, str) or not tile:
                    return False

        return True

    def validateDictionary(self):
        """Check that the dictionary is a list of strings."""
        if not isinstance(self.dictionary, list):
            return False

        for word in self.dictionary:
            if not isinstance(word, str):
                return False

        return True

    def buildTrie(self):
        """Build a trie of words meeting the minimum length."""
        trie = {}

        for word in self.dictionary:
            if len(word) < MIN_WORD_LENGTH:
                continue

            current = trie
            normalized_word = word.lower()

            for letter in normalized_word:
                if letter not in current:
                    current[letter] = {}

                current = current[letter]

            # Mark where a complete dictionary word ends.
            current[END_OF_WORD] = normalized_word

        return trie

    def moveThroughTile(self, node, tile):
        """Follow every letter of a tile through the trie."""
        current = node

        # Qu, St, and Ie contain multiple letters but occupy one tile.
        for letter in tile.lower():
            if letter not in current:
                return None

            current = current[letter]

        return current

    def search_from_tile(self, row, col, node, visited, found):
        """Search neighboring tiles without reusing a tile in one path."""
        if visited[row][col]:
            return

        tile = self.grid[row][col]
        next_node = self.moveThroughTile(node, tile)

        # Stop if this path is not a dictionary prefix.
        if next_node is None:
            return

        visited[row][col] = True

        if END_OF_WORD in next_node:
            found.add(next_node[END_OF_WORD])

        size = len(self.grid)

        # Explore all eight neighbors, including diagonals.
        for row_change in range(-1, 2):
            for col_change in range(-1, 2):
                if row_change == 0 and col_change == 0:
                    continue

                new_row = row + row_change
                new_col = col + col_change

                if (
                    0 <= new_row < size
                    and 0 <= new_col < size
                    and not visited[new_row][new_col]
                ):
                    self.search_from_tile(
                        new_row,
                        new_col,
                        next_node,
                        visited,
                        found,
                    )

        # Release this tile so another search path can use it.
        visited[row][col] = False

    def getSolution(self):
        """Return unique matches in dictionary order and original case."""
        solutions = []

        if not self.validGrid() or not self.validateDictionary():
            return solutions

        trie = self.buildTrie()

        if not trie:
            return solutions

        size = len(self.grid)
        visited = [[False] * size for _ in range(size)]
        found = set()

        for row in range(size):
            for col in range(size):
                self.search_from_tile(
                    row,
                    col,
                    trie,
                    visited,
                    found,
                )

        added = set()

        # Preserve dictionary order and the first matching capitalization.
        for word in self.dictionary:
            normalized_word = word.lower()

            if (
                len(word) >= MIN_WORD_LENGTH
                and normalized_word in found
                and normalized_word not in added
            ):
                solutions.append(word)
                added.add(normalized_word)

        return solutions


def main():
    """Run the solver on an example board."""
    grid = [
        ["T", "W", "Y", "R"],
        ["E", "N", "P", "H"],
        ["G", "Z", "Qu", "R"],
        ["O", "N", "T", "A"],
    ]
    dictionary = [
        "art", "ego", "gent", "get", "net", "new", "newt",
        "prat", "pry", "qua", "quart", "quartz", "rat", "tar",
        "tarp", "ten", "went", "wet", "arty", "rhr", "not", "quar",
    ]

    game = Boggle(grid, dictionary)
    print(game.getSolution())


if __name__ == "__main__":
    main()
