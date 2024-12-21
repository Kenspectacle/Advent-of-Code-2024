import copy

class Solution:

    def convert_data_to_int(self, data) -> list[list]:
        for i in range(len(data)):
            data[i] = list(map(int, data[i]))
        return data
    
    def check_is_ascending(self, nums) -> bool:
        return (all(nums[i] <= nums[i+1] for i in range(len(nums) - 1)))
    
    def check_is_descending(self, nums) -> bool:
        return (all(nums[i] >= nums[i+1] for i in range(len(nums) - 1)))
    
    def check_are_valid_gaps(self, nums, gap) -> bool:
        for i in range(len(nums) - 1):
            diff = abs(nums[i+1] - nums[i])
            if diff > gap or diff == 0:
                return False
        return True
    
    def check_if_level_is_safe(self, level) -> bool:
        is_monotonous = self.check_is_ascending(level) or self.check_is_descending(level)
        are_valid_gaps = self.check_are_valid_gaps(level, 3)
        if (is_monotonous and are_valid_gaps): 
            return True
        else: 
            return False
        

    def find_safe_levels(self, data):
        number_of_safe_levels = 0
        data = self.convert_data_to_int(data)
        print(data)
        for level in data:
            
            print('Checking for: ', level)
            

            # initialize
            is_safe = False 


            is_safe = self.check_if_level_is_safe(level)

            # bruteforce check for each removed element in level
            for i in range(len(level)):
                filtered_level = copy.deepcopy(level)
                filtered_level.pop(i)
                is_safe = self.check_if_level_is_safe(filtered_level) or is_safe
                
            # check for safety in each level
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
# data = s.load_data('task2_input.txt')
data = s.load_data('task2_input.txt')
print(data)
print(f'total safe levels: {s.find_safe_levels(data)}')
print('len input: ', len(data))