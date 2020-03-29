import itertools
xs = [100, 76, 56, 44, 89, 73, 68, 56, 64, 123, 2333, 144, 50, 132, 123, 34, 89]
§

def choose_best_sum(t, k, ls):
    return max([sum(li) for li in(itertools.combinations(ls, k)) if sum(li) <= t], default=None)
