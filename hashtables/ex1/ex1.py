# Understand
#   Inputs:
#       Weight = Array of Nums
#       Length = Lenght of array
#       Limit  = Target for sum of weights
#   Output:
#       Tuple of Indices
#   Ex:
#       weights = [4, 4], length = 2, limit = 8
#       ANSWER = (0, 1) ---> index 0 is 4, index 1 is 4 --> 4 + 4 = 8



def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    weight_chart = {}
    # weight_index = []
    # Loop over weights and add them to dict
    for i in range(0, length):
        weight_chart[weights[i]] = i
        print("Testing out chart --> ", weight_chart)
    l = 0
    while l <= length - 1:
        # print("weight L --> ", weights[l])
        diff = limit - weights[l]
        # print("diff --> ", diff)
        # print("WEIGHTS DIFF --> ", weights[diff])
        if diff in weight_chart:
            print("MADE IT HERE")
            return (weight_chart[diff], l)
        l += 1


if __name__ == "__main__":
    weight = [4, 5, 6, 11, 15, 99, 12, 35, 80]
    length = len(weight)
    limit = 27

    result = get_indices_of_item_weights(weight, length, limit)

    print(result)