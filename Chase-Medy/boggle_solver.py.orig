"""
Chase Medy

Boggle Solver

Given a grid of letter tiles and a dictionary, finds every dictionary
word that can be formed by walking through adjacent tiles (including
diagonals), without reusing any tile within a single word.

Special tiles: "Qu", "St", and "Ie" each count as two letters. Words
shorter than three characters are ignored.
"""


class Boggle:
    """Solve a Boggle board against a supplied dictionary."""

    def __init__(self, grid, dictionary):
        """Store the initial grid and dictionary."""
        self.grid = grid
        self.dictionary = dictionary
        self.solution = []

    def setGrid(self, grid):
        """Replace the current grid."""
        self.grid = grid

    def setDictionary(self, dictionary):
        """Replace the current dictionary."""
        self.dictionary = dictionary

    def getSolution(self):
        """Return every valid word from the dictionary that appears on the
        grid. Returns an empty list when the grid or dictionary is invalid.
        """
        if not self._isValidInput():
            self.solution = []
            return self.solution

        tiles = [[cell.lower() for cell in row] for row in self.grid]
        words = [w.lower() for w in self.dictionary
                 if isinstance(w, str) and len(w) >= 3]

        tree = {}
        for word in words:
            node = tree
            for ch in word:
                node = node.setdefault(ch, {})
            node["$"] = True

        rows = len(tiles)
        cols = len(tiles[0])
        found = set()

        def stepThrough(node, chars):
            for ch in chars:
                node = node.get(ch)
                if node is None:
                    return None
            return node

        def neighbors(r, c):
            for dr in (-1, 0, 1):
                for dc in (-1, 0, 1):
                    if dr == 0 and dc == 0:
                        continue
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols:
                        yield nr, nc

        def search(r, c, node, path, visited):
            nextNode = stepThrough(node, tiles[r][c])
            if nextNode is None:
                return
            grownPath = path + tiles[r][c]
            if "$" in nextNode and len(grownPath) >= 3:
                found.add(grownPath)
            visited.add((r, c))
            for nr, nc in neighbors(r, c):
                if (nr, nc) not in visited:
                    search(nr, nc, nextNode, grownPath, visited)
            visited.remove((r, c))

        for r in range(rows):
            for c in range(cols):
                search(r, c, tree, "", set())

        self.solution = sorted(found)
        return self.solution

    def _isValidInput(self):
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
                if not isinstance(cell, str) or not cell.isalpha():
                    return False
        return True


def main():
    grid = [["A", "B", "C", "D"],
            ["E", "F", "G", "H"],
            ["Ie", "J", "K", "L"],
            ["A", "B", "C", "D"]]
    dictionary = ["ABEF", "AFJIEB", "DGKD", "DGKA"]
    mygame = Boggle(grid, dictionary)
    print(mygame.getSolution())


if __name__ == "__main__":
    main()