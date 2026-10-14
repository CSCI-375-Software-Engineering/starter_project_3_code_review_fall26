"""Find dictionary words in a Boggle grid."""


class Boggle:
    """Solve a square Boggle board against a supplied dictionary."""

    VALID_MULTI = {"qu", "st", "ie"}

    def __init__(self, grid, dictionary):
        self.grid = []
        self.dictionary = set()
        self.solutions = []
        self.set_grid(grid)
        self.set_dictionary(dictionary)

    def set_grid(self, grid):
        """Set the board, using an empty list when no grid is provided."""
        self.grid = grid if grid is not None else []

    def set_dictionary(self, dictionary):
        """Keep alphabetic dictionary words of at least three letters."""
        self.dictionary = set()
        if dictionary:
            for word in dictionary:
                if (
                    isinstance(word, str)
                    and word.isalpha()
                    and len(word) >= 3
                ):
                    self.dictionary.add(word.lower())

    def _normalized_grid(self):
        """Return a lowercase copy of the grid, or None if it is invalid."""
        size = len(self.grid)
        if size == 0:
            return None

        board = []
        for row in self.grid:
            if not isinstance(row, (list, tuple)) or len(row) != size:
                return None

            normalized_row = []
            for tile in row:
                if not isinstance(tile, str) or not tile.isalpha():
                    return None

                normalized_tile = tile.lower()
                if len(normalized_tile) == 1:
                    # A single q is not allowed; use the "Qu" tile instead.
                    if normalized_tile == "q":
                        return None
                elif normalized_tile not in self.VALID_MULTI:
                    return None

                normalized_row.append(normalized_tile)
            board.append(normalized_row)

        return board

    def get_solution(self):
        """Return all dictionary words that can be formed on the board."""
        board = self._normalized_grid()
        if board is None or not self.dictionary:
            self.solutions = []
            return self.solutions

        # Prefix pruning stops a search as soon as it cannot match any word.
        prefixes = set()
        for word in self.dictionary:
            for end in range(1, len(word) + 1):
                prefixes.add(word[:end])

        size = len(board)
        found = set()
        visited = [[False] * size for _ in range(size)]

        def search(row, column, current):
            current += board[row][column]
            if current not in prefixes:
                return

            if len(current) >= 3 and current in self.dictionary:
                found.add(current)

            visited[row][column] = True
            for row_delta in (-1, 0, 1):
                for column_delta in (-1, 0, 1):
                    next_row = row + row_delta
                    next_column = column + column_delta
                    in_bounds = (
                        0 <= next_row < size
                        and 0 <= next_column < size
                    )
                    if (
                        (row_delta or column_delta)
                        and in_bounds
                        and not visited[next_row][next_column]
                    ):
                        search(next_row, next_column, current)

            # Allow this tile to be used by a different search path.
            visited[row][column] = False

        for row in range(size):
            for column in range(size):
                search(row, column, "")

        self.solutions = sorted(found)
        return self.solutions


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

    game = Boggle(grid, dictionary)
    print(game.get_solution())


if __name__ == "__main__":
    main()
