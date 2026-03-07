# WAP in python to create a movie rating system that takes a list of ratings as input and calculates the average rating, counts the number of 5 star ratings, and sorts the ratings in ascending order.


# enter ratings as space separated values, for example: 5 4 3 5 2 1
ratings = list(map(int, input("Enter ratings (1-5): ").split()))

# create a list to store valid ratings
valid = []
# iterate through the ratings and check if they are valid (between 1 and 5)
for r in ratings:
    if 1 <= r <= 5:
        # if the rating is valid, add it to the valid list
        valid.append(r)

if len(valid) == 0:
    # if there are no valid ratings, print a message
    print("No valid ratings.")
else:
    # calculate average rating
    print("Average Rating:", sum(valid)/len(valid))
    # count the number of 5 star ratings
    print("5 Star Ratings:", valid.count(5))

    # sort the valid ratings in ascending order
    valid.sort()
    # print the sorted ratings
    print("Sorted Ratings:", valid)

    '''output:
    Enter ratings (1-5): 5 4 3 5 2 1
    Average Rating: 3.33
    5 Star Ratings: 2
    Sorted Ratings: [1, 2, 3, 4, 5, 5]
    '''
