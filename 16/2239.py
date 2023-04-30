sudoku = [list(map(int, input())) for _ in range(9)]
zeros = [(i,j) for i in range(9) for j in range(9) if not sudoku[i][j]]

def go(n):
    if n == len(zeros):
        for a in sudoku:
            print(*a, sep='')
        exit()
        
    x, y = zeros[n]
    a, b = x // 3 * 3, y // 3 * 3
    numbers = set([i for i in range(1, 10)])
    
    for i in range(a, a+3):
        for j in range(b, b+3):
            numbers.discard(sudoku[i][j])
    
    for i in range(9):
        numbers.discard(sudoku[x][i])
        numbers.discard(sudoku[i][y])
    
    for number in numbers:
        sudoku[x][y] = number
        go(n+1)
    sudoku[x][y] = 0

go(0)
