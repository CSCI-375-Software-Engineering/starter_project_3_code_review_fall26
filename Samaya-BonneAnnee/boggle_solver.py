#Samaya Bonne Annee
#004003137

class Boggle:
    def __init__(self, grid, dictionary):
        self.grid = grid
        self.dictionary = dictionary
        self.solutions = []

    def setGrid(self, grid): #this allows the user to replace the grid
      self.grid = grid

    def setDictionary(self, dictionary): #this allows the user to replace the dictionary
      self.dictionary = dictionary

    def validGrid(self):
      if len(self.grid) == 0: #if the grid has nothing in it is invalid
          return "Invalid Grid"
      for row in self.grid: #checking if the grid is NxN
        if len(self.grid) != len(row): #this will help determine if the # of columns is equal to the # of rows
          return "Invalid Grid"
      for row in self.grid: #checking if the forbidden characters are a part of the grid
        for tile in row:
          if tile.upper() == "Q" or tile.upper() == "S" or tile.upper() == "I" or tile.isdigit():
            return "Invalid Grid"

    def sameCase(self): #changing all the words and tiles into the same case so it's easier to check when methods are called
      newDictionary = []

      for word in self.dictionary:
        newDictionary.append(word.upper()) #changes the word to all uppercase

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
    
    def findWord(self, word):#searching the grid for the word using nested for loop
      lookedAtWords = []
      for row in self.grid:
        newRow = []
        for column in range(len(row)):
          newRow.append(False)
        lookedAtWords.append(newRow)

      for row in range(len(self.grid)):
        for column in range(len(self.grid)):
          tile = self.grid[row][column]

          if tile == word[0] or (tile in ["IE", "QU", "ST"] and word.startswith(tile)):
            if self.search(word, row, column, 0, lookedAtWords):
              return True

      return False
    
    def search(self, word, row, column, index, lookedAtWords): 
      if index == len(word):
        return True

      if row >= len(self.grid) or row < 0 or column < 0 or column >= len(self.grid):
        return False
        

      if lookedAtWords[row][column] == True:
        return False
      
      if self.grid[row][column] == "IE" or self.grid[row][column] == "QU" or self.grid[row][column] == "ST": #testing for the special cases making sure they dont pass through
        if word[index:index+2] != self.grid[row][column]:
          return False
      else:
        if self.grid[row][column] != word[index]:
          return False
      lookedAtWords[row][column] = True
      if self.grid[row][column] == "IE" or self.grid[row][column] == "QU" or self.grid[row][column] == "ST":
        nextIndex = index + 2
      else:
        nextIndex = index + 1

      if self.search(word, row - 1, column, nextIndex, lookedAtWords):  #goes up
        return True
      if self.search(word, row + 1, column, nextIndex, lookedAtWords):#goes down
        return True
      if self.search(word, row, column - 1, nextIndex, lookedAtWords):#goes left
        return True
      if self.search(word, row, column + 1, nextIndex, lookedAtWords): #goes right
        return True
      if self.search(word, row - 1, column + 1, nextIndex, lookedAtWords): #so this would be upper right if you put it together
        return True
      if self.search(word, row + 1, column + 1, nextIndex, lookedAtWords): #this would be lower right
        return True
      if self.search(word, row + 1, column - 1, nextIndex, lookedAtWords): #lower left
        return True
      if self.search(word, row - 1, column - 1, nextIndex, lookedAtWords): #upper left
        return True
      lookedAtWords[row][column] = False
      return False
    
    def getSolution(self): #checks if everything is valid and if so it is appended 
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
    grid = [["T", "W", "Y", "R"], ["E", "N", "P", "H"],["G", "Z", "Qu", "R"],["O", "N", "T", "A"]]
    dictionary = ["art", "ego", "gent", "get", "net", "new", "newt", "prat", "pry", "qua", "quart", "quartz", "rat", "tar", "tarp", "ten", "went", "wet", "arty", "rhr", "not", "quar"]
    
    mygame = Boggle(grid, dictionary)
    print(mygame.getSolution())

if __name__ == "__main__":
    main()
