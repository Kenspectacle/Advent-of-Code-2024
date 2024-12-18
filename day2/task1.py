class Solution:
    def find_safe_levels(self, data):
        number_of_safe_levels = 0
        for i in range(len(data)):
            data[i] = list(map(int, data[i]))
        print(data)
        for level in data:
            print('Checking for: ', level)
            
            # initialize
            is_safe = True
            left = 0
            right = 1
            if level[left] < level[right]:
                is_ascending = True
            else:
                is_ascending = False
            
            # check for safety in each level
            while right < len(level):
                diff = level[right] - level[left]
                if (((diff > 0) == (not is_ascending)
                    or ((diff < 0) == (is_ascending )))
                    ):
                    is_safe = False
                    print('safety: unsafe \nreason: wrong ascend')
                    break
                elif(abs(diff) > 3 or abs(diff) == 0):
                    is_safe = False
                    print(f'safety: unsafe \nreason: the difference is {abs(diff)}')
                    break
                else:
                    left += 1
                    right += 1
                    
            if is_safe:
                number_of_safe_levels += 1
                print(f'safety: safe, increasing number of safe level by 1 to {number_of_safe_levels}')
            else:
                print(f'Current level is unsafe, number of safe level stays at {number_of_safe_levels}')

                
        return number_of_safe_levels
        
    def load_data(self, input_file) -> list[list]:
        with open(input_file, 'r') as file:
            data = [line.split() for line in file]
        return data


s = Solution()
data = s.load_data('task1_input.txt')
print(data)
print(f'total safe levels: {s.find_safe_levels(data)}')