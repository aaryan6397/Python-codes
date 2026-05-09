try:
    filename = input("Enter file name: ")

    file = open(filename, "r")

    content = file.read()

    lines = content.splitlines()
    words = content.split()
    characters = len(content)

    print("Total Lines:", len(lines))
    print("Total Words:", len(words))
    print("Total Characters:", characters)

    file.close()

except FileNotFoundError:
    print("Error: File not found.")

except Exception as e:
    print("Unexpected Error:", e)