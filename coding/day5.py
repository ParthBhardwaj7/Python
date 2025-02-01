# Define a lambda function to add two numbers
add = lambda a, b: a + b

# Use the lambda function
result = add(5, 3)
print(result)  # Output: 8

pairs = [(1, 3), (4, 1), (2, 8)]
sorted_pairs = sorted(pairs, key=lambda x: x[1])

print(sorted_pairs)  # Output: [(4, 1), (1, 3), (2, 8)]

numbers = [1, 2, 3, 4]
doubled = list(map(lambda x: x * 2, numbers))

print(doubled)  # Output: [2, 4, 6, 8]

numbers = [1, 2, 3, 4, 5]
evens = list(filter(lambda x: x % 2 == 0, numbers))

print(evens)  # Output: [2, 4]
