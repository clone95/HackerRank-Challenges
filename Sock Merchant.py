# John works at a clothing store. He has a large pile of socks that he must pair by color for sale. Given an array of
# integers representing the color of each sock, determine how many pairs of socks with matching colors there are.
#
# For example, there are  socks with colors . There is one pair of color  and one of color . There are three odd socks
#  left, one of each color. The number of pairs is .
#
# Function Description
#
# Complete the sockMerchant function in the editor below. It must return an integer representing the number of matching
#  pairs of socks that are available.
#
# sockMerchant has the following parameter(s):
#
# n: the number of socks in the pile
# ar: the colors of each sock

#
# The first line contains an integer , the number of socks represented in .
# The second line contains  space-separated integers describing the colors of the socks in the pile.
#
# Constraints
#
#  where
# Output Format
#
# Print the total number of matching pairs of socks that John can sell.


input_socks = [9, [1, 2, 2, 1, 1, 1, 1, 1, 1, 3, 5, 1, 2]]


def main(socks):
    couples = 0
    pairs_from_colour = 0
    pairs = 0
    colours = dict()
    for el in socks[1]:
        if el in colours.keys():
            colours[el] += 1
        else:
            colours[el] = 1

    for colour in colours.keys():

        pairs_from_colour = colours[colour] / 2
        pairs += int(pairs_from_colour)

    return pairs


if __name__ == '__main__':
    print(main(input_socks))


