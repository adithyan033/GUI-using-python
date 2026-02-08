rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

matrix = []

print("Enter the matrix elements:")

for i in range(rows):
    row = []
    for j in range(cols):
        element = int(input(f"Element [{i}][{j}]: "))
        row.append(element)
    matrix.append(row)

print("\nMatrix is:")
for row in matrix:
    for element in row:
        print(element, end=" ")
    print()
