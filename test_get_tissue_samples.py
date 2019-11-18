import unittest
import get_tissue_samples as pg


class TestPlotGtex(unittest.TestCase):
    '''Test for functions in plot_gtex'''
    def test_linear_search(self):
        '''Test for linear search'''
        L = [2, 4, 5, 6, 7, 8]
        self.assertEqual(pg.linear_search(4, L), 1)

    def test_linear_search_empty(self):
        '''Test for linear search'''
        L = []
        self.assertEqual(pg.linear_search(4, L), -1)

    def test_linear_search_not_found(self):
        '''Test for linear search'''
        L = [2, 4, 5, 6, 7, 8]
        self.assertEqual(pg.linear_search(1, L), -1)


if __name__ == '__main__':
    unittest.main()
