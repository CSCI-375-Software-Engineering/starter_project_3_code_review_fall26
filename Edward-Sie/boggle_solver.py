
class Boggle:
    def __init__(self, grid, dictionary):
        self.grid = grid
        self.dictionary = dictionary
        self.solutions = []

    def getSolution(self):
        self.solutions = []

        # Validate the grid and dictionary.
        if not isinstance(self.grid, list) or not isinstance(
            self.dictionary, list
        ):
            return self.solutions

        if len(self.grid) == 0 or len(self.dictionary) == 0:
            return self.solutions

        if not all(
            isinstance(row, list) and len(row) > 0
            for row in self.grid
        ):
            return self.solutions

        # Ensure the Boggle board is rectangular.
        num_cols = len(self.grid[0])

        if not all(len(row) == num_cols for row in self.grid):
            return self.solutions

        # Keep grid cells and dictionary words as strings.
        if not all(
            isinstance(cell, str) and cell != ""
            for row in self.grid
            for cell in row
        ):
            return self.solutions

        if not all(isinstance(word, str) for word in self.dictionary):
            return self.solutions

        # Convert everything to uppercase for case-insensitive lookup.
        norm_grid = [
            [cell.upper() for cell in row]
            for row in self.grid
        ]

        norm_dict = {
            word.upper()
            for word in self.dictionary
            if len(word) >= 3
        }

        if not norm_dict:
            return self.solutions

        # Build prefixes to stop DFS when a path cannot form a word.
        prefixes = set()

        for word in norm_dict:
            for i in range(1, len(word) + 1):
                prefixes.add(word[:i])

        found_words = set()
        num_rows = len(norm_grid)

        def dfs(row, col, current_word, visited):
            # DFS explores neighboring tiles to build possible words.
            # Multi-character tiles such as "Qu" and "St" are added
            # as complete strings instead of individual letters.
            tile = norm_grid[row][col]
            next_word = current_word + tile

            # Stop if the current path cannot form a dictionary word.
            if next_word not in prefixes:
                return

            # A valid Boggle word must contain at least 3 letters.
            if len(next_word) >= 3 and next_word in norm_dict:
                found_words.add(next_word)

            visited.add((row, col))

            # Explore all 8 neighboring positions.
            for dr in (-1, 0, 1):
                for dc in (-1, 0, 1):
                    if dr == 0 and dc == 0:
                        continue

                    new_row = row + dr
                    new_col = col + dc

                    if (
                        0 <= new_row < num_rows
                        and 0 <= new_col < num_cols
                        and (new_row, new_col) not in visited
                    ):
                        dfs(new_row, new_col, next_word, visited)

            visited.remove((row, col))

        # Start searching from every cell on the board.
        for row in range(num_rows):
            for col in range(num_cols):
                dfs(row, col, "", set())

        # Preserve the original spelling and capitalization.
        for word in self.dictionary:
            if word.upper() in found_words and word not in self.solutions:
                self.solutions.append(word)

        return self.solutions


def main():
    grid = [
        ["T", "W", "Y", "R"],
        ["E", "N", "P", "H"],
        ["G", "Z", "Qu", "R"],
        ["O", "N", "T", "A"]
    ]

    dictionary = [
        "art", "ego", "gent", "get", "net", "new", "newt",
        "prat", "pry", "qua", "quart", "quartz", "rat",
        "tar", "tarp", "ten", "went", "wet", "arty",
        "rhr", "not", "quar"
    ]

    mygame = Boggle(grid, dictionary)
    print(mygame.getSolution())


if __name__ == "__main__":
    main()
