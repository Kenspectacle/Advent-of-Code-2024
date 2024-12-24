def load_data(input_file) -> list:
    with open(input_file, 'r') as file:
        equations = file.read().split('\n')
        test_values = []
        operands = []
        for equation in equations:
            equation = equation.split(' ')
            test_values.append(equation[0][:-1])
            operands.append(equation[1:])
        operands = [[int(el) for el in operand] for operand in operands]
        test_values = [int(test_value) for test_value in test_values]
        
    return test_values, operands

def check_row_calibrated(test_value, operands, operator, current, pointer) -> bool:
    if current == test_value:
        return True
    elif pointer >= len(operands):
        return False
    
    match operator:
        case "+":
            current += operands[pointer]
        case "*":
            current *= operands[pointer]
        case "||":
            current = str(current)
            temp = str(operands[pointer])
            current += temp
            current = int(current)
    
    pointer += 1
    
    return (
        check_row_calibrated(test_value, operands, "+", current, pointer)
        or
        check_row_calibrated(test_value, operands, "*", current, pointer)
        or
        check_row_calibrated(test_value, operands, "||", current, pointer)
    )
    

def find_total_calibration_result(test_values, operands) -> int:
    total = 0
    for i in range(len(operands)):
        # check for each row
        is_valid = check_row_calibrated(test_values[i], operands[i], "+", 0, 0)
        if is_valid:
            total += test_values[i]
        
    
    return total


# test_values, operands = load_data('day7/test.txt')
# print (find_total_calibration_result(test_values, operands))

test_values, operands = load_data('day7/task1_test.txt')
print (find_total_calibration_result(test_values, operands))