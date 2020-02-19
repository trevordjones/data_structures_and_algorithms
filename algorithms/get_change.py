"""
Problem: Money Change
Task: Find the minimum number of coins needed to change the input value
(an integer) into coins with denominations 1, 5, and 10.
"""


def get_change(amount):
    """
    @type   amount: int
    @param  amount: The amount you must find change for

    @rtype  int
    @return The optimum number of coins with denominations 1, 5, and 10 for the amount given
    """

    coin_counter = 0
    while amount > 0:
        if amount >= 10:
            amount -= 10
        elif amount >= 5:
            amount -= 5
        else:
            amount -= 1
        coin_counter += 1

    return coin_counter

if __name__ == '__main__':
    assert get_change(2) == 2
    assert get_change(28) == 6
