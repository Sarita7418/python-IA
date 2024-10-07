import itertools

def is_magic_square(square, n, magic_number):
    
    for row in square:
        if sum(row) != magic_number:
            return False
    
    for col in range(n):
        if sum(square[row][col] for row in range(n)) != magic_number:
            return False
    
    main_diagonal = sum(square[i][i] for i in range(n))
    secondary_diagonal = sum(square[i][n-i-1] for i in range(n))
    
    if main_diagonal != magic_number or secondary_diagonal != magic_number:
        return False
    
    return True

def generate_magic_squares(n):
    numbers = list(range(1, n**2 + 1))
    
    magic_number = n * (n**2 + 1) // 2
    
    print(f"Magic number = {magic_number}")
    
    for perm in itertools.permutations(numbers):
        
        square = [[perm[i * n + j] for j in range(n)] for i in range(n)]
        if is_magic_square(square, n, magic_number):
            print(f"Magic Square:")
            for row in square:
                print(row)
            print()

n = int(input("Please give me the square's dimension (n): "))
generate_magic_squares(n)
