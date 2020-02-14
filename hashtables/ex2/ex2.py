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
    route = [None] * length

    """
    YOUR CODE HERE
    """
    # print tickets and length to check the data

    # for loop - ticket in tickets (key: source, value: destination)
        # hash table insert function ht, source, and destination
    # set 1st route equal to retrieve function ht, and 'None' source

    # for loop - index in range of 1, length (skip source)
        # set index route equal to retrieve function ht, route index - 1

    # return route

    # test tickets
