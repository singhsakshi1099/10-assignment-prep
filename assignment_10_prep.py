# -*- coding: utf-8 -*-
"""assignment 10 prep

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jRgOWOid4PSvvTNz9qqwNy8q_ge5SapQ
"""

#solution 1

def isPowerOfThree(n):
    if n <= 0:
        return False
    while n % 3 == 0:
        n //= 3
    return n == 1

#solution2

def lastRemaining(n):
    remaining = 1
    step = 1
    left_to_right = True

    while n > 1:
        if left_to_right:
            remaining += step
        else:
            remaining += (n % 2) * step

        n //= 2
        left_to_right = not left_to_right
        step *= 2

    return remaining

#solution3

def generateSubsets(set_str):
    subsets = []
    generateSubsetsRecursive(set_str, "", 0, subsets)
    return subsets

def generateSubsetsRecursive(set_str, current_subset, index, subsets):
    if index == len(set_str):
        subsets.append(current_subset)
        return

    # Recursive call without including the current character
    generateSubsetsRecursive(set_str, current_subset, index + 1, subsets)

    # Recursive call including the current character
    generateSubsetsRecursive(set_str, current_subset + set_str[index], index + 1, subsets)

    print(generateSubsets("abc"))

#solution 3

def calculateLength(str):
    if str == "":
        return 0
    else:
        return 1 + calculateLength(str[1:])

print(calculateLength("abcd"))
print(calculateLength("GEEKSFORGEEKS"))

#solution 4

def countContiguousSubstrings(S):
    count = 0
    prev_char = ''
    for char in S:
        if char == prev_char:
            count += 1
        else:
            count = 1
        prev_char = char
    return count
print(countContiguousSubstrings("abcab"))

#solution 6

def towerOfHanoi(n, source, destination, auxiliary):
    if n == 1:
        print("move disk 1 from rod", source, "to rod", destination)
        return 1
    else:
        moves = 0
        moves += towerOfHanoi(n - 1, source, auxiliary, destination)
        print("move disk", n, "from rod", source, "to rod", destination)
        moves += 1
        moves += towerOfHanoi(n - 1, auxiliary, destination, source)
        return moves

N = 2
total_moves = towerOfHanoi(N, 1, 3, 2)
print(total_moves)

#7 solution

def printPermutations(str):
    permutations = []
    generatePermutations(list(str), 0, len(str) - 1, permutations)
    return permutations

def generatePermutations(str_list, left, right, permutations):
    if left == right:
        permutations.append("".join(str_list))
    else:
        for i in range(left, right + 1):
            str_list[left], str_list[i] = str_list[i], str_list[left]
            generatePermutations(str_list, left + 1, right, permutations)
            str_list[left], str_list[i] = str_list[i], str_list[left]  # Backtrack

print(printPermutations("cd"))

#8 solution

def countConsonants(string):
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    count = 0
    for char in string:
        if char in consonants:
            count += 1
    return count

print(countConsonants("Hello, World!"))

