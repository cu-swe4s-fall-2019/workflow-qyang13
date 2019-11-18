import unittest
import get_gene_counts as pg


class TestPlotGtex(unittest.TestCase):
    '''Test for functions in get_gene_counts'''
    def test_binary_search(self):
        '''Test for binary search'''
        L = [['a', 1], ['b', 2], ['c', 3], ['d', 4]]
        self.assertEqual(pg.binary_search('a', L), 1)

    def test_binary_search_empty(self):
        '''Test for binary search'''
        L = []
        self.assertEqual(pg.binary_search('z', L), -1)

    def test_binary_search_not_found(self):
        '''Test for binary search'''
        L = [['a', 1], ['b', 2], ['c', 3], ['d', 4]]
        self.assertEqual(pg.binary_search('z', L), -1)


if __name__ == '__main__':
    unittest.main()
