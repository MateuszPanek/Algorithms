
arrr = [12, 10, 8, 12, 7, 6, 4, 10, 12]
def highest_rank(arrr: list):
    maxi = 0
    highest = 0
    for item in arrr:
        if arrr.count(item) >=  maxi and item > highest:
            maxi = arrr.count(item)
            highest = item
    return highest

print(highest_rank(arrr))