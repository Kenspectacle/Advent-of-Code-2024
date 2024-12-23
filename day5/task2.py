from collections import defaultdict
import math

def load_data(input_file) -> list:
    with open(input_file, 'r') as file:
        data = file.read().split('\n\n')
        rules, updates = data
        rules = [rule.split('|') for rule in rules.split('\n')]
        updates = [update.split(',') for update in updates.split('\n')]
    return rules, updates

def find_valid_print_queue(rules, updates) -> int:
    total = 0
    
    # create adjacency list: source -> destination    
    adj_list = defaultdict(list)
    for a, b in rules:
        adj_list[a].append(b)
        
    # check for valid print queues
    for update in updates:
        
        is_sorted = False

        valid_queue = True
        temp = 0
        
        while not is_sorted:
            is_sorted = True
            for i in range(len(update) - 1):
                prev = update[i]
                curr = update[i+1]
                if curr not in adj_list[prev]:
                    valid_queue = False
                    is_sorted = False
                    # sort
                    temp = update[i+1]
                    update[i+1] = update[i]
                    update[i] = temp 
                    
                    
                
        if not valid_queue:
            mid = math.floor(len(update) / 2)
            total += int(update[mid])
        else:
            print(f'current {update} is not valid')
            
    return total


rules, updates = load_data('day5/task1_test.txt')
print(find_valid_print_queue(rules, updates))

# rules, updates = load_data('day5/test2.txt')
# print(find_valid_print_queue(rules, updates))