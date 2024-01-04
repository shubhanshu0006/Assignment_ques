#Write a program to count the the lines in a file “demo.txt
def count_lines(filename):
    try:
        with open(filename, 'r') as file:
            # Read all lines from the file
            lines = file.readlines()

            # Count the number of lines
            line_count = len(lines)

            print(f"The number of lines in {filename} is: {line_count}")

    except FileNotFoundError:
        print(f"File {filename} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


count_lines('demo.txt')
