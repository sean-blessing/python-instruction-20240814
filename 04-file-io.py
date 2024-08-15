# p. 97

# p.103 - reading_files.py examples
# simple open and close
FILE_NAME = './files/test-file.txt'
file_in = open(FILE_NAME)
# reading in the file
file_in.close()

# open a file, iterate over the lines, strip whitespace, print line
# using 'with' eliminates need for 'close'
with open(FILE_NAME) as file_in:
    # iterate over the lines in the file
    for raw_line in file_in:
        #print(f'raw_line: {raw_line}')
        # remove whitespace
        line = raw_line.rstrip()
        print(f'line: {line}')
print("=" * 40)

# read entire file into one string
with open(FILE_NAME) as file_in:
    contents = file_in.read()
    print("NORMAL: ")
    print(contents)
    print("RAW:")
    print(repr(contents))
print("=" * 40)

# read all lines into an array

# read into array but get rid of newline

# p. 107 writing to a text file
states = (
    'Ohio',
    'Indiana',
    'Colorado',
    'Alabama'
)





