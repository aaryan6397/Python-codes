try:
    source = input("Enter source file name: ")
    destination = input("Enter destination file name: ")

    # Open source file
    file1 = open(source, "r")
    content = file1.read()

    # Count words
    word_count = len(content.split())

    # Write to destination file
    file2 = open(destination, "w")
    file2.write(content)

    # Close files
    file1.close()
    file2.close()

    print("File copied successfully!")
    print("Total words copied:", word_count)

except FileNotFoundError:
    print("Source file not found.")

except Exception as e:
    print("Error:", e)