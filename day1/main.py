
total = 0

# Open the file in read mode
with open('data.txt', 'r') as file:
    a = []
    b = []
    for line in file:
        # Process each line (line will include the newline character at the end)
        arr = list(map(int, line.split())) # Use .strip() to remove the newline character
        a.append(arr[0])
        b.append(arr[1])

a.sort()
b.sort()
for i in range(len(a)):
    total += abs(b[i] - a[i])

print(total)
