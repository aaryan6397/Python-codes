def second_largest_smallest(nums):

    smallest = largest = nums[0]
    second_smallest = second_largest = nums[0]

    for num in nums:

        if num < smallest:
            second_smallest = smallest
            smallest = num

        elif num < second_smallest or second_smallest == smallest:
            second_smallest = num

        if num > largest:
            second_largest = largest
            largest = num

        elif num > second_largest or second_largest == largest:
            second_largest = num

    return second_smallest, second_largest


numbers = [10, 5, 20, 8, 15]

s_small, s_large = second_largest_smallest(numbers)

print("Second Smallest =", s_small)
print("Second Largest =", s_large)