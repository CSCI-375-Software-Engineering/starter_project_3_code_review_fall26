class Boggle:
    def __init__(self, grid, dictionary):
        self.grid = grid
        self.dictionary = dictionary
        self.solutions = []
    def setGrid(self, grid):
        self.grid = grid

    def setDictionary(self, dictionary):
        self.dictionary = dictionary

    def getSolution(self):
        #Check if grid is empty
        if not self.grid:
            return []
        #Check if dictionary is empty
        if not self.dictionary:
            return []
        #Check if grid is a valid 2d array
        if type(self.grid) != list or type(self.grid[0]) != list:
            return []
        #Check if dictionary is a list
        if type(self.dictionary) != list:
            return []
        #Check if length of rows and columns are equal in the grid
        row_length = len(self.grid[0])
        for row in self.grid:
            if type(row) != list or len(row) != row_length:
                return []
        #Check if each element in dictionary is a word
        for word in self.dictionary:
            if type(word) != str:
                return []
        #Changes all letters in the array to uppercase
        for row in self.grid:
            for col in range(len(row)):
                if type(row[col]) != str:
                    return []
                else:
                    row[col] = row[col].upper()
        #Changes all letters in the dictionary to uppercase
        for i in range(len(self.dictionary)):
            self.dictionary[i] = self.dictionary[i].upper()
        #Checks if the double letters in the array are together
        invalid_tiles = {"Q", "S", "I"}
        valid_pairs = {"QU", "ST", "IE"}
        for row in self.grid:
            for cell in row:
                if cell in invalid_tiles:
                    return [] 
                if (len(cell) == 2 and cell[0] in invalid_tiles and cell not in valid_pairs):
                    return []

        #Set of full words for complete word checks
        dictionary_set = set(self.dictionary)
        #Set of prefixes for every word for prefix checks
        prefix_set = set()
        #Find prefix of every word to add to prefix_set
        for word in self.dictionary:
            for i in range(1, len(word) + 1):
                prefix_set.add(word[:i])

        #Stores the size of the grid and create sets to track solutions and already visited coordinates
        num_rows = len(self.grid)
        num_cols = len(self.grid[0])
        solutions = set()
        visited = set()

        #Defines all possible directions to traverse through the grid
        directions = [
            (-1,-1), (-1,0), (-1,1), 
            (0, -1), (0, 1), (1,-1),
            (1,0), (1,1)
        ]

        #Depth-First Search function to search through the grid
        def _dfs(r, c, current_word):
            #If the word is not in the prefix set, then stop exploring that path
            if current_word not in prefix_set:
                return
            #If the word is long enough and in the dictionary then add to solutions 
            if current_word in dictionary_set:
                if len(current_word) >= 3:
                    solutions.add(current_word)
            #marks the position so it doesn't reuse tiles
            visited.add((r,c))
            #explore all unvisited neighboring tiles in the grid
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < num_rows and 0 <= nc < num_cols and (nr, nc) not in visited:
                    _dfs(nr, nc, current_word + self.grid[nr][nc])
            #Backtracks by removing the saved position
            visited.remove((r,c))
        #Starts the depth first search
        for r in range(num_rows):
            for c in range(num_cols):
                _dfs(r, c, self.grid[r][c])
    #returns the solution to the game
        self.solution = sorted(list(solutions))
        return self.solution


def main():
    grid = [["T", "W", "Y", "R"], ["E", "N", "P", "H"],["G", "Z", "Qu", "R"],["O", "N", "T", "A"]]
    dictionary = ["art", "ego", "gent", "get", "net", "new", "newt", "prat", "pry", "qua", "quart", "quartz", "rat", "tar", "tarp", "ten", "went", "wet", "arty", "rhr", "not", "quar"]
    
    mygame = Boggle(grid, dictionary)
    print(mygame.getSolution())

if __name__ == "__main__":
    main()
