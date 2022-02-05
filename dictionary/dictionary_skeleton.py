"""
In this program, you will implement the built-in Python dictionary type using lists. A
dictionary can be implemented by maintaining a list of lists, in the following format:

[
    [
        (key, value),
        (key, value)
    ],
    ...
]

The inner lists are called buckets, which contain (key, value) pairs. You should implement
the following functions:
    - insert(key, value)
    - get(key)
    - remove(key)
    - clear()
"""

class MyDictionary:
    def __init__(self, num_buckets=100):
        """
        Creates a new empty MyDictionary with the given number of buckets, by default 100.
        """
        self.buckets = [[] for i in range(num_buckets)]
        self.num_buckets = num_buckets

    def __str__(self):
        """
        Turns the MyDictionary into a string, which allows it to be printed with:
            print my_dict
        """
        all_items = ['%r: %r' % (key, value) for (key, value) in self.items()]
        return '{%s}' % ', '.join(all_items)

    def __getitem__(self, key):
        """
        Allows 'getting' an item using bracket notation like:
            my_dict['Brandon']
        """
        return self.get(key)

    def _get_hash(self, key):
        """
        Hashes the given key by calling Python's default hashing function and modulo with the
        number of buckets to get a number in the range of 0 to (num_buckets - 1). Call this
        to get the bucket to put the (key, value) pair into.
        """
        return hash(key) % self.num_buckets

    def items(self):
        """
        Returns all of the (key, value) pairs in the dictionary. Basically "flattens" the
        list of lists into a single list.
        """
        return [item for sublist in self.buckets for item in sublist]

    def insert(self, key, value):
        """
        Inserts the given (key, value) pair into self.buckets. Does nothing if the key
        already exists in the buckets.

        Remember to insert the entire (key, value) pair so that you can look for the key
        later. Also remember that self._get_hash(key) gets the bucket to insert the key-value
        pair into.
        """
        pass

    def get(self, key):
        """
        Returns the value for the given key, or None if the key does not exist.

        Remember that self._get_hash(key) always returns the same number for the same key. So
        calling it multiple times means you will always get the same bucket for the same key.
        """
        pass

    def remove(self, key):
        """
        Removes the value for the given key. Does nothing if the key doesn't exist.

        To delete an item in a list, use the `del` keyword. For example, to delete the
        item at the 1st index of a list, you would write:
            del some_list[1]
        """
        pass

    def clear(self):
        """
        Clears all of the items in the buckets.
        """
        pass

def main():
    """
    The main function that will be called when executing the file
    """
    ages = MyDictionary()

    ages.insert('Brandon', 20)
    ages.insert('John Smith', 15)
    ages.insert('Jungwoo', 14)
    assert ages.get('Brandon') == 20
    assert ages['Jungwoo'] == 14
    # 'Jungwoo' already exists, so don't do anything
    ages.insert('Jungwoo', 100)
    assert ages['Jungwoo'] == 14

    ages.remove('Brandon')
    assert ages.get('Brandon') is None
    assert ages.get('John Smith') == 15
    # should not do anything
    ages.remove('foo')

    ages.clear()
    assert ages['Brandon'] is None
    assert ages['John Smith'] is None
    assert ages['Jungwoo'] is None

    ages.insert('Jungwoo', 14)
    assert ages['Jungwoo'] == 14
    print 'Success!'

if __name__ == '__main__':
    main()
