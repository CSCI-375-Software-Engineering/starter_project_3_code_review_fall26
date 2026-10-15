import unittest
import sys

sys.path.append("/home/codio/workspace/")

from boggle_solver import Boggle


class TestSuite_Alg_Scalability_Cases(unittest.TestCase):

    # Test Frame 1
    def test_Normal_case_3x3(self):
        grid = [
            ["A", "B", "C"],
            ["D", "E", "F"],
            ["G", "H", "I"]
        ]

        dictionary = ["abc", "abdhi", "abi", "ef", "cfi", "dea"]

        mygame = Boggle(grid, dictionary)
        solution = [x.upper() for x in mygame.getSolution()]

        expected = ["abc", "abdhi", "cfi", "dea"]
        expected = [x.upper() for x in expected]

        self.assertEqual(sorted(expected), sorted(solution))

    # Test Frame 2
    def test_Normal_case_4x4(self):
        grid = [
            ["T", "W", "Y", "R"],
            ["E", "N", "P", "H"],
            ["G", "Z", "Qu", "R"],
            ["O", "N", "T", "A"]
        ]

        dictionary = ["art", "get", "net", "new", "newt", "quart", "wet"]

        mygame = Boggle(grid, dictionary)
        solution = mygame.getSolution()

        self.assertIn("new", solution)
        self.assertIn("quart", solution)

    # Test Frame 3
    def test_Normal_case_5x5(self):
        grid = [
            ["A", "B", "C", "D", "E"],
            ["F", "G", "H", "I", "J"],
            ["K", "L", "M", "N", "O"],
            ["P", "Q", "R", "S", "T"],
            ["U", "V", "W", "X", "Y"]
        ]

        dictionary = ["abc", "fgh", "klm", "pqr", "uvw"]

        mygame = Boggle(grid, dictionary)
        solution = mygame.getSolution()

        self.assertIn("abc", solution)
        self.assertIn("fgh", solution)
        self.assertIn("klm", solution)

    # Test Frame 4
    def test_Normal_case_6x6(self):
        grid = [
            ["A", "B", "C", "D", "E", "F"],
            ["G", "H", "I", "J", "K", "L"],
            ["M", "N", "O", "P", "Q", "R"],
            ["S", "T", "U", "V", "W", "X"],
            ["Y", "Z", "A", "B", "C", "D"],
            ["E", "F", "G", "H", "I", "J"]
        ]

        dictionary = ["abc", "ghi", "mno", "stu"]

        mygame = Boggle(grid, dictionary)
        solution = mygame.getSolution()

        self.assertIn("abc", solution)
        self.assertIn("ghi", solution)
        self.assertIn("mno", solution)

    # Test Frame 5
    def test_large_dictionary(self):
        grid = [
            ["C", "A", "T"],
            ["D", "O", "G"],
            ["R", "A", "T"]
        ]

        dictionary = [
            "cat", "dog", "rat", "fish", "bird",
            "horse", "mouse", "snake", "lion", "tiger"
        ]

        mygame = Boggle(grid, dictionary)
        solution = mygame.getSolution()

        self.assertIn("cat", solution)
        self.assertIn("dog", solution)
        self.assertIn("rat", solution)
        self.assertNotIn("fish", solution)


class TestSuite_Simple_Edge_Cases(unittest.TestCase):

    # Test Frame 6
    def test_SquareGrid_case_1x1(self):
        grid = [["A"]]
        dictionary = ["a", "b", "c"]

        mygame = Boggle(grid, dictionary)
        solution = mygame.getSolution()

        self.assertEqual([], solution)

    # Test Frame 7
    def test_EmptyGrid_case_0x0(self):
        grid = [[]]
        dictionary = ["hello", "there", "general", "kenobi"]

        mygame = Boggle(grid, dictionary)
        solution = mygame.getSolution()

        self.assertEqual([], solution)

    # Test Frame 8
    def test_empty_dictionary(self):
        grid = [
            ["A", "B"],
            ["C", "D"]
        ]

        dictionary = []

        mygame = Boggle(grid, dictionary)

        self.assertEqual([], mygame.getSolution())

    # Test Frame 9
    def test_non_square_grid(self):
        grid = [
            ["A", "B", "C"],
            ["D", "E", "F"]
        ]

        dictionary = ["abc"]

        mygame = Boggle(grid, dictionary)

        self.assertEqual([], mygame.getSolution())

    # Test Frame 10
    def test_grid_not_list(self):
        grid = "ABC"
        dictionary = ["abc"]

        mygame = Boggle(grid, dictionary)

        self.assertEqual([], mygame.getSolution())

    # Test Frame 11
    def test_dictionary_not_list(self):
        grid = [
            ["A", "B"],
            ["C", "D"]
        ]

        dictionary = "abc"

        mygame = Boggle(grid, dictionary)

        self.assertEqual([], mygame.getSolution())

    # Test Frame 12
    def test_empty_tile(self):
        grid = [
            ["A", ""],
            ["C", "D"]
        ]

        dictionary = ["acd"]

        mygame = Boggle(grid, dictionary)

        self.assertEqual([], mygame.getSolution())

    # Test Frame 13
    def test_non_string_tile(self):
        grid = [
            ["A", 5],
            ["C", "D"]
        ]

        dictionary = ["acd"]

        mygame = Boggle(grid, dictionary)

        self.assertEqual([], mygame.getSolution())


class TestSuite_Complete_Coverage(unittest.TestCase):

    # Test Frame 14
    def test_horizontal_word(self):
        grid = [
            ["C", "A", "T"],
            ["X", "X", "X"],
            ["X", "X", "X"]
        ]

        mygame = Boggle(grid, ["cat"])

        self.assertIn("cat", mygame.getSolution())

    # Test Frame 15
    def test_vertical_word(self):
        grid = [
            ["C", "X", "X"],
            ["A", "X", "X"],
            ["T", "X", "X"]
        ]

        mygame = Boggle(grid, ["cat"])

        self.assertIn("cat", mygame.getSolution())

    # Test Frame 16
    def test_diagonal_word(self):
        grid = [
            ["C", "X", "X"],
            ["X", "A", "X"],
            ["X", "X", "T"]
        ]

        mygame = Boggle(grid, ["cat"])

        self.assertIn("cat", mygame.getSolution())

    # Test Frame 17
    def test_word_changes_direction(self):
        grid = [
            ["C", "A", "X"],
            ["X", "T", "X"],
            ["X", "X", "X"]
        ]

        mygame = Boggle(grid, ["cat"])

        self.assertIn("cat", mygame.getSolution())

    # Test Frame 18
    def test_word_not_on_board(self):
        grid = [
            ["C", "A", "T"],
            ["X", "X", "X"],
            ["X", "X", "X"]
        ]

        mygame = Boggle(grid, ["dog"])

        self.assertNotIn("dog", mygame.getSolution())

    # Test Frame 19
    def test_short_word_not_allowed(self):
        grid = [
            ["A", "T"],
            ["X", "X"]
        ]

        mygame = Boggle(grid, ["at"])

        self.assertNotIn("at", mygame.getSolution())

    # Test Frame 20
    def test_tile_cannot_be_reused(self):
        grid = [
            ["A", "B"],
            ["X", "X"]
        ]

        mygame = Boggle(grid, ["aba"])

        self.assertNotIn("aba", mygame.getSolution())

    # Test Frame 21
    def test_duplicate_dictionary_word(self):
        grid = [
            ["C", "A"],
            ["X", "T"]
        ]

        mygame = Boggle(grid, ["cat", "cat"])

        solution = mygame.getSolution()

        self.assertEqual(1, solution.count("cat"))


class TestSuite_Qu_and_St(unittest.TestCase):

    # Test Frame 22
    def test_Qu_tile(self):
        grid = [
            ["Qu", "A"],
            ["X", "T"]
        ]

        mygame = Boggle(grid, ["quat"])

        self.assertIn("quat", mygame.getSolution())

    # Test Frame 23
    def test_Qu_tile_long_word(self):
        grid = [
            ["Qu", "A", "R"],
            ["X", "X", "T"],
            ["X", "X", "Z"]
        ]

        mygame = Boggle(grid, ["quart"])

        self.assertIn("quart", mygame.getSolution())

    # Test Frame 24
    def test_St_tile(self):
        grid = [
            ["St", "A"],
            ["X", "R"]
        ]

        mygame = Boggle(grid, ["star"])

        self.assertIn("star", mygame.getSolution())

    # Test Frame 25
    def test_Ie_tile(self):
        grid = [
            ["P", "Ie"],
            ["X", "R"]
        ]

        mygame = Boggle(grid, ["pier"])

        self.assertIn("pier", mygame.getSolution())


if __name__ == "__main__":
    unittest.main()
