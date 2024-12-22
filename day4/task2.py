def load_data(input_file) -> list[list]:
    with open(input_file, 'r') as file:
        data = file.read()
    return data

def find_xmas_occurance(data) -> int:
    total_xmas_occurances = 0
    input_lines = data.split('\n')
    horizontal_length = len(input_lines[0])
    vertical_length = len(input_lines)

    for row in range(vertical_length - 2):
        for col in  range(horizontal_length - 2):
            valid_right_diagonal = False
            valid_left_diagonal = False
            
            # check right diagonal
            right_diagonal = input_lines[row][col] + input_lines[row + 1][col + 1] + input_lines[row + 2][col + 2]
            if (right_diagonal == "MAS"
                or right_diagonal == "SAM"):
                valid_right_diagonal = True
                
            # check left diagonal
            left_diagonal = input_lines[row][col+2] + input_lines[row + 1][col + 1] + input_lines[row + 2][col]
            if (left_diagonal == "MAS"
                or left_diagonal == "SAM"):
                valid_left_diagonal = True
            
            # evaluate possible xmas in current position
            if valid_right_diagonal and valid_left_diagonal:
                total_xmas_occurances += 1
            
            
    return total_xmas_occurances            

data = load_data('day4/task1_test.txt')
# print(data)

print(find_xmas_occurance(data))

data = load_data('day4/test2.txt')
# print(data)

print(find_xmas_occurance(data))