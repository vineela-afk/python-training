def readfr(filename):
    '''
    to read a file
    '''
    try:
        with open(filename, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        print(f"error file '{filename}' not found")
    except IOError:
        print("cant read file")


def writeto(filename, content):
    '''
    to write to a file
    '''
    try:
        with open(filename, 'w') as file:
            file.write(content)
            print("Written")
    except IOError:
        print("cant write file")


filename = "abcd.txt"
file_read = readfr(filename)

if file_read:
    print("content: " + file_read)
    
text = "i am inside write file"
writeto(filename, text)
    