def has_negatives(a):

    """
    YOUR CODE HERE
    """
    cache = {}
    result = []
    # iterate through list to gather all k/v pairs
    for num in range(0, len(a)):
        number = abs(a[num])
        if number in cache:
            cache[number] += 1
            # print("CACHE NUMBER ", cache[number])
        else:
            cache[number] = 1
        # print("CACHE --> ", cache)
    for key in cache:   
        # print("key", key)
        # print("cache key --> ", cache[key])
        if cache[key] > 1:
            result.append(key)
    return result


if __name__ == "__main__":
    print(has_negatives([-1,-2,1,2,3,4,-4]))
