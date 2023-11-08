n1 = [x for x in range(10) if x % 2 == 0]
n2 = [x for x in range(10) if x % 2 != 0]
# n1 is even 0-8, 0,2,4,6,8
# n2 is odd 1-9, 1,3,5,7,9

zipped = list(zip(n1, n2))
# list is [(0,1),(2,3),(4,5),(6,7),(8,9)]
# print(zipped)

zipped_2 = zipped[::-1]
# steps from the end of the list (reverses list)

zipped_2.extend(n2[::-1])
# unsure
# print(zipped_2.extend(n2[::-1]))
# prints none, object is not iterable

n1[-5:-5] = [999]
# modifies value of n1 at index 5th from the end to 999, n1 = [999, 0, 2, 4, 6, 8]
# print(n1)

n1[1:4] = ['a', 'b', 'c']
# modifies list n1 from index 1,2,3, ending at 4 to the given values,
# n1 = [999, 'a', 'b', 'c', 6, 8]
# print(n1)

lst = sorted(n1, key=lambda x: (isinstance(x, int), x), reverse=True)
# sorts n1 with integers first, reversed in value order
# n1 = [999,8,6,'c','b','a']

print(lst)
