def load_data(input_file) -> list[list]:
    with open(input_file, 'r') as file:
        data = file.read()
    return data

def parse_mul(data) -> int:
    res = 0
    
    # init
    state = "START"
    parse_mode_enable = True
    number_one = ""
    number_two = ""
    parsing_fail = False
    parsing_done = False
    digits = ['0','1','2','3','4','5','6','7','8','9']

    for char in data:
        print(f'processing: {char}')
        
        # print(f'current status:\n'
        #       f'number_one: {number_one}\n'
        #       f'number_two: {number_two}\n'
        #       f'parsing_fail: {parsing_fail}\n'
        #       f'parsing_done: {parsing_done}')
        
        if parsing_fail:
            state = "START"
            number_one = ""
            number_two = ""
            parsing_fail = False
            parsing_done = False

        match state:
            # mul(num1, num2)
            case "START":
                if char == "m" and parse_mode_enable:
                    state = "M_FOUND"
                # do() and don't()
                if char == "d":
                    state = "D_FOUND"
            case "M_FOUND":
                if char == "u":
                    state = "U_FOUND"
                else:
                    parsing_fail = True
            case "U_FOUND":
                if char == "l":
                    state = "L_FOUND"
                else:
                    parsing_fail = True
            case "L_FOUND":
                if char == "(":
                    state = "LEFT_PAR_MUL_FOUND"
                else:
                    parsing_fail = True
            case "LEFT_PAR_MUL_FOUND":
                if char in digits:
                    state = "LEFT_NUMBER"
                    number_one += char
                else:
                    parsing_fail = True
            case "LEFT_NUMBER":
                if char in digits:
                    number_one += char
                elif char == ",":
                    state = "COMMA_FOUND"
                else:
                    parsing_fail = True
            case "COMMA_FOUND":
                if char in digits:
                    state = "RIGHT_NUMBER"
                    number_two += char
            case "RIGHT_NUMBER":
                if char in digits:
                    number_two += char
                elif char == ")":
                    state = "RIGHT_PAR_MUL_FOUND"
                    parsing_done = True
                else:
                    parsing_fail = True
                    
            # do/don't
            case "D_FOUND":
                if char == "o":
                    state = "O_FOUND"
                else:
                    parsing_fail = True
            case "O_FOUND":
                if char == "(":
                    state = "LEFT_PAR_DO_FOUND"
                elif char == "n":
                    state = "DON_FOUND"
                else:
                    parsing_fail = True
            case "LEFT_PAR_DO_FOUND":
                if char == ")":
                    state = "START"
                    parse_mode_enable = True
                else:
                    parsing_fail = True
            case "DON_FOUND":
                if char == "'":
                    state = "DON'_FOUND"
                else:
                    parsing_fail = True
            case "DON'_FOUND":
                if char == "t":
                    state = "DON'T_FOUND"
                else:
                    parsing_fail = True
            case "DON'T_FOUND":
                if char == "(":
                    state = "LEFT_PAR_DON'T_FOUND"
                else:
                    parsing_fail = True
            case "LEFT_PAR_DON'T_FOUND":
                if char == ")":
                    state = "START"
                    parse_mode_enable = False
                else:
                    parsing_fail = True
                
                    
                    
        if parsing_done:
            print('parsing is done!')
            current_mult = int(number_one) * int(number_two)
            print(f'adding {current_mult} into res {res}')
            res += current_mult
            number_one = ""
            number_two = ""
            parsing_fail = False
            parsing_done = False
            state = "START"
    return res
                         
                      

data = load_data('task2_input.txt')
print(data)

print(parse_mul(data))