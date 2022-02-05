# import FruitVendor here

class FruitMarket(object):
    """
    The FruitMarket class is in charge of all of the vendors.
    """
    def __init__(self, vendors):
        """
        Initializes a FruitMarket with the provided list of vendors. self.vendors is a
        dictionary mapping name of the vendor to their FruitVendor object.

        @param vendors -- List of Strings, representing the name of a FruitVendor
        """
        # YOUR CODE HERE

    def __str__(self):
        """
        Returns a print-friendly version of the FruitMarket in the following format:
            <FruitMarket: vendor1, vendor2, ...>
        """
        return '<FruitMarket: %s>' % ', '.join(self.vendors.keys())

    def stock_one(self, vendor_name, fruit, quantity, cost=None):
        """
        Stocks one vendor with the provided number of fruit at the given cost.
        """
        # YOUR CODE HERE

    def stock_all(self, fruit, quantity):
        """
        Gives every vendor the given number of fruit.
        """
        # YOUR CODE HERE

    def fix_cost(self, fruit, cost):
        """
        Sets the cost of the given fruit in every vendor, without changing the quantity
        of the vendor.
        """
        # YOUR CODE HERE

    def buy_one(self, vendor_name, fruit, payment):
        """
        Buys 1 fruit at the given vendor with the given payment. Returns the change given
        by the payment and the cost of buying 1 fruit.
        """
        # YOUR CODE HERE
