# https://www.geeksforgeeks.org/puzzle-15-camel-and-banana-puzzle/
# A person has 3000 bananas and a camel. The person wants to transport maximum
# number of bananas to a destination which is 1000 KMs away, using only the
# camel as a mode of transportation. The camel cannot carry more than 1000
# bananas at a time and eats a banana every km it travels. What is the maximum
# number of bananas that can be transferred to the destination using only
# camel (no other mode of transportation is allowed).

# There are 2 ways to think about about. The key is that if we move too far in
# one move, then we lose a lot of bananas. So the best shot is that we move
# all bananas 1 km at a time.
def __move_1(bananas, distance, capacity):
    # return bananas after traveling the distance
    if bananas <= 0 or distance <= 0:
        return 0  # recursion base

    if bananas < distance:
        raise Exception(f'no enough bananas: {bananas} to cover distance {distance} !')

    if bananas <= capacity:
        return bananas - distance

    if bananas - capacity <= 2 * distance:  # not worth to come back
        return capacity - distance

    # make one move and then recursion
    return capacity - 2 * distance + __move_1(bananas - capacity,
                                              distance, capacity)


def transport_1(bananas, distance, capacity):
    """ return how many left after traveling the distance """
    left = bananas
    for i in range(distance):
        print(f'move 1 km from {i}, with {left} bananas')
        left = __move_1(left, 1, capacity)

    return left


# Test, uncomment to run
print(transport_1(3010, 1000, 1000))

# Obviously, in the case of the last 1000 bananas we could jump to the
# destination with one move.
# Now, the question is how far can we jump? This depends on the number of
# bananas. If we have 3000 bananas, then at least we need 3 round trips
# to move them (the last travel is not needed to come back). So we need
# 5 travels. If we have 2000 bananas, then we need only 3 travels.
# http://codinginterviewquestionsans.blogspot.com/2018/01/camel-and-bananas-puzzle.html
import math


# basically, if we have 4321 bananas, first we get to 4000 bananas with some
# disitance, then to 3000, 2000, 1000
def transport(bananas, distance, capacity):
    to_goal = distance
    left = bananas
    # this formula causes rounding error (3010 gives wrong result)
    # this need more consideration.
    # On the other hand, first version is always right.
    trips = int(math.ceil(bananas / capacity)) * 2 - 1
    print(f'bananas={bananas}, goal={to_goal}')

    # we need extra logic if bananas is not multiple of capacity
    if bananas % capacity > 0:
        trip = math.floor((bananas % capacity) / trips)  # if we use //, then there will be rounding error.

        to_goal -= trip
        left -= trip * trips
        print(f'bananas={left}, goal={to_goal}, trips={trips}, travel={trip}')
        trips -= 2

    while trips > 1:
        trip = round(capacity / trips)  # if we use //, then there will be rounding error.

        to_goal -= trip
        # we drop the extra bananas since they are not worth coming back
        if left > capacity * round(left / capacity):
            left = left // capacity * capacity

        left -= trip * trips
        print(f'bananas={left}, goal={to_goal}, trips={trips}, travel={trip}')
        trips -= 2  # When we reduce one capacity(1000), we reduce 2 trips.

    if left > capacity * round(left / capacity):
        left = left // capacity * capacity

    print(f'bananas={left - to_goal}, goal={0}, trips={trips}, travel={to_goal}')
    return left - to_goal


print(transport(3000, 1000, 1000))
print(transport(3010, 1000, 1000))
print(transport(3200, 1000, 1000))
print(transport(5000, 1500, 1000))
