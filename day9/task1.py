from collections import defaultdict

def load_data(input_file) -> str:
    with open(input_file, 'r') as file:
        disk_map = file.read()
    return disk_map

def find_disk_fragment(disk_map) -> str:
    # get disk fragments
    fragment = []
    id = 0
    for i, char in enumerate(disk_map):
        if i % 2 == 0:
            for i in range(int(char)):
                fragment.append(str(id))
            id += 1
        else:
            for i in range(int(char)):
                fragment.append('.')
    return fragment


def defragment_disk(fragment) -> str:
    new_fragment = list(fragment)
    
    left = 0
    right = len(new_fragment) - 1
    found_free_space = False
    found_memory_block = False
    while left < right:
        
        if not new_fragment[left].isdigit():
            found_free_space = True
        else:
            left += 1
        if new_fragment[right].isdigit():
            found_memory_block = True
        else:
            right -= 1
        
        if found_free_space and found_memory_block:
            new_fragment[left], new_fragment[right] = new_fragment[right], new_fragment[left]
            # reset
            found_free_space = False
            found_memory_block = False
            left += 1
            right -= 1
        
    return new_fragment

def find_checksum(defrag) -> int:
    checksum = 0
    for id, mem_block in enumerate(defrag):
        if mem_block.isdigit():
            checksum += id * int(mem_block)
    
    return checksum
    
        

print('loading diskmap...')
disk_map = load_data('day9/task1_test.txt')
# disk_map = load_data('day9/test.txt')
# disk_map = '233313312141413140234'
print('finished loading diskmap')
print('finding the disk fragment...')
fragment = find_disk_fragment(disk_map)
print('finished loading disk fragment...')
print('defragging the fragment...')
defrag = defragment_disk(fragment)
print('finished defragging')
print('final step: checking checksum')
checksum = find_checksum(defrag)
print(checksum)
print('checksum finished')
print('status: OK')