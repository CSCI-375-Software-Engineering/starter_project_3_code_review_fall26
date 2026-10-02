"""Boggle solver by Xiomara Strayhorn.

Find dictionary words using adjacent tiles without reusing a cell. Qu, St,
and Ie are whole tiles; word length is measured in letters, not tiles.
Only Python's built-in types are used.
"""


class Boggle:
    """Store a board and dictionary and find their matching words."""

    def __init__(self, grid, dictionary):
        self.solution = []
        self.setGrid(grid)
        self.setDictionary(dictionary)

    def setGrid(self, grid):
        """Replace the board and discard any previous result."""
        self.grid = grid
        self.solution = []

    def setDictionary(self, dictionary):
        """Replace the candidate words and discard any previous result."""
        self.dictionary = dictionary
        self.solution = []

    def _valid_inputs(self):
        """Reject malformed boards or dictionaries without raising errors."""
        if not isinstance(self.grid, list) or not self.grid:
            return False
        if not isinstance(self.grid[0], list) or not self.grid[0]:
            return False
        width = len(self.grid[0])
        for row in self.grid:
            if not isinstance(row, list) or len(row) != width:
                return False
            for tile in row:
                if not isinstance(tile, str):
                    return False
                token = tile.lower()
                if not (len(token) == 1 and 'a' <= token <= 'z'):
                    if token not in ('qu', 'st', 'ie'):
                        return False
        return isinstance(self.dictionary, (list, tuple)) and all(
            isinstance(word, str) for word in self.dictionary
        )

    def getSolution(self):
        """Return each matching word once; return [] for invalid inputs.

        A trie shares dictionary prefixes, so a board path is abandoned as
        soon as it cannot form any candidate. Results retain the spelling of
        the first dictionary entry; callers need not rely on their order.
        """
        self.solution = []
        if not self._valid_inputs():
            return self.solution

        board = [[tile.lower() for tile in row] for row in self.grid]
        rows, columns = len(board), len(board[0])
        capacity = sum(len(tile) for row in board for tile in row)
        words = {}
        trie = {}
        for word in self.dictionary:
            key = word.lower()
            if not 3 <= len(key) <= capacity:
                continue
            if not all('a' <= letter <= 'z' for letter in key):
                continue
            if key in words:
                continue
            words[key] = word
            node = trie
            for letter in key:
                node = node.setdefault(letter, {})
            node[None] = key

        found = set()
        visited = set()

        def search(row, column, node):
            """Consume a whole tile, then try its unused neighbors."""
            for letter in board[row][column]:
                node = node.get(letter)
                if node is None:
                    return
            word = node.get(None)
            if word is not None:
                found.add(word)
            visited.add((row, column))
            for next_row in range(max(0, row - 1), min(rows, row + 2)):
                for next_column in range(max(0, column - 1),
                                         min(columns, column + 2)):
                    if (next_row, next_column) not in visited:
                        search(next_row, next_column, node)
            visited.remove((row, column))

        for row in range(rows):
            for column in range(columns):
                search(row, column, trie)
        self.solution = [spelling for key, spelling in words.items()
                         if key in found]
        return self.solution

    def findAllSolutions(self):
        """Provide the alternative method name used in the rubric."""
        return self.getSolution()


def main():
    """Run the sample board from the assignment."""
    grid = [["T", "W", "Y", "R"], ["E", "N", "P", "H"],
            ["G", "St", "Qu", "R"], ["O", "N", "T", "A"]]
    dictionary = ["art", "ego", "gent", "get", "net", "new", "newt",
                  "prat", "pry", "qua", "quart", "rat", "tar", "tarp",
                  "ten", "went", "wet", "stont", "stqura", "arty", "egg", "not"]
    print(Boggle(grid, dictionary).getSolution())


if __name__ == "__main__":
    main()
