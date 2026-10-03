#Amaia Murat 004002220

class Boggle:
    def __init__(self, grid, dictionary):
        self.grid = grid
        self.dictionary = dictionary
        self.solution = []
        self.trie = {} #Stores dictionary words in a Trie for searching

    def setGrid(self, grid): #Artificial Design: Sets/updates the the game board
        self.grid = grid
    
    def setDictionary(self, dictionary): #Artificial Design: Sets/updates the dictionary
        self.dictionary = dictionary

    def getSolution(self): 
      
        '''
        Searches the entire Boggle board for words that appear in the dictionary and can be formed using adjacent tiles
        
        Returns:
        A list of all valid words found on the Boggle board
        An empty list if the grid/dictionary is invalid or empty

        Preconditions:
        The grid must be a non-empty NxN board (a square)
        The dictionary must contain valid words
        len(words) must be >= 3

        Postconditions:
        self.solution contains all valid words found on the board
        No duplicate words in the solution list
        The search allows horizontal, vertical, and diagonal movement
        A Boggle cube cannot be used more than once in the same word
        '''
        self.solution = []

        try: #If an unexpected error occurs, returns [] instead of stopping the program

          if not self.grid or not self.dictionary: #Checks if grid or dictionary is empty 
            return [] #Returns an empty list if the grid of dictionary is empty
        
          n = len(self.grid) #Let n = number of rows; the grid must be a square
        
          if n == 0:
            return [] #grid with 0 rows is not valid

          for y in self.grid: #Let y = num of rows in the grid; verify each row is NxN
            if len(y) != n:
              return [] #Returns empty list if the grid is not a square

            for tile in y:
              if tile == "": #Empty str are not valid Boggle tiles
                return []
              if tile.upper() in ["Q","S","I"]: #Raw Q, S, I are not valid
                return []

          self.trie = {} #Create trie to store dictionary words
          # Ignore words shorter than 3 letters
        
          for word in self.dictionary:
            if len(word) < 3:
              continue
            lower_word = word.lower() #Makes words case-insensitive
            node = self.trie

            for letter in lower_word:
              if letter not in node: 
                node[letter] = {} #Create a new Trie node if this letter does not exist

              node = node[letter] #Move to the next Trie node

            node["word"] = word #Store the complete dictionary word at the end of its Trie

        #Begin searching from every tile in the board

          for y in range(n):
            for x in range(n):
              visited = []

              #Create a grid to track which cubes have been used in the current word
            
              for row in range(n):
                visited.append([False]*n)

              self.findWords(y, x, "", self.trie, visited)

          return self.solution #Returns the list of valid words found on the board

        except:
          return [] #If any unexpected error occurs

    def findWords(self, y, x, curr_word, node, visited):
          
      '''
      Recursively searches the board for dictionary words that can be formed starting from the specified tile

      Parameters: 
      y: The row position of the current tile
      x: The column position of the current tile
      curr_word: The letters collected so far
      node: The current location in the dictionary Trie
      visited: A 2D list that tracks which cubes are currently used

      Returns:
      None. Words that are found are added to self.solution

      Preconditions:
      y and x represent a possible board position
      node represents the current Trie position
      visited tracks cubes already used by the current word

      Postconditions:
      Valid dictionary words are added to self.solution
      All adjacent directions are searched
      A cube is only used once in the per word
      Qu, St, and Ie are treated as two letters but one physical cube
      '''

      n = len(self.grid)

      if y < 0 or y >=  n or x < 0 or x >= n:
        return #Stop if the coordinates are outside the board

      if visited[y][x]:
        return #Stop if this cube has already been used in the current word

      tile = self.grid[y][x].lower() #Get the current tile and convert it to lowercase
      curr_node = node

      for letter in tile:
        if letter not in curr_node:
          return #Stop if the tile can't continue a dictionary word

        curr_node = curr_node[letter] #Move to the next Trie node
      new_word = curr_word + tile #Add the current tile to the word being formed

      if "word" in curr_node:
        word = curr_node["word"]
              
        if word not in self.solution: #Makes sure the word isn't added more than once
          self.solution.append(word)

      visited[y][x] = True #Marks the cube as used for the current word

      #Search all eight adjacent directions

      for dy in [-1, 0, 1]: 
        for dx in [-1, 0, 1]:
          if dy == 0 and dx == 0:
            continue #Skip the current cube, which we can't repeat

          ''' 
          Recursively search the neighboring cube
          Pass the new word and current Trie node so the search can continue building the word from the neighboring tile
          '''

          self.findWords(y+dy, x+dx, new_word, curr_node, visited)

      visited[y][x] = False #Unmark the cube so it can be used in another path



def main():
    grid = [["T", "W", "Y", "R"], ["E", "N", "P", "H"],["G", "Z", "Qu", "R"],["O", "N", "T", "A"]]
    dictionary = ["art", "ego", "gent", "get", "net", "new", "newt", "prat", "pry", "qua", "quart", "quartz", "rat", "tar", "tarp", "ten", "went", "wet", "arty", "rhr", "not", "quar"]
    
    mygame = Boggle(grid, dictionary)
    print(mygame.getSolution())

if __name__ == "__main__":
    main()