from market import FruitMarket
import unittest

class TestMarket(unittest.TestCase):
    """
    Tests the FruitMarket class
    """
    def setUp(self):
        self.market = FruitMarket(['Albertsons', 'Vons', 'Safeway', 'Trader Joe'])
        self.albertsons = self.market.vendors['Albertsons']
        self.vons = self.market.vendors['Vons']
        self.safeway = self.market.vendors['Safeway']
        self.trader = self.market.vendors['Trader Joe']

    def test_stock_one(self):
        self.market.stock_one('Albertsons', 'apple', 5, 1.50)
        self.assertEqual(self.albertsons.get_stock('apple'), 5)
        self.assertEqual(self.albertsons.get_cost('apple'), 1.5)
        self.assertIsNone(self.albertsons.get_stock('banana'))
        self.assertIsNone(self.albertsons.get_cost('banana'))

        # stock adds, cost replaces
        self.market.stock_one('Albertsons', 'apple', 5, 1.25)
        self.assertEqual(self.albertsons.get_stock('apple'), 10)
        self.assertEqual(self.albertsons.get_cost('apple'), 1.25)

        # no cost means cost stays the same
        self.market.stock_one('Albertsons', 'apple', 1)
        self.assertEqual(self.albertsons.get_stock('apple'), 11)
        self.assertEqual(self.albertsons.get_cost('apple'), 1.25)

    def test_stock_all(self):
        self.market.stock_all('banana', 10)
        self.assertEqual(self.albertsons.get_stock('banana'), 10)
        self.assertEqual(self.vons.get_stock('banana'), 10)
        self.assertEqual(self.safeway.get_stock('banana'), 10)
        self.assertEqual(self.trader.get_stock('banana'), 10)

        self.market.stock_one('Vons', 'banana', 10)
        self.market.stock_all('banana', 1)
        self.assertEqual(self.albertsons.get_stock('banana'), 11)
        self.assertEqual(self.vons.get_stock('banana'), 21)
        self.assertEqual(self.safeway.get_stock('banana'), 11)
        self.assertEqual(self.trader.get_stock('banana'), 11)

    def test_fix_cost(self):
        self.market.stock_all('banana', 10)
        self.market.fix_cost('banana', 2)
        self.assertEqual(self.albertsons.get_cost('banana'), 2)
        self.assertEqual(self.vons.get_cost('banana'), 2)
        self.assertEqual(self.safeway.get_cost('banana'), 2)
        self.assertEqual(self.trader.get_cost('banana'), 2)

    def test_buy_one(self):
        self.market.stock_all('apple', 2)
        self.market.fix_cost('apple', .75)

        # Exact change
        change = self.market.buy_one('Albertsons', 'apple', .75)
        self.assertEqual(self.albertsons.get_stock('apple'), 1)
        self.assertEqual(change, 0)
        self.assertEqual(self.albertsons.get_cost('apple'), .75)

        # Not enough payment
        change = self.market.buy_one('Albertsons', 'apple', 0)
        self.assertEqual(self.albertsons.get_stock('apple'), 1)
        self.assertIsNone(change)

        # Change given
        change = self.market.buy_one('Albertsons', 'apple', 10)
        self.assertEqual(self.albertsons.get_stock('apple'), 0)
        self.assertEqual(change, 9.25)

unittest.main()
