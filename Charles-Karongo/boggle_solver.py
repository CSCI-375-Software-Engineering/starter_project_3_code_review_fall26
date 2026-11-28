"""
Charles Karongo
004002678

"""


# boggle_solver.py

class Boggle:
    def __init__(self, grid, dictionary):
        self.grid = grid
        self.dictionary = dictionary

    def setGrid(self, grid):
        self.grid = grid

    def setDictionary(self, dictionary):
        self.dictionary = dictionary

    def getSolution(self):
        if not self.grid or not self.dictionary:
            return []

        rows = len(self.grid)
        if rows == 0:
            return []
        cols = len(self.grid[0])
        if cols == 0:
            return []

        found_words = set()
        dict_set = set(word.upper() for word in self.dictionary)

        # Build prefix set to prune dead-end paths early and avoid timeouts
        prefix_set = set()
        for word in self.dictionary:
            w = word.upper()
            for i in range(1, len(w) + 1):
                prefix_set.add(w[:i])

        def dfs(r, c, visited, path):
            if path not in prefix_set:
                return

            if len(path) >= 3 and path in dict_set:
                found_words.add(path)

            directions = [
                (-1, -1), (-1, 0), (-1, 1),
                (0, -1), (0, 1),
                (1, -1), (1, 0), (1, 1)
            ]

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and (
                        nr, nc) not in visited:
                    visited.add((nr, nc))
                    letter = self.grid[nr][nc].upper()
                    dfs(nr, nc, visited, path + letter)
                    visited.remove((nr, nc))

        for r in range(rows):
            for c in range(cols):
                start_letter = self.grid[r][c].upper()
                if start_letter in prefix_set:
                    dfs(r, c, {(r, c)}, start_letter)

        return sorted(list(found_words))
