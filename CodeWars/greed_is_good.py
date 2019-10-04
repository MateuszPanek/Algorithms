def score(dice: list) -> int:
    from collections import Counter
    """Calculates score of dice throws"""
    results = {1: {6: 2000, 5: 2100, 4: 1100, 3: 1000, 2: 200, 1: 100},
               2: {6: 400, 5: 200, 4: 200, 3: 200, 2: 0, 1: 0},
               3: {6: 600, 5: 300, 4: 300, 3: 300, 2: 0, 1: 0},
               4: {6: 800, 5: 400, 4: 400, 3: 400, 2: 0, 1: 0},
               5: {6: 1000, 5: 700, 4: 550, 3: 500, 2: 100, 1: 50},
               6: {6: 1200, 5: 600, 4: 600, 3: 600, 2: 0, 1: 0}
               }
    return sum(results[value[0]][value[1]] for value in [item for item in Counter(dice).items()])
