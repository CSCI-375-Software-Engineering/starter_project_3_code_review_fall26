class Boggle:
    VALID_MULTI = {"qu", "st", "ie"}

    def __init__(self, grid, dictionary):
        self.grid = []
        self.dictionary = set()
        self.solutions = []
        self.setGrid(grid)
        self.setDictionary(dictionary)

    def setGrid(self, grid):
        self.grid = grid if grid is not None else []

    def setDictionary(self, dictionary):
        self.dictionary = set()
        if dictionary:
            for word in dictionary:
                if isinstance(word, str) and word.isalpha() and len(word) >= 3:
                    self.dictionary.add(word.lower())

    def _normalized_grid(self):
        """Returns a lowercase copy of the grid, or None if the grid is invalid."""
        n = len(self.grid)
        if n == 0:
            return None
        board = []
        for row in self.grid:
            if not isinstance(row, (list, tuple)) or len(row) != n:
                return None
            new_row = []
            for tile in row:
                if not isinstance(tile, str) or not tile.isalpha():
                    return None
                t = tile.lower()
                if len(t) == 1:
                    if t == "q":
                        return None
                elif t not in self.VALID_MULTI:
                    return None
                new_row.append(t)
            board.append(new_row)
        return board

    def getSolution(self):
        board = self._normalized_grid()
        if board is None or not self.dictionary:
            self.solutions = []
            return self.solutions

        prefixes = set()
        for word in self.dictionary:
            for i in range(1, len(word) + 1):
                prefixes.add(word[:i])

        n = len(board)
        found = set()
        visited = [[False] * n for _ in range(n)]

        def dfs(r, c, current):
            current += board[r][c]
            if current not in prefixes:
                return
            if len(current) >= 3 and current in self.dictionary:
                found.add(current)
            visited[r][c] = True
            for dr in (-1, 0, 1):
                for dc in (-1, 0, 1):
                    nr, nc = r + dr, c + dc
                    if (dr or dc) and 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                        dfs(nr, nc, current)
            visited[r][c] = False

        for r in range(n):
            for c in range(n):
                dfs(r, c, "")

        self.solutions = sorted(found)
        return self.solutions


def main():
    grid = [["T", "W", "Y", "R"], ["E", "N", "P", "H"], ["G", "Z", "Qu", "R"], ["O", "N", "T", "A"]]
    dictionary = ["art", "ego", "gent", "get", "net", "new", "newt", "prat", "pry", "qua", "quart", "quartz",
                  "rat", "tar", "tarp", "ten", "went", "wet", "arty", "rhr", "not", "quar"]

    mygame = Boggle(grid, dictionary)
    print(mygame.getSolution())


if __name__ == "__main__":
    main()
