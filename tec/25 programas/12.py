import itertools

numbers = [1, 2, 3]
permutations = list(itertools.permutations(numbers))

for permutation in permutations:
    print(list(permutation))
