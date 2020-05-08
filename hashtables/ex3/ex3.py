# Understand
#   Given a list of lists:
#       Numbers = [
#            [1, 2, 3, 4, 5], [0]
#            [12, 7, 2, 9, 1], [1]
#            [99, 2, 7, 1,] [2]
#       ]
#   Find all numbers that repeat

def intersection(arrays):
    """
    YOUR CODE HERE
    """
    arrays_list = arrays[0]
    first = arrays_list[0]
    second = arrays_list[1]
    combo = 0
    cache = dict()
    for num in first:
        # print("FIRST --> ", num)
        for other_num in second:
            # print("SECOND", other_num)
            if other_num == num:
                combo = other_num
                key = combo 
                cache[key] = num
 
                
    
    return cache


if __name__ == "__main__":
    arrays = []
    a = [[1, 2, 3, 4, 5, 9], [12, 7, 2, 9, 1], [99, 2, 7, 1, 88, 9]]
    arrays.append(a)
    # arrays.append(list(range(1000000,2000000)) + [1,2,3])
    # arrays.append(list(range(2000000,3000000)) + [1,2,3])
    # arrays.append(list(range(3000000,4000000)) + [1,2,3])

    print(intersection(arrays))
