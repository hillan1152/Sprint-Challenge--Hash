#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination

# Source = Starting Air Port -----> VALUE
# Destination = Next Airport -----> NEXT
# Beginning Source is None
# Ending Destination is None

# Hash:
#   K: starting location      V: Destination

# Fill up dictionary with all K/V Pairs
# Create list of the route
# Start with none, end with none
# return route 

def reconstruct_trip(tickets, length):
    
    """
    YOUR CODE HERE
    """
    # create dict
    cache = {}
    # Size of list * None for efficiency 
    route = [None] * length
    # helps calculate starting point for adding tickets
    r = 1
    # loop through each ticket and make source/destination -- k/v
    for place in tickets:
        # print("places", place.source)
        cache[place.source] = place.destination
        # print("cache", cache)
    # First route always None
    route[0] = cache["NONE"]
    # while r approaches length, increase by 1 and apply 
    while r < length:
        # print("r", r - 1)
        # print("route r", route[r])
        route[r] = cache[route[r-1]]
        r += 1


    return route




if __name__ == "__main__":
    ticket_1 = Ticket("NONE", "PDX")
    ticket_2 = Ticket("PDX", "DCA")
    ticket_3 = Ticket("DCA", "NONE")

    tickets = [ticket_1, ticket_2, ticket_3]

    expected = ["PDX", "DCA", "NONE"]
    result = reconstruct_trip(tickets, 3)

    print(result)