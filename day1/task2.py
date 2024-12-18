from collections import defaultdict

class Solution:
    def find_similarity_score(self, data):
        # Convert to two separate lists
        nums1 = [int(row[0]) for row in data]
        nums2 = [int(row[1]) for row in data]
        print(nums1)
        print(nums2)
        
        count = defaultdict(int)
        for num in nums2:
            count[num] += 1
        
        similarity_score = 0
        
        for num in nums1:
            similarity_score += num * count[num]
        
        return similarity_score
    
    def load_data(self, input_file) -> list[list]:
        with open(input_file, 'r') as file:
            data = [line.split() for line in file]
        return data
    
s = Solution()
data = s.load_data('task2_input.txt')
print(data)
print(s.find_similarity_score(data))