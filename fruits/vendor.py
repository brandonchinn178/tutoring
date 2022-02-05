class FruitVendor(object):
    """
    The class in charge of one vendor's fruit shop. Each vendor has their own stock of fruits
    and their own prices.
    """
    def __init__(self):
        """
        Initializes a FruitVendor with empty inventory and cost dictionaries. self.inventory
        will map a fruit to its stock and self.costs will map a fruit to its cost.
        """
        self.inventory = {}
        self.costs = {}

    def __str__(self):
        """
        Prints out this FruitVendor in the following format:
            +--------+----------+--------+
            | fruit  | quantity |  cost  |
            +--------+----------+--------+
            | apple  |    10    | $1.00  |
            | banana |    10    | $2.50  |
            +--------+----------+--------+
        """
        fruit_col_width = max([len(fruit) for fruit in self.inventory.keys()]) + 2
        border = ('+{:-^%d}+{:-^10}+{:-^7}+\n' % fruit_col_width).format('', '', '')
        row = '|{:^%d}|{:^10}|{:^7}|\n' % fruit_col_width

        table = border + row.format('fruit', 'quantity', 'cost') + border
        for fruit, quant in self.inventory.items():
            cost = self.costs.get(fruit, 0)
            table += row.format(fruit, quant, '${:.2f}'.format(cost))
        return table + border

    def get_stock(self, fruit):
        """
        Gets the quantity of the given fruit. Return None if fruit isn't in stock.
        """
        return self.inventory.get(fruit)

    def get_cost(self, fruit):
        """
        Gets the cost of the given fruit. Return None if fruit doesn't have a cost.
        """
        return self.costs.get(fruit)

    def stock(self, fruit, quantity, cost=None):
        """
        Stocks the specified fruit with the given quantity and cost. If the fruit already
        exists, add the given quantity to the existing quantity, but simply replace the
        existing cost with the new cost. If None is passed as the cost, keep the existing
        cost the same.

        >>> vendor.stock('apple', 5, 1.50)
        >>> vendor.stock('banana', 10, 2)
        >>> vendor.stock('apple', 5, 1)
        >>> vendor.stock('banana', 1)

        After this code, the vendor will have 10 apples at $1 and 11 bananas at $2.
        """
        old_quan = self.inventory.get(fruit, 0)
        self.inventory[fruit] = old_quan + quantity
        if cost is not None:
            self.costs[fruit] = cost

    def buy(self, fruit, quantity, payment):
        """
        Customer buys the given number of fruit with the given amount of money. Decrement
        the given amount of fruit in the inventory and return the change returned to the
        customer.

        If there is not enough fruit or the payment is not enough, return None.
        """
        if fruit not in self.inventory:
            return None

        old_quan = self.inventory[fruit]
        if old_quan < quantity:
            return None
        cost = self.costs[fruit]
        if payment < cost:
            return None

        self.inventory[fruit] = old_quan - quantity
        return payment - cost * quantity
