def load_data(input_file) -> list[list]:
    with open(input_file, 'r') as file:
        data = file.read()
    return data
    
def check_horizontal(input_lines, row, col):
    potential_word = input_lines[row][col] + input_lines[row][col+1] + input_lines[row][col+2] + input_lines[row][col+3]
    if potential_word == "XMAS" or potential_word == "SAMX":
        return True
    return False
    
    
def check_vertical(input_lines, row, col):
    potential_word = input_lines[row][col] + input_lines[row+1][col] + input_lines[row+2][col] + input_lines[row+3][col]
    if potential_word == "XMAS" or potential_word == "SAMX":
        return True
    return False

def check_right_diagonal(input_lines, row, col):
    potential_word = input_lines[row][col] + input_lines[row+1][col+1] + input_lines[row+2][col+2] + input_lines[row+3][col+3]
    if potential_word == "XMAS" or potential_word == "SAMX":
        return True
    return False

def check_left_diagonal(input_lines, row, col):
    potential_word = input_lines[row][col] + input_lines[row+1][col-1] + input_lines[row+2][col-2] + input_lines[row+3][col-3]
    if potential_word == "XMAS" or potential_word == "SAMX":
        return True
    return False

def find_xmas_occurance(data) -> int:
    total_xmas_occurances = 0
    input_lines = data.split('\n')
    horizontal_length = len(input_lines[0])
    vertical_length = len(input_lines)
    
    # check each element for potential substring
    
    # horizontal
    for row in range(vertical_length):
        for col in range(horizontal_length - 3):
            if check_horizontal(input_lines, row, col): total_xmas_occurances += 1
    
    # vertical
    for row in range(vertical_length - 3):
        for col in range(horizontal_length):
            if check_vertical(input_lines, row, col): total_xmas_occurances += 1
            
    # right diagonal
    for row in range(vertical_length - 3):
        for col in range(horizontal_length - 3):
            if check_right_diagonal(input_lines, row, col): total_xmas_occurances += 1
            
    # left diagonal
    for row in range(vertical_length - 3):
        for col in range(3, horizontal_length):
            if check_left_diagonal(input_lines, row, col): total_xmas_occurances += 1
    
            
    return total_xmas_occurances            

data = load_data('day4/task1_test.txt')
# print(data)

print(find_xmas_occurance(data))

data = load_data('day4/test.txt')
# print(data)

print(find_xmas_occurance(data))