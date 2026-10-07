"""
Chase Medy

Boggle Solver

Given a grid of letter tiles and a dictionary, finds every dictionary
word that can be formed by walking through adjacent tiles (including
diagonals), without reusing any tile within a single word.

Special tiles: "Qu", "St", and "Ie" each count as two letters. Words
shorter than three characters are ignored.
"""


MIN_WORD_LENGTH = 3
WORD_END = "$"
MULTI_CHAR_TILES = {"qu", "st", "ie"}
VALID_TILES = {chr(c) for c in range(ord("a"), ord("z") + 1)} | MULTI_CHAR_TILES
DIRECTIONS = tuple(
    (dr, dc) for dr in (-1, 0, 1) for dc in (-1, 0, 1) if (dr, dc) != (0, 0)
)


class Boggle:
    """Solve a Boggle board against a supplied dictionary."""

    def __init__(self, grid, dictionary):
        """Store the initial grid and dictionary, and build the trie."""
        self.grid = grid
        self.dictionary = dictionary
        self.solution = []
        self._trie = self._build_trie(dictionary)

    def setGrid(self, grid):
        """Replace the current grid and clear any cached solution."""
        self.grid = grid
        self.solution = []

    def setDictionary(self, dictionary):
        """Replace the current dictionary, rebuild the trie, and clear
        any cached solution.
        """
        self.dictionary = dictionary
        self.solution = []
        self._trie = self._build_trie(dictionary)

    def getSolution(self):
        """Return every valid word from the dictionary that appears on the
        grid. Returns an empty list when the grid or dictionary is invalid.
        """
        if not self._is_valid_input():
            self.solution = []
            return self.solution

        tiles = [[cell.lower() for cell in row] for row in self.grid]
        rows = len(tiles)
        cols = len(tiles[0])
        found = set()

        for r in range(rows):
            for c in range(cols):
                self._search(r, c, tiles, rows, cols, self._trie, "", set(), found)

        self.solution = sorted(found)
        return self.solution

    def _build_trie(self, dictionary):
        """Compile the dictionary into a trie for prefix-pruned search."""
        trie = {}
        if not isinstance(dictionary, list):
            return trie
        for word in dictionary:
            if not isinstance(word, str) or len(word) < MIN_WORD_LENGTH:
                continue
            node = trie
            for ch in word.lower():
                node = node.setdefault(ch, {})
            node[WORD_END] = True
        return trie

    def _step_through(self, node, chars):
        """Walk one tile's characters down the trie, returning the resulting
        node or None if the prefix is not in the dictionary.
        """
        for ch in chars:
            node = node.get(ch)
            if node is None:
                return None
        return node

    def _neighbors(self, r, c, rows, cols):
        """Yield the in-bounds neighbors of (r, c), including diagonals."""
        for dr, dc in DIRECTIONS:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                yield nr, nc

    def _search(self, r, c, tiles, rows, cols, node, path, visited, found):
        """Depth-first walk from (r, c), collecting completed words."""
        next_node = self._step_through(node, tiles[r][c])
        if next_node is None:
            return
        grown_path = path + tiles[r][c]
        if WORD_END in next_node and len(grown_path) >= MIN_WORD_LENGTH:
            found.add(grown_path)
        visited.add((r, c))
        for nr, nc in self._neighbors(r, c, rows, cols):
            if (nr, nc) not in visited:
                self._search(
                    nr, nc, tiles, rows, cols, next_node, grown_path, visited, found
                )
        visited.remove((r, c))

    def _is_valid_input(self):
        """Check that the grid is a non-empty rectangle of allowed tiles
        and the dictionary is a list.
        """
        if not isinstance(self.grid, list) or not self.grid:
            return False
        if not isinstance(self.dictionary, list):
            return False
        width = None
        for row in self.grid:
            if not isinstance(row, list) or not row:
                return False
            if width is None:
                width = len(row)
            elif len(row) != width:
                return False
            for cell in row:
                if not isinstance(cell, str):
                    return False
                if cell.lower() not in VALID_TILES:
                    return False
        return True


def main():
    grid = [
        ["A", "B", "C", "D"],
        ["E", "F", "G", "H"],
        ["Ie", "J", "K", "L"],
        ["A", "B", "C", "D"],
    ]
    dictionary = ["ABEF", "AFJIEB", "DGKD", "DGKA"]
    game = Boggle(grid, dictionary)
    result = game.getSolution()
    print(result)
    assert "abef" in result
    assert "afjieb" in result  # exercises the "Ie" multi-char tile
    assert "dgkd" in result
    assert "dgka" not in result  # in dictionary, but no A adjacent to K


if __name__ == "__main__":
    main()