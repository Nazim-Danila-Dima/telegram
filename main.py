import unittest
import parse


class TestParse(unittest.TestCase):
    def test_parse(self):
        self.assertEqual(parse.parse('Лайпанов Назим Шамилевич, 212Б, 4, 3, https://github.com/nazim-080/OpenCV'), 1)
        self.assertEqual(parse.parse('Лайпанов Назим Шамилевич, 212Б, 3, https://github.com/nazim-080/OpenCV'), -1)
        self.assertEqual(parse.parse('Лайпанов Назим Шамилевич, 222Б, 4, 3, https://github.com/nazim-080/OpenCV'), -2)
        self.assertEqual(parse.parse('Лайпанов Назим Шамилевич, 212Б, 6, 3, https://github.com/nazim-080/OpenCV'), -3)
        self.assertEqual(parse.parse('Лайпанов Назим Шамилевич, 212Б, 4, 8, https://github.com/nazim-080/OpenCV'), -4)
        self.assertEqual(parse.parse('Лайпанов Назим Шамилевич, 212Б, 3, 4, https://gitub.com/nazim-080/OpenCV'), -5)


if __name__ == "__main__":
    unittest.main()
