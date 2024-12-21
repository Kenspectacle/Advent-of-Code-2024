def load_data(input_file) -> list[list]:
    with open(input_file, 'r') as file:
        data = file.read()
    return data

def parse_mul(data) -> int:
    res = 0
    
    # init
    in_parsing = False
    has_m = False
    has_u = False
    has_l = False
    has_left_par = False
    has_number_one = False
    has_comma = False
    has_number_two = False
    has_right_par = False
    number_one = ""
    number_two = ""
    parsing_fail = False
    parsing_done = False
    
    digits = ['0','1','2','3','4','5','6','7','8','9']

    for char in data:
        print(f'processing: {char}')
        
        # print(f'current status:\n'
        #       f'has_m: {has_m}\n'
        #       f'has_u: {has_u}\n'
        #       f'has_l: {has_l}\n'
        #       f'has_left_par: {has_left_par}\n'
        #       f'has_number_one: {has_number_one}\n'
        #       f'has_comma: {has_comma}\n'
        #       f'has_number_two: {has_number_two}\n'
        #       f'has_right_par: {has_right_par}\n'
        #       f'number_one: {number_one}\n'
        #       f'number_two: {number_two}\n'
        #       f'parsing_fail: {parsing_fail}\n'
        #       f'parsing_done: {parsing_done}')
        
        if parsing_fail:
            in_parsing = False
            has_m = False
            has_u = False
            has_l = False
            has_left_par = False
            has_number_one = False
            has_comma = False
            has_number_two = False
            has_right_par = False
            number_one = ""
            number_two = ""
            parsing_fail = False
            parsing_done = False

        if not in_parsing:
            if char == "m":
                in_parsing = True
                has_m = True
        else:
            if has_number_two:
                if char == ")":
                    has_right_par = True
                    parsing_done = True
                elif char in digits:
                    number_two += char
                else:
                    parsing_fail = True
            elif has_comma:
                if char in digits:
                    has_number_two = True
                    number_two += char
                else:
                    parsing_fail = True
            elif has_number_one:
                if char == ",":
                    has_comma = True
                elif char in digits:
                    number_one += char
                else:
                    parsing_fail = True
            elif has_left_par:
                if char in digits:
                    has_number_one = True
                    number_one += char
                else:
                    parsing_fail = True
            elif has_l:
                if char == "(":
                    has_left_par = True
                else:
                    parsing_fail = True
            elif has_u:
                if char == "l":
                    has_l = True
                else:
                    parsing_fail = True
            elif has_m:
                if char == "u":
                    has_u = True
                else:
                    parsing_fail = True
                    
            if parsing_done:
                print('parsing is done!')
                current_mult = int(number_one) * int(number_two)
                print(f'adding {current_mult} into res {res}')
                res += current_mult
                parsing_done = False
                in_parsing = False
                has_m = False
                has_u = False
                has_l = False
                has_left_par = False
                has_number_one = False
                has_comma = False
                has_number_two = False
                has_right_par = False
                number_one = ""
                number_two = ""
                parsing_fail = False
                parsing_done = False
    return res
                         
                      

data = load_data('task1_input.txt')
print(data)

print(parse_mul(data))