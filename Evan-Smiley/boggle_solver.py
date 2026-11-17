###Evan Smiley 004002998###

class Boggle:
    def __init__(self, grid=None, dictionary=None):
        self._grid = []
        self._dictionary = set()
        self._solutions = []
        self._prefixes = set()
        self._rows = 0
        self._cols = 0
        
        if grid is not None and dictionary is not None:
            self.setGrid(grid)
            self.setDictionary(dictionary)
    
    def setGrid(self, grid):
        #Check if grid is valid
        if not grid or len(grid) == 0:
            self._grid = []
            self._rows = 0
            self._cols = 0
            return False
        
        #Convert grid to lowercase for case-insensitive matching
        self._grid = [[cell.lower() for cell in row] for row in grid]
        self._rows = len(self._grid)
        self._cols = len(self._grid[0]) if self._rows > 0 else 0
        self._solutions = []
        return True
    
    def setDictionary(self, dictionary):
        #Check if dictionary is valid
        if not dictionary or len(dictionary) == 0:
            self._dictionary = set()
            self._prefixes = set()
            return False
        
        #Convert dictionary to lowercase for case-insensitive matching
        self._dictionary = set(word.lower() for word in dictionary)
        self._prefixes = set()
        for word in self._dictionary:
            for i in range(1, len(word) + 1):
                self._prefixes.add(word[:i])
        self._solutions = []
        return True
    
    def getSolution(self):
        #Check if grid or dictionary is invalid
        if not self._grid or not self._dictionary:
            return []
        
        #Reset solutions and start DFS from each cell
        self._solutions = []
        for r in range(self._rows):
            for c in range(self._cols):
                self._dfs(r, c, "", set())
        return sorted(list(set(self._solutions)))
    
    def getGrid(self):
        #Return the current grid
        return self._grid
    
    def getDictionary(self):
        #Return the current dictionary as a sorted list
        return sorted(list(self._dictionary))
    
    def _dfs(self, r, c, word, visited):
        #Check if position is valid and not visited
        if not (0 <= r < self._rows and 0 <= c < self._cols and (r, c) not in visited):
            return
        
        #Add the current cell's value to the word
        word += self._grid[r][c]
        
        #Check if this prefix can lead to any word
        if word not in self._prefixes:
            return
        
        #Mark current cell as visited
        visited.add((r, c))
        
        #Check if current word is valid (3+ characters and in dictionary)
        if len(word) >= 3 and word in self._dictionary:
            self._solutions.append(word)
        
        #Explore all 8 adjacent cells
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr != 0 or dc != 0:
                    self._dfs(r + dr, c + dc, word, visited.copy())
        
        #Backtrack - unmark current cell
        visited.remove((r, c))


def parse_grid(grid_str):
    #Parse grid string into a 2D list
    grid_str = grid_str.strip()
    
    #Try eval first for simple cases
    try:
        grid = eval(grid_str)
        if isinstance(grid, list) and len(grid) > 0:
            return grid
    except:
        pass
    
    #Manual parsing for complex cases with multi-character tiles
    if grid_str.startswith('[') and grid_str.endswith(']'):
        grid_str = grid_str[1:-1]
    
    rows = []
    parts = grid_str.split('],[')
    
    for part in parts:
        part = part.strip('[]')
        cells = []
        i = 0
        while i < len(part):
            #Skip whitespace
            if part[i] in ' \t':
                i += 1
                continue
            
            #Handle quoted strings
            if part[i] == '"' or part[i] == "'":
                quote = part[i]
                i += 1
                start = i
                while i < len(part) and part[i] != quote:
                    i += 1
                cell = part[start:i]
                cells.append(cell)
                i += 1
            else:
                #Handle unquoted values
                start = i
                while i < len(part) and part[i] not in ', \t':
                    i += 1
                cell = part[start:i]
                if cell:
                    cells.append(cell)
            
            #Skip comma
            while i < len(part) and part[i] != ',':
                i += 1
            if i < len(part):
                i += 1
        
        if cells:
            rows.append(cells)
    
    return rows


def parse_dictionary(dict_str):
    #Parse dictionary string into a list of words
    dict_str = dict_str.strip()
    
    #Try eval first for simple cases
    try:
        dictionary = eval(dict_str)
        if isinstance(dictionary, list) and len(dictionary) > 0:
            return dictionary
    except:
        pass
    
    #Manual parsing for complex cases
    if dict_str.startswith('[') and dict_str.endswith(']'):
        dict_str = dict_str[1:-1]
    
    words = []
    i = 0
    while i < len(dict_str):
        #Skip whitespace
        if dict_str[i] in ' \t':
            i += 1
            continue
        
        #Handle quoted strings
        if dict_str[i] == '"' or dict_str[i] == "'":
            quote = dict_str[i]
            i += 1
            start = i
            while i < len(dict_str) and dict_str[i] != quote:
                i += 1
            word = dict_str[start:i]
            words.append(word)
            i += 1
        else:
            #Handle unquoted values
            start = i
            while i < len(dict_str) and dict_str[i] not in ', \t':
                i += 1
            word = dict_str[start:i]
            if word:
                words.append(word)
        
        #Skip comma
        while i < len(dict_str) and dict_str[i] != ',':
            i += 1
        if i < len(dict_str):
            i += 1
    
    return words


def main():
    #Get grid and dictionary input from user
    grid_input = input().strip()
    dict_input = input().strip()
    
    #Parse the inputs
    grid = parse_grid(grid_input)
    dictionary = parse_dictionary(dict_input)
    
    #Create Boggle game and get solution
    game = Boggle(grid, dictionary)
    print(game.getSolution())

if __name__ == "__main__":
    main()