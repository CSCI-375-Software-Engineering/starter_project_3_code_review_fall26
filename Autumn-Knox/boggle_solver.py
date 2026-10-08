class Boggle:
    def __init__(self, grid, dictionary):
        self.grid = grid
        self.dictionary = dictionary
        self.solutions = []

    def getSolution(self):
        self.solutions = []

        if not self.grid or not self.dictionary:
            return self.solutions

        for word in self.dictionary:
            word = word.lower()

            # Boggle words must contain at least 3 letters
            if len(word) < 3:
                continue

            found = False

            for row in range(len(self.grid)):
                for col in range(len(self.grid[row])):
                    if self.search(word, row, col, 0, set()):
                        found = True
                        break

                if found:
                    break

            if found and word not in self.solutions:
                self.solutions.append(word)

        return self.solutions

    def search(self, word, row, col, index, visited):

        # Check row boundaries
        if row < 0 or row >= len(self.grid):
            return False

        # Check column boundaries
        if col < 0 or col >= len(self.grid[row]):
            return False

        # Do not reuse a tile
        if (row, col) in visited:
            return False

        tile = str(self.grid[row][col]).lower()

        # Check if the tile matches the next part of the word
        # This supports Qu, St, and Ie tiles
        if not word[index:].startswith(tile):
            return False

        new_index = index + len(tile)

        # Entire word has been matched
        if new_index == len(word):
            return True

        visited.add((row, col))

        # All 8 possible neighboring directions
        directions = [
            (-1, -1),
            (-1, 0),
            (-1, 1),
            (0, -1),
            (0, 1),
            (1, -1),
            (1, 0),
            (1, 1)
        ]

        for row_change, col_change in directions:
            new_row = row + row_change
            new_col = col + col_change

            if self.search(
                word,
                new_row,
                new_col,
                new_index,
                visited
            ):
                visited.remove((row, col))
                return True

        visited.remove((row, col))
        return False


def main():
    grid = [
        ["T", "W", "Y", "R"],
        ["E", "N", "P", "H"],
        ["G", "Z", "Qu", "R"],
        ["O", "N", "T", "A"]
    ]

    dictionary = [
        "art",
        "ego",
        "gent",
        "get",
        "net",
        "new",
        "newt",
        "prat",
        "pry",
        "qua",
        "quart",
        "quartz",
        "rat",
        "tar",
        "tarp",
        "ten",
        "went",
        "wet",
        "arty",
        "rhr",
        "not",
        "quar"
    ]

    mygame = Boggle(grid, dictionary)
    print(mygame.getSolution())


if __name__ == "__main__":
    main()
