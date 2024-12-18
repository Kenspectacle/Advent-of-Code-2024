class Solution:
    def find_total_distance(self, data) -> int:
        
        # Convert to two separate lists
        nums1 = [int(row[0]) for row in data]
        nums2 = [int(row[1]) for row in data]
        print(nums1)
        print(nums2)
        sorted_nums1 = sorted(nums1)
        sorted_nums2 = sorted(nums2)
        
        total_distance = 0
        for i in range(len(sorted_nums1)):
            total_distance += abs(sorted_nums1[i] - sorted_nums2[i])
            
        return total_distance
    
    def load_data(self) -> list[list]:
        with open('task1_input.txt', 'r') as file:
            data = [line.split() for line in file]
        return data
    
s = Solution()
data = s.load_data()
print(data)
print(s.find_total_distance(data))