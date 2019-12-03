def spliter(array: str, args: str) -> list:
    """Slices given string by specified separator and returns a list of sub-strings"""
    splited = []
    start_i = 0
    array.strip(args)
    for item in array:
        if item == args:
            splited.append(array[start_i: array.index(item, start_i)])
            start_i = array.index(item, start_i) + 1
            print(start_i)
            print(array)
    splited.append(array[start_i:len(array) - 1])
    return splited


print(spliter('abcghrdchgg:hgfdchgjgfty:tyfhgvkyugvh:', ':'))
