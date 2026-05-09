
import sqlite3
import time
from plyer import notification
from playsound import playsound

# Database Connection
conn = sqlite3.connect("medicine.db")
cursor = conn.cursor()

# Create Table
cursor.execute('''
CREATE TABLE IF NOT EXISTS medicines (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    med_time TEXT
)
''')

conn.commit()


def add_medicine():
    name = input("Enter Medicine Name: ")
    med_time = input("Enter Time (HH:MM format): ")

    cursor.execute(
        "INSERT INTO medicines (name, med_time) VALUES (?, ?)",
        (name, med_time)
    )

    conn.commit()

    print("Medicine Added Successfully!\n")


def view_medicines():
    cursor.execute("SELECT * FROM medicines")
    data = cursor.fetchall()

    if len(data) == 0:
        print("No Medicine Records Found!")

    else:
        print("\n===== Medicine Records =====")

        for row in data:
            print(f"ID: {row[0]}")
            print(f"Medicine Name: {row[1]}")
            print(f"Medicine Time: {row[2]}")
            print("---------------------------")


def start_reminder():
    print("\nReminder System Started...")

    while True:
        current_time = time.strftime("%H:%M")

        cursor.execute("SELECT name FROM medicines WHERE med_time=?",
                       (current_time,))

        medicines = cursor.fetchall()

        for medicine in medicines:

            print(f"⏰ Time to take: {medicine[0]}")

            # Desktop Notification
            notification.notify(
                title="Medicine Reminder",
                message=f"Take your medicine: {medicine[0]}",
                timeout=10
            )

            # Alarm Sound
            try:
                playsound("alarm.mp3")
            except:
                print("Alarm sound file not found!")

        time.sleep(60)


while True:

    print("\n===== Smart Medicine Reminder System =====")
    print("1. Add Medicine")
    print("2. View Medicines")
    print("3. Start Reminder")
    print("4. Exit")

    choice = input("Enter Your Choice: ")

    if choice == '1':
        add_medicine()

    elif choice == '2':
        view_medicines()

    elif choice == '3':
        start_reminder()

    elif choice == '4':
        print("Project Closed Successfully!")
        break

    else:
        print("Invalid Choice!")

conn.close()
