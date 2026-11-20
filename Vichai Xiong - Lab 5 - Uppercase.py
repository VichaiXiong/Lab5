#convert all characters to uppercase from the old text file into a new text file

with open("regular.txt", "r") as regular_file:
    with open("uppercase.txt", "w") as uppercase_file:
        for text in regular_file:
            uppercase_file.write(text.upper())
    