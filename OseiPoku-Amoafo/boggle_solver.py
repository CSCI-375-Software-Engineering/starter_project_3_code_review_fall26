class Boggle:
    def __init__(self, grid, dictionary):
        self.grid = grid
        self.dictionary = dictionary
        self.solutions = []

    def setGrid(self, grid):  # replace the grid
        self.grid = grid

    def setDictionary(self, dictionary):  # replace the dictionary
        self.dictionary = dictionary

    def validGrid(self):
        if len(self.grid) == 0:  # an empty grid is invalid
            return "Invalid Grid"
        for row in self.grid:  # grid must be NxN
            if len(self.grid) != len(row):
                return "Invalid Grid"
        for row in self.grid:  # no forbidden single-letter tiles or digits
            for tile in row:
                if tile.upper() in ("Q", "S", "I") or tile.isdigit():
                    return "Invalid Grid"

    def sameCase(self):  # uppercase everything so comparisons are simple
        self.dictionary = [word.upper() for word in self.dictionary]
        self.grid = [[tile.upper() for tile in row] for row in self.grid]

    def validDictionary(self):
        for word in self.dictionary:
            for letter in word:
                if letter.isdigit():
                    return "Invalid dictionary"

    def findWord(self, word):
        size = len(self.grid)
        visited = [[False] * size for _ in range(size)]
        for row in range(size):
            for column in range(size):
                if self.search(word, row, column, 0, visited):
                    return True
        return False

    def search(self, word, row, column, index, visited):
        if index == len(word):
            return True
        size = len(self.grid)
        if row < 0 or row >= size or column < 0 or column >= size:
            return False
        if visited[row][column]:
            return False

        tile = self.grid[row][column]  # may be 1 letter or "IE"/"QU"/"ST"
        if word[index:index + len(tile)] != tile:
            return False

        visited[row][column] = True
        nextIndex = index + len(tile)
        for dRow in (-1, 0, 1):
            for dColumn in (-1, 0, 1):
                if dRow == 0 and dColumn == 0:
                    continue
                if self.search(word, row + dRow, column + dColumn,
                               nextIndex, visited):
                    return True
        visited[row][column] = False
        return False

    def getSolution(self):
        self.solutions = []
        if self.validGrid() == "Invalid Grid":
            return []
        if self.validDictionary() == "Invalid dictionary":
            return []
        self.sameCase()
        for word in self.dictionary:
            if len(word) >= 3 and word not in self.solutions:
                if self.findWord(word):
                    self.solutions.append(word)
        return self.solutions


def main():
    grid = [["T", "W", "Y", "R"], ["E", "N", "P", "H"],
            ["G", "Z", "Qu", "R"], ["O", "N", "T", "A"]]
    dictionary = ["art", "ego", "gent", "get", "net", "new", "newt", "prat",
                  "pry", "qua", "quart", "quartz", "rat", "tar", "tarp",
                  "ten", "went", "wet", "arty", "rhr", "not", "quar"]

    mygame = Boggle(grid, dictionary)
    print(mygame.getSolution())


if __name__ == "__main__":
    main()