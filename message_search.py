import time

start = time.time()
result = 0
lines = 0
magic_string = "replace_this" # Change this string based on what you're searching for. Everything MUST be lowercase for it to search all cases of the word.

for index in range(32): # Change the number in the range function to the total number of message files you have.
    file = open(f"message_{index + 1}.json", "r") # Replace the path to the chat folder here. Don't overwrite the filename part you see here.
    for line in file:
        lines += 1
        if magic_string in line.lower():
            result += 1
    file.close()

print (f"Total chat messages: {result}")
print (f"Search for string: {magic_string}. Number of results: {result}")
end = time.time()
print (f"Lines counted: {lines}. Calculated in: {round((end - start), 4)} seconds.")