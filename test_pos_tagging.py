import unittest
from pos_tagging import *

class Test(unittest.TestCase):

    def test_unchanging_plurals(self):
        m = unchanging_plurals()
        self.assertSetEqual(set(['sheep', 'moose', 'police', 'series', 'fish', 'multimedia', 'deer', 'headquarters', 'marijuana', 'salmon', 'cannabis', 'bison', 'swine', 'dna', 'buffalo', 'species', 'trout']), set(m))

    def test_noun_stem(self):
        m1 = noun_stem("sheep")
        m2 = noun_stem("buffalo")

        self.assertEqual(m1, "sheep")
        self.assertEqual(m2, "buffalo")

        m3 = noun_stem("men")
        m4 = noun_stem("women")
        m5 = noun_stem("policemen")

        self.assertEqual(m3, "man")
        self.assertEqual(m4, "woman")
        self.assertEqual(m5, "policeman")

        m6 = noun_stem("dogs")
        m7 = noun_stem("countries")
        m8 = noun_stem("ashes")

        self.assertEqual(m6, "dog")
        self.assertEqual(m7, "country")
        self.assertEqual(m8, "ash")

    def test_tag_word(self):

        m1 = Lexicon()
        m1.add("John", "P")
        m1.add("Mary", "P")
        m1.add("duck", "N")
        m1.add("student", "N")
        m1.add("purple", "A")
        m1.add("old", "A")
        m1.add("fly", "I")
        m1.add("swim", "I")
        m1.add("like", "T")
        m1.add("orange", "Ns")
        m1.add("orange", "A")
        m1.add("fish", "Ns")
        m1.add("fish", "Np")
        m1.add("fish", "Ip")
        m1.add("fish", "Tp")
        m1.add("a", "AR")

        self.assertSetEqual(set(tag_word(m1,"John")), set(["P"]))
        self.assertSetEqual(set(tag_word(m1,"orange")), set(["Ns","A"]))
        self.assertSetEqual(set(tag_word(m1,"fish")), set(["Ns","Np","Ip","Tp"]))
        self.assertSetEqual(set(tag_word(m1,"a")) , set(["AR"]))
        self.assertSetEqual(set(tag_word(m1,"zxghqw")), set([]))


if __name__ == '__main__':
    unittest.main()
