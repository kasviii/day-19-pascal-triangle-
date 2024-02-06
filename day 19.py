def generate_pascals_triangle(height):
    triangle = []
    for i in range(height):
        row = [1]
        if i > 0:
            for j in range(1, i):
                row.append(triangle[i-1][j-1] + triangle[i-1][j])
            row.append(1)
        triangle.append(row)
    return triangle

def main():
    height = int(input("Enter the height of Pascal's triangle: "))
    pascals_triangle = generate_pascals_triangle(height)
    for row in pascals_triangle:
        print(row)

if __name__ == "__main__":
    main()
