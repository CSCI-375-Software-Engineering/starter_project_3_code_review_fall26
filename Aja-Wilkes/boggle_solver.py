# Copied Boggle_solver in from previous Codio assignment
class Boggle:
    def __init__(self, grid, dictionary):
        self.grid = grid
        self.dictionary = dictionary
        self.solutions = []

    def get_neighbors(self, row, col):
      directions = [(-1, 0), (1, 0), (0, -1), (0, 1),
                    (-1, -1), (-1, 1), (1, -1), (1, 1)]
                    # up, down, left, right, up-left, up-right, down-left, down-right)
      neighbors = [] # valid directions/moves
      for row_change, col_change in directions:
        new_row = row + row_change
        new_col = col + col_change

        if 0 <= new_row < len(self.grid) and 0 <= new_col < len(self.grid[0]):
          neighbors.append((new_row, new_col))
      return neighbors

    def search(self, row, col, current, visited):
      letter = self.grid[row][col]
      new_current = current + letter
      new_visited = visited | {(row, col)}

      if len(new_current) >= 3: # Rule out words less than 3, change case
        lower_current = new_current.lower()
        if lower_current in self.word_lookup:
          original_word = self.word_lookup[lower_current]
          if original_word not in self.solutions:
            self.solutions.append(original_word)
      if new_current.lower() not in self.prefixes:
        return
      for neighbor_row, neighbor_col in self.get_neighbors(row, col):
        if (neighbor_row, neighbor_col) not in new_visited:
          self.search(neighbor_row, neighbor_col, new_current, new_visited)


    # Create prefixes based on dictionary
    def set_prefixes(self):
      self.prefixes = set()
      self.word_lookup = {}
      for word in self.dictionary:
        self.word_lookup[word.lower()] = word
        for i in range (1, len(word) + 1):
          prefix = word[0:i]
          self.prefixes.add(prefix.lower())
          
    def getSolution(self):
      self.set_prefixes()
      self.solutions = []
      for row in range(len(self.grid)):
        for col in range(len(self.grid[0])):
          self.search(row, col, "", set())
      return self.solutions
def main():
    grid = [["T", "W", "Y", "R"], ["E", "N", "P", "H"],["G", "Z", "Qu", "R"],["O", "N", "T", "A"]]
    dictionary = ["art", "ego", "gent", "get", "net", "new", "newt", "prat", "pry", "qua", "quart", "quartz", "rat", "tar", "tarp", "ten", "went", "wet", "arty", "rhr", "not", "quar"]
    
    mygame = Boggle(grid, dictionary)
    
    print(mygame.getSolution())

if __name__ == "__main__":
    main()