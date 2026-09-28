#Name: Ohene Baffoe Osei
#SID : 004001870

class Boggle:
  def __init__(self, grid, dictionary):
        self.grid = grid
        self.dictionary = dictionary
        self.solutions = []
    

  def setGrid(self, grid):
      self.grid = grid
      self.solutions = []
      self.solution = []
    

  def setDictionary(self, dictionary):
      self.dictionary = dictionary
      self.solutions = []
      self.solution = []
    

  def validGrid(self):
      # Make sure the grid is a non-empty square grid
      if not isinstance(self.grid, list) or len(self.grid) == 0:
        return False
      
      size = len(self.grid)

      for row in self.grid:
        if not isinstance(row, list) or len(row) != size:
          return False
        
        for tile in row:
          # Every tile must contain a string
          if not isinstance(tile, str) or len(tile) == 0:
            return False
      
      return True
    

  def validateDictionary(self):
    # Make sure the dictionary is a list of strings
      if not isinstance(self.dictionary, list):
        return False
      
      for word in self.dictionary:
        if not isinstance(word, str):
          return False
      
      return True

    
  def buildTrie(self):
     # Build a trie so invalid word paths can be stopped early
      trie = {}

      for word in self.dictionary:
        if len(word) < 3:
          continue
          
        current = trie

        normalized_word = word.lower()

        for letter in normalized_word:
          if letter not in current:
            current[letter] = {}

          current = current[letter]
          # Mark the end of a complete dictionary word

        current['#'] = normalized_word
      
      return trie
    

  def moveThroughTile(self, node, tile):
      current = node

      # Check every letter in a tile, including multi-letter tiles like Qu

      for letter in tile.lower():
        if letter not in current:
          return 
        
        current = current[letter]
      
      return current
    

  def dfs(self, row, col, node, visited, found):
    #A tile cannot be used more than once in the same word
      if visited[row][col]:
        return 
      
      tile = self.grid[row][col]
      next_node = self.moveThroughTile(node, tile)
      #stop searching if this path is not a prefix in the trie

      if next_node is None:
        return 
      
      visited[row][col] = True

      if "#" in next_node:
        found[next_node['#']] = True
      
      #check all eight neighboring tiles
      for row_change in range(-1, 2):
        for col_change in range(-1, 2):
          if row_change == 0 and col_change ==0:
            continue
          
          new_row = row +row_change
          new_col = col + col_change
        

          if (
            0 <= new_row < len(self.grid)
            and 0 <= new_col < len(self.grid)
            and not visited[new_row][new_col]

          ):
            self.dfs(
              new_row,
              new_col,
              next_node,
              visited,
              found
            )
        #unmark the tile so it can be used in another path
      
      visited[row][col] = False

  def getSolution(self):
    self.solutions= []
    self.solution = []

    #return an empty list if either input is invalid

    if not self.validGrid() or not self.validateDictionary():
      return []
    
    trie = self.buildTrie()
    
    if len(trie) == 0:
      return []
    
    size = len(self.grid)

    visited = []

    for row in range(size):
      visited.append([False]*size)

    
    found = {}

    #start a search from every position on the board
    for row in range(size):
      for col in range(size):
        self.dfs(
          row,
          col,
          trie,
          visited,
          found
        )
    

    added = {}

    for word in self.dictionary:
      normalized_word = word.lower()

      if (
        len(word) >=3
        and normalized_word in found 
        and normalized_word not in added
      ):

        self.solutions.append(word)
        added[normalized_word] = True

    
    self.solution = self.solutions
    return self.solutions



def main():
    grid = [["T", "W", "Y", "R"], ["E", "N", "P", "H"],["G", "Z", "Qu", "R"],["O", "N", "T", "A"]]
    dictionary = ["art", "ego", "gent", "get", "net", "new", "newt", "prat", "pry", "qua", "quart", "quartz", "rat", "tar", "tarp", "ten", "went", "wet", "arty", "rhr", "not", "quar"]
    
    mygame = Boggle(grid, dictionary)
    print(mygame.getSolution())

if __name__ == "__main__":
    main()
