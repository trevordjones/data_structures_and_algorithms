"""
Problem: Maxiumum value of loot
Task: Find the most valuable combination of items assuming any fraction
      of an item can be put into the knapsack
"""

def fractional_knapsack(capacity, weights, values):
    """
    @type   capacity: int
    @param  capacity: The capacity of the knapsack

    @type   weights: list[int]
    @param  weights: Weight of an item - this is what fills the capacity of the knapsack

    @type   values: list[int]
    @param  values: The value of each item - corresponds to weight𝑖

    @rtype  float
    @return Maximum value of items that can fit into the knapsack. The difference
            between the value and the answer must be at most 10^−3
    """
    value = 0.

    fractions = {}
    for i, weight in enumerate(weights):
        fractions[float(values[i])/float(weight)] = [float(weight), float(values[i])]

    sorted_fractions = sorted(fractions.keys(), reverse=True)
    for fraction in sorted_fractions:
        if capacity == 0:
            return value

        weight = fractions[fraction][0]
        if capacity > weight:
            multiplier = weight
            capacity -= weight
        else:
            multiplier = capacity
            weight -= multiplier
            capacity = 0
        value = value + (multiplier * fraction)

    return value

if __name__ == "__main__":
    value = fractional_knapsack(50, [20, 50, 30], [60, 100, 120])
    assert round(value, 4) == 180.0000

    value = fractional_knapsack(10, [30], [500])
    assert round(value, 4) == 166.6667
