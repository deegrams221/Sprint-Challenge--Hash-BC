#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)

"""
* A brute-force solution would involve two nested loops, yielding a quadratic-runtime solution. How can we use a hash table in order to implement a solution with a better runtime?
* Think about what we can store in the hash table in order to help us to solve this problem more efficiently.
* What if we store each weight in the input list as keys? What would be a useful thing to store as the value for each key?
* If we store each weight's list index as its value, we can then check to see if the hash table contains an entry for `limit - weight`. If it does, then we've found the two items whose weights sum up to the `limit`!
"""
def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    """
    # print the weights, length, and limit
    print(f"WEIGHT: {weights}")
    print(f"LENGTH: {length}")
    print(f"LIMIT: {limit}")

    # for the index in the range of length
    for index in range(length):
        # set check weight to hash table retrieve `limit - weight`
        check_weight = hash_table_retrieve(ht, limit - weights[index])
        # check for None
        if check_weight is None:
            # then return hash table insert
            hash_table_insert(ht, weights[index], index)
            # then print
            print(f"WEIGHT INDEX: {index} VALUE: {weights[index]}")
        # otherwise
        else:
            # return the index, and weight check
            return (index, check_weight)

    # return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")

# test -> it works!!! HAHAH it's ALIVE!
test_weights = [2, 4, 5, 6, 8]
print(get_indices_of_item_weights(test_weights, 5, 21))