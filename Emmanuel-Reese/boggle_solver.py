class Boggle:
    """
    Finds all dictionary words that can be traced on a Boggle grid.

    Attributes:
        grid: Validated 2D list of tile strings, or None if invalid.
        dictionary: Lowercased, de-duplicated list of words with at
            least 3 letters, or None if the input was invalid.
        solution: List of found words from the last getSolution() call.
        rows: Number of grid rows (read-only property).
        cols: Number of grid columns (read-only property).

    Usage:
        game = Boggle(grid, dictionary)
        words = game.getSolution()
    """

    # All 8 directions (row offset, column offset) around a cell.
    _OFFSETS = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1), (0, 1),
        (1, -1), (1, 0), (1, 1),
    ]

    def __init__(self, grid, dictionary):
        self.grid = None
        self.dictionary = None
        self.solution = []
        self._rows = 0
        self._cols = 0
        self._trie = None
        self.setGrid(grid)
        self.setDictionary(dictionary)

    @property
    def rows(self):
        """Number of rows in the grid (0 if the grid is invalid)."""
        return self._rows

    @property
    def cols(self):
        """Number of columns in the grid (0 if the grid is invalid)."""
        return self._cols

    def _reset_grid(self):
        """Marks the grid as invalid and clears its dimensions."""
        self.grid = None
        self._rows = 0
        self._cols = 0

    @staticmethod
    def _is_blank(value):
        """True if value is not a string or has no visible characters."""
        return not isinstance(value, str) or len(value.strip()) == 0

    def setGrid(self, grid):
        """
        Validates and stores the grid.

        Requirements:
          - grid is a non-empty list
          - every row is a non-empty list
          - every row has the same length
          - every cell is a non-blank string (whitespace-only is rejected)
        On failure, self.grid is set to None.
        """
        # Reject anything that isn't a non-empty list.
        if not isinstance(grid, list) or len(grid) == 0:
            self._reset_grid()
            return

        row_len = None
        for row in grid:
            # Each row must be a non-empty list.
            if not isinstance(row, list) or len(row) == 0:
                self._reset_grid()
                return
            if row_len is None:
                # The first row sets the expected width.
                row_len = len(row)
            elif len(row) != row_len:
                # Every later row must match that width (rectangular).
                self._reset_grid()
                return
            for cell in row:
                # Every tile must be a real, non-blank string.
                if self._is_blank(cell):
                    self._reset_grid()
                    return

        # Grid passed all checks, so store it.
        self.grid = grid
        self._rows = len(grid)
        self._cols = row_len

    def setDictionary(self, dictionary):
        """
        Validates, normalizes, and stores the dictionary, then builds
        the trie used by the search.

        Requirements:
          - dictionary is a non-empty list
          - every entry is a non-blank string
        Words are lowercased, duplicates are removed, and words shorter
        than 3 letters are dropped because they can never be valid.
        The result may be an empty list (for example, if every word was
        too short). That is allowed here, but _is_valid() treats it as
        unsolvable because there is nothing to search for.
        On failure, self.dictionary is set to None.
        """
        # Reject anything that isn't a non-empty list.
        if not isinstance(dictionary, list) or len(dictionary) == 0:
            self.dictionary = None
            self._trie = None
            return

        normalized = []
        seen = set()
        for word in dictionary:
            # Every word must be a real, non-blank string.
            if self._is_blank(word):
                self.dictionary = None
                self._trie = None
                return
            # Lowercase so matching is case-insensitive.
            lowered = word.lower()
            # Skip words under 3 letters and duplicates.
            if len(lowered) >= 3 and lowered not in seen:
                seen.add(lowered)
                normalized.append(lowered)

        self.dictionary = normalized
        self._trie = self._build_trie(normalized)

    @staticmethod
    def _build_trie(words):
        """
        Builds a nested-dict trie for fast prefix pruning.

        Expects words that are already validated and normalized by
        setDictionary() (lowercase, 3+ letters, no duplicates).
        '$' marks the end of a complete word.
        """
        trie = {}
        for word in words:
            node = trie
            for ch in word:
                if ch not in node:
                    # Create a branch for this letter if missing.
                    node[ch] = {}
                node = node[ch]
            # Mark the end of a complete word.
            node['$'] = True
        return trie

    def _is_valid(self):
        """
        True only if the grid is valid, the dictionary is valid, and the
        normalized dictionary contains at least one word.
        """
        if self.grid is None or self.dictionary is None:
            return False
        return len(self.dictionary) > 0

    def _neighbors(self, r, c):
        """Yields all adjacent cells, skipping any that are off the grid."""
        for dr, dc in self._OFFSETS:
            nr, nc = r + dr, c + dc
            if 0 <= nr < self._rows and 0 <= nc < self._cols:
                yield nr, nc

    def _dfs(self, r, c, node, visited, path, found):
        """
        Depth-first search from cell (r, c), following the trie.

        node: trie node reached before this tile.
        visited: set of cells on the current path (no cell reused).
        path: list of tile strings on the current path.
        found: set that collects completed words.
        """
        tile = self.grid[r][c].lower()
        # Walk the trie one character at a time for this tile's letters.
        # If there is no matching branch, this path can never lead to a
        # dictionary word, so prune immediately.
        current_node = node
        for ch in tile:
            if ch not in current_node:
                return
            current_node = current_node[ch]

        # Extend the path. A list avoids building a new string per step.
        path.append(tile)
        visited.add((r, c))

        if '$' in current_node:
            found.add("".join(path))

        for nr, nc in self._neighbors(r, c):
            if (nr, nc) not in visited:
                self._dfs(nr, nc, current_node, visited, path, found)

        # Backtrack: un-mark this cell and drop its tile so other paths
        # can reuse the cell.
        visited.remove((r, c))
        path.pop()

    def getSolution(self):
        """
        Returns a sorted list of found words, or an empty list if no
        words were found or the grid/dictionary are invalid.
        """
        self.solution = []

        if not self._is_valid():
            return self.solution

        found = set()
        visited = set()

        for r in range(self._rows):
            for c in range(self._cols):
                self._dfs(r, c, self._trie, visited, [], found)

        self.solution = sorted(found)
        return self.solution


def main():
    grid = [
        ["T", "W", "Y", "R"],
        ["E", "N", "P", "H"],
        ["G", "Z", "Qu", "R"],
        ["O", "N", "T", "A"],
    ]
    dictionary = [
        "art", "ego", "gent", "get", "net", "new", "newt", "prat",
        "pry", "qua", "quart", "quartz", "rat", "tar", "tarp", "ten",
        "went", "wet", "arty", "rhr", "not", "quar",
    ]
    mygame = Boggle(grid, dictionary)
    print(mygame.getSolution())


if __name__ == "__main__":
    main()