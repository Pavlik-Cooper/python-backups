import unittest
import app


class TestCap(unittest.TestCase):
    def test_one_word(self):
        word = "python"
        res = app.cap(word)
        self.assertEqual(res,"Python")

    def test_sentence(self):
        sent = "monty python"
        res = app.cap(sent)
        self.assertEqual(res,sent.title())



if __name__== "__main__":
    unittest.main()