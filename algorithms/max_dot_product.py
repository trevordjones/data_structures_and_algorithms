"""
Problem: Maximum Advertisement Revenue
Task: Given two sequences a1, a2, . . . , a𝑛 (a𝑖 is the profit per click of the 𝑖-th ad)
      and b1, b2, . . . , b𝑛 (b𝑖 is the average number of clicks per day of the 𝑖-th slot),
      we need to partition them into 𝑛 pairs (a𝑖, b𝑗) such that the sum of their products
      is maximized.

      Basically need to pair each a𝑖 with each b𝑗 such that when multiplied and then summed,
      it is the greatest possible value.
"""

def max_dot_product(profits_per_click, clicks_per_day):
    """
    @type   profits_per_click: list[int]
    @param  profits_per_click: The profit per click of the 𝑖-th slot
            per click

    @type   clicks_per_day: list[int]
    @param  clicks_per_day: Average number of clicks per day of the 𝑖-th slot

    @rtype  int
    @return Maximum value of the sum of a𝑖 and b𝑖 (or some permutation of b𝑖)
    """

    res = 0
    profits_per_click.sort()
    clicks_per_day.sort()
    for i in range(len(profits_per_click)):
        res += profits_per_click[i] * clicks_per_day[i]
    return res

if __name__ == '__main__':
    assert max_dot_product([23], [39]) == 897
    assert max_dot_product([1, 3, -5], [-2, 4, 1]) == 23
