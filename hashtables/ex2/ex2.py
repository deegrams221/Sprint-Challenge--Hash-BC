#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)

"""
* The crux of this problem requires us to 'link' tickets together to reconstruct the entire trip. For example, if we have a ticket `('SJC', 'BOS')` that has us flying from San Jose to Boston, then there exists another ticket where Boston is the starting location, `('BOS', 'JFK')`.
* We can hash each ticket such that the starting location is the key and the destination is the value. Then, when constructing the entire route, the `i`th location in the route can be found by checking the hash table for the `i-1`th location.
* You might need to do some cleanup at the end to make sure results match what the test and example are expecting.
"""
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination

def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    # route = [None] * length
    route = []

    """
    YOUR CODE HERE
    """

    # for loop - ticket in tickets (key: source, value: destination)
    for ticket in tickets:
        # hash table insert function ht, source, and destination
        hash_table_insert(hashtable, ticket.source, ticket.destination)
    # account for NONE
    destination = hash_table_retrieve(hashtable, 'NONE')
    # while loop - destination != NONE
    while destination is not 'NONE':
        # append destination to route
        route.append(destination)
        # destination set to retrieve ht, destination
        destination = hash_table_retrieve(hashtable, destination)

    # return route
    return route