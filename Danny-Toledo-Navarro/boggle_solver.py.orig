class Boggle:
    def __init__(self, grid, dictionary):
        self.grid = grid
        self.dictionary = dictionary
        self.solutions = []
        self.trie = {}

    def validateGrid(self, g):
        if not g or len(g) == 0:
            return False
        rowLen = None
        for row in g:
            if not row or len(row) == 0:
                return False
            if rowLen is None:
                rowLen = len(row)
            elif len(row) != rowLen:
                return False
            for tile in row:
                if not isinstance(tile, str) or len(tile) == 0:
                    return False
        return True

    def validateDict(self, d):
        if not d or len(d) == 0:
            return False
        for word in d:
            if not isinstance(word, str) or len(word) == 0:
                return False
        return True

    def buildTrie(self, dictionary):
        root = {}
        for word in dictionary:
            node = root
            for ch in word.upper():
                if ch not in node:
                    node[ch] = {}
                node = node[ch]
            node["$"] = True
        return root

    def find_words(self, w, y, x, g, v, t, sol):
        # out of bounds
        if y < 0 or y >= len(g) or x < 0 or x >= len(g[0]):
            return
        # already used in this path
        if (y, x) in v:
            return

        # walk the tile's letters through the trie, one character at a time
        # (a tile like "Qu" consumes two trie levels in a single move)
        node = t
        for ch in g[y][x].upper():
            if ch not in node:
                return
            node = node[ch]

        # this tile is valid — commit to it
        w = w + g[y][x]
        v.add((y, x))

        if "$" in node and len(w) >= 3 and w not in sol:
            sol.append(w)

        directions = [(-1, -1), (-1, 0), (-1, 1),
                      (0, -1),           (0, 1),
                      (1, -1),  (1, 0),  (1, 1)]
        for dy, dx in directions:
            self.find_words(w, y + dy, x + dx, g, v, node, sol)

        # backtrack so other paths can reuse this tile
        v.remove((y, x))

    def getSolution(self):
        if not self.validateGrid(self.grid) or not self.validateDict(self.dictionary):
            return self.solutions

        self.trie = self.buildTrie(self.dictionary)

        for y in range(len(self.grid)):
            for x in range(len(self.grid[0])):
                self.find_words("", y, x, self.grid, set(), self.trie, self.solutions)

        return self.solutions


def main():
    grid = [["T", "W", "Y", "R"],
            ["E", "N", "P", "H"],
            ["G", "Z", "Qu", "R"],
            ["O", "N", "T", "A"]]
    dictionary = ["art", "ego", "gent", "get", "net", "new", "newt", "prat",
                  "pry", "qua", "quart", "quartz", "rat", "tar", "tarp",
                  "ten", "went", "wet", "arty", "rhr", "not", "quar"]

    mygame = Boggle(grid, dictionary)
    print(mygame.getSolution())


if __name__ == "__main__":
    main()