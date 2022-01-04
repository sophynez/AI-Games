import math

def negamax(elem, leaves, actual_depth, depth):
    if actual_depth == depth:
        return leaves[elem]
    else:
        s = max(-negamax(elem*2, leaves, actual_depth+1, depth), -negamax(elem*2+1, leaves, actual_depth+1, depth))
        return s


def minmax(elem, leaves, turn, _actual_nbr_of_turns, nbr_of_turns):

    if _actual_nbr_of_turns == nbr_of_turns:
        return leaves[elem]
    else:
        if turn == max :
            return max(minmax(elem*2, leaves, min, _actual_nbr_of_turns+1, nbr_of_turns), minmax(elem*2+1, leaves, min, _actual_nbr_of_turns+1, nbr_of_turns))
        elif turn == min:
            return min(minmax(elem*2, leaves, max, _actual_nbr_of_turns+1, nbr_of_turns), minmax(elem*2+1, leaves, max, _actual_nbr_of_turns+1, nbr_of_turns))

list = [15, 6, 3, 12, 42, 45, 42, 39, -9, 66, 27, 36, 33, 30, 61, 60]
list2 = [9, 15, 18, 6, 3, 12, 21, 24]
# in reality, number of turns represents the depth of the "tree", so we get that by calculating the log2 of len on our list according the the exercice given
depth_tree = math.log(len(list), 2)

print(depth_tree)
print(minmax(0, list, max, 0, depth_tree))
print(negamax(0, list, 0, depth_tree))



# amelioration : write function which returns depth of any given tree and not only binary trees