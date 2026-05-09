#include <iostream>
using namespace std;

int main() {
    float s1, s2, s3, s4, s5;
    float total, percentage;

    // Input marks
    cout << "Enter marks of 5 subjects: ";
    cin >> s1 >> s2 >> s3 >> s4 >> s5;

    // Calculate total and percentage
    total = s1 + s2 + s3 + s4 + s5;
    percentage = total / 5;

    cout << "\nTotal Marks = " << total;
    cout << "\nPercentage = " << percentage << "%";

    // Grade calculation using nested if-else
    if (percentage >= 90) {
        cout << "\nGrade = A+";
    }
    else {
        if (percentage >= 75) {
            cout << "\nGrade = A";
        }
        else {
            if (percentage >= 60) {
                cout << "\nGrade = B";
            }
            else {
                if (percentage >= 40) {
                    cout << "\nGrade = C";
                }
                else {
                    cout << "\nGrade = Fail";
                }
            }
        }
    }

    // Scholarship eligibility
    if (percentage >= 85) {
        cout << "\nScholarship Status: Eligible";
    }
    else {
        cout << "\nScholarship Status: Not Eligible";
    }

    return 0;
}