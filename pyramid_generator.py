# CT_SD_02 - Advanced Pattern Generator

def generate_pyramid(pyramid_type, size):
    if pyramid_type == 1:  # Standard Pyramid
        for i in range(1, size+1):
            print(" "*(size-i) + " ".join(str(j%10) for j in range(1, i+1)))
    
    elif pyramid_type == 2:  # Inverted Pyramid
        for i in range(size, 0, -1):
            print(" "*(size-i) + " ".join(str(j%10) for j in range(1, i+1)))
    
    elif pyramid_type == 3:  # Left-Aligned Pyramid
        for i in range(1, size+1):
            print(" ".join(str(j%10) for j in range(1, i+1)))
    
    elif pyramid_type == 4:  # Binary Pyramid
        for i in range(1, size+1):
            binary_str = " ".join([str(j%2) for j in range(1, i+1)])
            print(" "*(size-i) + binary_str)

def generate_diamond(size):
    for i in range(1, size+1):
        print(" "*(size-i) + " ".join(str(j%10) for j in range(1, i+1)))
    for i in range(size-1, 0, -1):
        print(" "*(size-i) + " ".join(str(j%10) for j in range(1, i+1)))

def generate_spiral(size):
    matrix = [[0]*size for _ in range(size)]
    num = 1
    top, left = 0, 0
    bottom, right = size-1, size-1

    while top <= bottom and left <= right:
        for i in range(left, right+1):
            matrix[top][i] = num % 10
            num += 1
        top += 1

        for i in range(top, bottom+1):
            matrix[i][right] = num % 10
            num += 1
        right -= 1

        if top <= bottom:
            for i in range(right, left-1, -1):
                matrix[bottom][i] = num % 10
                num += 1
            bottom -= 1

        if left <= right:
            for i in range(bottom, top-1, -1):
                matrix[i][left] = num % 10
                num += 1
            left += 1

    for row in matrix:
        print(" ".join(map(str, row)))

def show_pyramid_menu(size):
    print("\nPyramid Types:")
    print("1. Standard Pyramid")
    print("2. Inverted Pyramid")
    print("3. Left-Aligned Pyramid")
    print("4. Binary Pyramid")
    
    while True:
        try:
            choice = int(input("Select pyramid type (1-4): "))
            if 1 <= choice <= 4:
                print(f"\nGenerating {['Standard', 'Inverted', 'Left-Aligned', 'Binary'][choice-1]} Pyramid (Size: {size}):\n")
                generate_pyramid(choice, size)
                break
            else:
                print("Please enter a number between 1-4")
        except ValueError:
            print("Invalid input! Please enter a number.")

def show_diamond_menu(size):
    print("\nGenerating Diamond Pattern:\n")
    generate_diamond(size)

def show_spiral_menu(size):
    print("\nGenerating Spiral Pattern:\n")
    generate_spiral(size)

def main():
    print("""
    ===== ADVANCED PATTERN GENERATOR =====
    Main Categories:
    1. Pyramids
    2. Diamonds
    3. Spirals
    """)
    
    while True:
        try:
            category = int(input("Select category (1-3): "))
            if category not in (1, 2, 3):
                raise ValueError
            size = int(input("Enter size (1-9): "))
            if not 1 <= size <= 9:
                raise ValueError
            break
        except ValueError:
            print("Invalid input! Please enter valid numbers.\n")
    
    if category == 1:
        show_pyramid_menu(size)
    elif category == 2:
        show_diamond_menu(size)
    elif category == 3:
        show_spiral_menu(size)

if __name__ == "__main__":
    main()