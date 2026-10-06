#Nylah Shepherd, 03134431
#wrote in another program 

class Boggle:
    def __init__(self, grid, dictionary):
        self.Grid = grid
        self.Dictionary = dictionary
        self.solution = []

    #set a new grid
    def setGrid(self, new_grid):
        self.Grid = new_grid

    #set a new dictionary
    def setDictionary(self, new_dictionary):
        self.Dictionary = new_dictionary

    #find a word
    def findWord(self, word):
        word = word.lower()
        if len(word) < 3: #atleast 3 words
            return False

        #directions
        directions = [
            (-1, 0),   # up
            (1, 0),    # down
            (0, -1),   # left
            (0, 1),    # right
            (-1, -1),  # upper-left
            (-1, 1),   # upper-right
            (1, -1),   # lower-left
            (1, 1)     # lower-right
        ]

        #search for rest of word
        def search(row, col, index, visited):
            if index == len(word):  #check if word found
                return True

            #check all directions
            for direction in directions:
                dr, dc = direction
                new_row = row + dr
                new_col = col + dc

                #make sure new position on board.
                if (0 <= new_row < len(self.Grid) and
                    0 <= new_col < len(self.Grid[new_row])):

                    #confirming tile not used already
                    if (new_row, new_col) not in visited:
                        next_tile = self.Grid[new_row][new_col].lower()
                        
                        # does tile match next part of word
                        if word[index:index + len(next_tile)] == next_tile:
                            visited.add((new_row, new_col))
                            
                            # Continue looking for the rest of the word.
                            if search(
                                new_row,
                                new_col,
                                index + len(next_tile),
                                visited
                            ):
                                return True
                            # Try another path.
                            visited.remove((new_row, new_col))
            return False

        # Look for the first tile.
        for row in range(len(self.Grid)):
            for col in range(len(self.Grid[row])):

                first_tile = self.Grid[row][col].lower()
                # This also handles Qu, St, and Ie as two letters.
                if word[:len(first_tile)] == first_tile:

                    visited = set()
                    visited.add((row, col))

                    #search for rest of word
                    if search(
                        row,
                        col,
                        len(first_tile),
                        visited
                    ):
                        return True

        return False
    
    #find all words in dictionary on board
    def getSolution(self):
        self.solution = []
        # Check that the grid is valid.
        if not isinstance(self.Grid, list) or len(self.Grid) == 0:
            return []

        for row in self.Grid:
            if not isinstance(row, list) or len(row) == 0:
                return []
            for tile in row:
                if not isinstance(tile, str):
                    return []
                # Only Qu, St, and Ie can be two-letter tiles.
                if len(tile) > 1 and tile.lower() not in ["qu", "st", "ie"]:
                    return []
        # Check that the dictionary is valid.
        if not isinstance(self.Dictionary, list):
            return []

        for word in self.Dictionary:
            if not isinstance(word, str):
                return []
        # Check every dictionary word.
        for word in self.Dictionary:
            if self.findWord(word):
                self.solution.append(word)

        return self.solution
    

def main():
    grid = [["T", "W", "Y", "R"], ["E", "N", "P", "H"],["G", "Z", "Qu", "R"],["O", "N", "T", "A"]]
    dictionary = ["art", "ego", "gent", "get", "net", "new", "newt", "prat", "pry", "qua", "quart", "quartz", "rat", "tar", "tarp", "ten", "went", "wet", "arty", "rhr", "not", "quar"]
    
    mygame = Boggle(grid, dictionary)
    print(mygame.getSolution())

if __name__ == "__main__":
    main()