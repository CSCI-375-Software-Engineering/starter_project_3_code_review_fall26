"""
Name: Jillian Drake
SID: 004001582
"""


class Boggle:
    """
    Represents a single game of Boggle.

    Data members:
        grid       - 2D list of uppercase strings, one tile per cell.
        dictionary - set of uppercase valid words to search for.
        solution   - list of words found in the grid so far.
        valid      - False if the grid or dictionary failed validation.
    """

    # The 8 (row, col) offsets for a tile's neighbors: up/down/left/right
    # and all 4 diagonals, since Boggle allows diagonal moves.
    _directions = [(-1, -1), (-1, 0), (-1, 1),
                   (0, -1),           (0, 1),
                   (1, -1),  (1, 0),  (1, 1)]

    def __init__(self, grid, dictionary):
        """
        Constructor. Sets safe default values first, then validates and
        stores the grid and dictionary via the setter methods below.
        """
        self.grid = []          # 2D list of strings representing the Boggle grid
        self.dictionary = set()  # Set of valid words from the dictionary
        self.solution = []      # List of words found in the grid that are in the dictionary
        self.valid = True       # Flag to indicate if the grid and dictionary are valid

        self.setGrid(grid)
        self.setDictionary(dictionary)

    def setGrid(self, grid):
        """
        Validate and store the game grid.

        A valid grid is a non-empty list of lists, where every row has the
        same length and every cell is a string. All tiles are uppercased
        on the way in so comparisons later don't have to worry about case.
        Sets self.valid = False and returns early on any invalid input.
        """
        if not isinstance(grid, list) or len(grid) == 0:
            self.valid = False
            return

        row_length = len(grid[0])
        for row in grid:
            if not isinstance(row, list) or len(row) != row_length:
                self.valid = False
                return
            for cell in row:
                if not isinstance(cell, str):
                    self.valid = False
                    return

        self.grid = [[cell.upper() for cell in row] for row in grid]

    def setDictionary(self, dictionary):
        """
        Validate and store the word dictionary.

        A valid dictionary is a list of strings. Words are uppercased and
        stored as a set for fast exact-match lookups in _search.
        Sets self.valid = False and returns early on any invalid input.
        """
        if not isinstance(dictionary, list):
            self.valid = False
            return

        for word in dictionary:
            if not isinstance(word, str):
                self.valid = False
                return

        self.dictionary = {word.upper() for word in dictionary}

    def getSolution(self):
        """
        Search the grid for every dictionary word and return the results.

        Returns an empty list immediately if the grid or dictionary
        failed validation. Otherwise, tries starting a search from every
        cell in the grid and returns whatever words were found, sorted
        alphabetically with no duplicates (the same word may be
        reachable via more than one path through the grid, but should
        only be reported once).
        """
        if not self.valid:
            return []

        for row in range(len(self.grid)):
            for col in range(len(self.grid[row])):
                # Try starting a word from every cell in the grid.
                self._search("", row, col, set())

        self.solution.sort()   # match expected alphabetical ordering
        return self.solution

    def _in_bounds(self, row, col):
        """Return True if (row, col) is a real cell inside the grid."""
        return 0 <= row < len(self.grid) and 0 <= col < len(self.grid[0])

    def _is_prefix(self, word):
        """
        Return True if `word` is a prefix of at least one dictionary word
        (or matches one exactly). Used to stop searching down paths that
        can never lead to a valid word, since the dictionary here isn't
        stored in a structure (like a trie) that supports prefix lookups
        directly.
        """
        for dict_word in self.dictionary:
            if dict_word.startswith(word):
                return True
        return False

    def _search(self, word_so_far, row, col, visited):
        """
        Recursively extend a word by one tile at (row, col) and try every
        unvisited neighbor from there.

        word_so_far - the word built so far, not including this tile.
        visited     - set of (row, col) cells already used in this path.

        If the extended word is a complete dictionary word of at least
        3 letters, it's added to the solution. If the extended word isn't
        even a prefix of any dictionary word, the search stops here rather
        than exploring neighbors that can't possibly lead anywhere.

        `visited` is combined with the current cell using set union (|)
        rather than being mutated in place, so each recursive call gets
        its own copy - this avoids having to manually "undo" the visit
        when backtracking.
        """
        tile = self.grid[row][col]
        # Uppercasing at storage time means we can safely combine tiles
        # like "Qu" or "St" into the word without extra case-handling here.
        new_word = word_so_far + tile

        if not self._is_prefix(new_word):
            return  # dead end, stop exploring this path

        if len(new_word) >= 3 and new_word in self.dictionary:
            # A word can be reachable via more than one path through the
            # grid; only record it the first time so getSolution()
            # returns each word once, not once per path.
            if new_word not in self.solution:
                self.solution.append(new_word)

        # Union (not mutation) - gives this recursive branch its own
        # snapshot of visited cells, so sibling branches aren't affected.
        new_visited = visited | {(row, col)}

        for dr, dc in self._directions:
            nr, nc = row + dr, col + dc
            if self._in_bounds(nr, nc) and (nr, nc) not in new_visited:
                self._search(new_word, nr, nc, new_visited)


def main():
    """Build a sample Boggle game and print every word found in it."""
    grid = [["T", "W", "Y", "R"],
            ["E", "N", "P", "H"],
            ["G", "St", "Qu", "R"],
            ["O", "N", "T", "A"]]

    dictionary = ["art", "ego", "gent", "get", "net", "new", "newt",
                  "prat", "pry", "qua", "quart", "rat", "tar", "tarp",
                  "ten", "went", "wet"]

    mygame = Boggle(grid, dictionary)
    print(mygame.getSolution())


if __name__ == "__main__":
    main()