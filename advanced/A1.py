#Read doc.txt file using Python File handling concept and return only the even length
#string from the file. Consider the content of doc.txt as given below:
#Hello I am a file
#Where you need to return the data string
#Which is of even length
#Make sure you return the content in The same link as it is present.

def get_even_length_strings(filename):
    try:
        with open(filename, 'r') as file:
            # Read all lines from the file
            lines = file.readlines()

            even_length_strings = []

            for line in lines:
                words = line.split()
                for word in words:
                    if len(word) % 2 == 0:
                        even_length_strings.append(word)

            return even_length_strings

    except FileNotFoundError:
        print(f"File {filename} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


filename = 'doc.txt'
result = get_even_length_strings(filename)

if result:
    print("Even-length strings in the file:")
    print(result)
