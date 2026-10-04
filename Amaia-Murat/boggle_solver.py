# Amaia Murat 004002220


class Boggle:
    def __init__(self, grid, dictionary):
        self.grid = grid
        self.dictionary = dictionary
        self.solution = []
        # Review Change: Use a set for faster duplicate checking.
        self.found_words = set()
        self.trie = {}  # Stores dictionary words in a Trie.

    def setGrid(self, grid):
        # Artificial Design: Updates the game board.
        self.grid = grid

    def setDictionary(self, dictionary):
        # Artificial Design: Updates the dictionary.
        self.dictionary = dictionary

    def getSolution(self):
        '''
        Searches the entire Boggle board for words that appear in the
        dictionary and can be formed using adjacent tiles.

        Returns:
        A list of all valid words found on the Boggle board.
        An empty list if the grid/dictionary is invalid or empty.

        Preconditions:
        The grid must be a non-empty NxN board (a square).
        The dictionary must contain valid words.
        Dictionary words must be at least 3 letters long.

        Postconditions:
        self.solution contains all valid words found on the board.
        No duplicate words are in the solution list.
        The search allows horizontal, vertical, and diagonal movement.
        A Boggle cube cannot be used more than once in the same word.
        '''
        self.solution = []

        # Review Change: Reset set for each new search.
        self.found_words = set()

        # Review Change: Validate the grid type explicitly.
        if not isinstance(self.grid, list):
            return []

        # Review Change: Validate the dictionary type explicitly.
        if not isinstance(self.dictionary, list):
            return []

        if not self.grid or not self.dictionary:
            return []

        n = len(self.grid)

        if n == 0:
            return []

        for row in self.grid:
            # Review Change: Validate row type and square dimensions.
            if not isinstance(row, list) or len(row) != n:
                return []

            for tile in row:
                # Review Change: Validate tile type explicitly.
                if not isinstance(tile, str) or tile == "":
                    return []

                if tile.upper() in ["Q", "S", "I"]:
                    return []

        self.trie = {}

        # Ignore dictionary words shorter than 3 letters.
        for word in self.dictionary:
            # Review Change: Handle invalid dictionary entries explicitly.
            if not isinstance(word, str):
                continue

            if len(word) < 3:
                continue

            lower_word = word.lower()
            node = self.trie

            for letter in lower_word:
                if letter not in node:
                    node[letter] = {}

                node = node[letter]

            node["word"] = word

        # Review Change: Create visited once and reuse it.
        visited = []

        for row in range(n):
            visited.append([False] * n)

        # Begin searching from every tile on the board.
        for y in range(n):
            for x in range(n):
                self.findWords(y, x, "", self.trie, visited)

        return self.solution

    def findWords(self, y, x, curr_word, node, visited):
        '''
        Recursively searches the board for dictionary words that can be
        formed starting from the specified tile.

        Parameters:
        y: The row position of the current tile.
        x: The column position of the current tile.
        curr_word: The letters collected so far.
        node: The current location in the dictionary Trie.
        visited: A 2D list tracking cubes used in the current word.

        Returns:
        None. Words that are found are added to self.solution.

        Preconditions:
        y and x represent a possible board position.
        node represents the current Trie position.
        visited tracks cubes already used by the current word.

        Postconditions:
        Valid dictionary words are added to self.solution.
        All adjacent directions are searched.
        A cube is only used once per word.
        Qu, St, and Ie are treated as two letters but one cube.
        '''

        n = len(self.grid)

        if y < 0 or y >= n or x < 0 or x >= n:
            return

        if visited[y][x]:
            return

        tile = self.grid[y][x].lower()
        curr_node = node

        for letter in tile:
            if letter not in curr_node:
                return

            curr_node = curr_node[letter]

        new_word = curr_word + tile

        if "word" in curr_node:
            word = curr_node["word"]

            # Review Change: Use set lookup for duplicate checking.
            if word not in self.found_words:
                self.solution.append(word)
                # Review Change: Add the word to the set.
                self.found_words.add(word)

        # Mark the cube as used for the current search path.
        visited[y][x] = True

        # Search all eight adjacent directions.
        for dy in [-1, 0, 1]:
            for dx in [-1, 0, 1]:
                if dy == 0 and dx == 0:
                    continue

                # Recursively search the neighboring cube.
                self.findWords(
                    y + dy, x + dx, new_word, curr_node, visited
                )

        # Review Change: Reset the shared matrix during backtracking.
        visited[y][x] = False


def main():
    grid = [
        ["T", "W", "Y", "R"],
        ["E", "N", "P", "H"],
        ["G", "Z", "Qu", "R"],
        ["O", "N", "T", "A"]
    ]

    dictionary = [
        "art", "ego", "gent", "get", "net", "new", "newt",
        "prat", "pry", "qua", "quart", "quartz", "rat",
        "tar", "tarp", "ten", "went", "wet", "arty",
        "rhr", "not", "quar"
    ]

    mygame = Boggle(grid, dictionary)
    print(mygame.getSolution())


if __name__ == "__main__":
    main()
