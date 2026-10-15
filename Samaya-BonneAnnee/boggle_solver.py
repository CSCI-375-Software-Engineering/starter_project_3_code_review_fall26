#Samaya Bonne Annee
#003004137
#Code copied over from debugger after incorporating peers' review suggestions
class Boggle:
    def __init__(self, grid, dictionary):
        self.grid = grid
        self.dictionary = dictionary
        self.solutions = []

    def setGrid(self, grid):  # this allows the user to replace the grid
        self.grid = grid

    def setDictionary(self, dictionary):  # this allows the user to replace the dictionary
        self.dictionary = dictionary

    def validGrid(self):
        if len(self.grid) == 0:  # if the grid has nothing in it is invalid
            return "Invalid Grid"

        for row in self.grid:  # checking if the grid is NxN
            if len(self.grid) != len(row):  # this will help determine if the # of columns is equal to the # of rows
                return "Invalid Grid"

        for row in self.grid:  # checking if the forbidden characters are a part of the grid
            for tile in row:
                if tile.upper() == "Q" or tile.upper() == "S" or tile.upper() == "I" or tile.isdigit():
                    return "Invalid Grid"

    def sameCase(self):  # changing all the words and tiles into the same case so it's easier to check when methods are called
        newDictionary = []

        for word in self.dictionary:
            newDictionary.append(word.upper())  # changes the word to all uppercase

        self.dictionary = newDictionary

        newGrid = []

        for row in self.grid:
            newRow = []

            for tile in row:
                newRow.append(tile.upper())

            newGrid.append(newRow)

        self.grid = newGrid

    def validDictionary(self):
        for word in self.dictionary:
            for letter in word:
                if letter.isdigit():
                    return "Invalid dictionary"

    def findWord(self, word):  # searching the grid for the word using nested for loop
        visited = []

        for row in self.grid:
            newRow = []

            for column in range(len(row)):
                newRow.append(False)

            visited.append(newRow)

        for row in range(len(self.grid)):
            for column in range(len(self.grid)):
                tile = self.grid[row][column]

                if tile == word[0] or (tile in ["IE", "QU", "ST"] and word.startswith(tile)):
                    if self.search(word, row, column, 0, visited):
                        return True

        return False

    def search(self, word, row, column, index, visited):
        if index == len(word):
            return True

        if row >= len(self.grid) or row < 0 or column < 0 or column >= len(self.grid):
            return False

        if visited[row][column] == True:
            return False

        tile = self.grid[row][column]

        # testing for the special cases making sure they dont pass through
        if word[index:index + len(tile)] != tile:
            return False

        visited[row][column] = True

        nextIndex = index + len(tile)

        # checking all 8 directions around the current tile
        for dRow in (-1, 0, 1):
            for dColumn in (-1, 0, 1):

                # skips the current tile
                if dRow == 0 and dColumn == 0:
                    continue

                if self.search(
                        word,
                        row + dRow,
                        column + dColumn,
                        nextIndex,
                        visited):
                    return True

        visited[row][column] = False

        return False

    def getSolution(self):  # checks if everything is valid and if so it is appended
        self.solutions = []

        if self.validGrid() == "Invalid Grid":
            return []

        if self.validDictionary() == "Invalid dictionary":
            return []

        self.sameCase()

        for word in self.dictionary:
            if len(word) >= 3:
                if self.findWord(word):
                    self.solutions.append(word)

        return self.solutions


def main():
    grid = [["T", "W", "Y", "R"], ["E", "N", "P", "H"],
            ["G", "Z", "Qu", "R"], ["O", "N", "T", "A"]]

    dictionary = ["art", "ego", "gent", "get", "net", "new", "newt",
                  "prat", "pry", "qua", "quart", "quartz", "rat", "tar",
                  "tarp", "ten", "went", "wet", "arty", "rhr", "not",
                  "quar"]

    mygame = Boggle(grid, dictionary)
    print(mygame.getSolution())


if __name__ == "__main__":
    main()