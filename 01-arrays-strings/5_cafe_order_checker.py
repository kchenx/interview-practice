# Cafe order checker
# I have two registers: one for take-out orders, and the other for the other
# folks eating inside the cafe. All the customer orders get combined into one
# list for the kitchen, where they should be handled first-come, first-served.
#
# Write a function to check that my service is first-come, first-served. All
# food should come out in the same order customers requested it.
#
# Assume each customer order as a unique integer.
#
# EXAMPLE
# Take-out orders: [1, 3, 5]
# Dine-in orders:  [2, 4, 6]
# Served orders:   [1, 2, 4, 6, 5, 3]
# Output:          False (3 was requested before 5, but 5 was served first)
#
# EXAMPLE
# Take-out orders: [17, 8, 24]
# Dine-in orders:  [12, 19, 2]
# Served orders:   [17, 8, 12, 19, 24, 2]
# Output:          True
#
# BONUS
# 1. This assumes each customer order in served_orders is unique. How can we
# adapt this to handle lists of customer orders with potential repeats?
#
# 2. Our implementation returns True when all the items in dine_in_orders and
# take_out_orders are first-come first-served in served_orders and False
# otherwise. That said, it'd be reasonable to raise an exception if some orders
# that went into the kitchen were never served, or orders were served but not
# paid for at either register. How could we check for those cases?
#
# 3. Our solution iterates through the customer orders from front to back.
# Would our algorithm work if we iterated from the back towards the front?
# Which approach is cleaner?

from typing import List
import unittest


def is_valid_merge(a: List[int], b: List[int], merged: List[int]) -> bool:
    """Returns true iff `merged` is a valid merge of `a` and `b`"""
    i = j = 0
    alen = len(a)
    blen = len(b)
    for mergedval in merged:
        if i < alen and mergedval == a[i]:
            i += 1
        elif j < blen and mergedval == b[j]:
            j += 1
        else:
            return False
    return True


class TestCafeOrderChecker(unittest.TestCase):
    def test_is_valid_merge(self):
        trues = [
            [[], [], []],
            [[1], [], [1]],
            [[1], [3], [1, 3]],
            [[1], [3], [3, 1]],
            [[1, 2], [5], [1, 5, 2]],
            [[17, 8, 24], [12, 19, 2], [17, 8, 12, 19, 24, 2]]
        ]
        falses = [
            [[1, 3, 5], [2, 4, 6], [1, 2, 4, 6, 5, 3]]
        ]
        for a, b, merged in trues:
            self.assertTrue(is_valid_merge(a, b, merged))
        for a, b, merged in falses:
            self.assertFalse(is_valid_merge(a, b, merged))


if __name__ == "__main__":
    unittest.main()
