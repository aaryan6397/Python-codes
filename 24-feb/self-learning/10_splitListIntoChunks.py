# Q10: Split a list into chunks of a given size
# Input: [1, 2, 3, 4, 5, 6, 7, 8, 9], chunk_size = 3
# Output: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
chunk_size = 3

chunks = []
for i in range(0, len(numbers), chunk_size):
    chunks.append(numbers[i:i + chunk_size])

print("Original List:", numbers)
print("Chunk Size:", chunk_size)
print("Chunks:", chunks)

# Output:
# Original List: [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Chunk Size: 3
# Chunks: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]