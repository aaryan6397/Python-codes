# enter salaries as space separated values, for example: 12000 25000 60000 8000 45000
salaries = list(map(int, input("Enter salaries: ").split()))

valid_salaries = []
for s in salaries:
    if s >= 10000:   # minimum wage
        if s > 50000:
            s = s + (0.05 * s)
            # add 5% bonus for salaries greater than 50000
        valid_salaries.append(s)
# sort the valid salaries in descending order
valid_salaries.sort(reverse=True)
# print the top 3 salaries
print("Top 3 Salaries:", valid_salaries[:3])

'''output:
Enter salaries: 12000 25000 60000 8000 45000
Top 3 Salaries: [63000.0, 45000, 25000
Enter salaries: 9000 15000 55000 7000 30000
Top 3 Salaries: [57750.0, 30000, 15000
Enter salaries: 8000 9000 10000 11000 12000
Top 3 Salaries: [12000, 11000, 10000'''