points = list(map(int, input("Enter team points: ").split()))

for i in range(len(points)):
    if points[i] < 0:
        points[i] = 0
# sort the points in descending order
points.sort(reverse=True)

# print the winner and runner-up points
print("Winner Points:", points[0])
# check if there are at least 2 teams to determine runner-up
if len(points) > 1:
   # print the runner-up points
    print("Runner-up Points:", points[1])
    # print the leaderboard
print("Leaderboard:", points)