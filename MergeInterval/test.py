def solution(n):
    # Your code here
    num_pallet = int(n)
    num_operation = 0
    
    while num_pallet != 1:
        if num_pallet % 2 == 0:
            num_pallet = num_pallet//2
            
        elif num_pallet == 3 or num_pallet%4 ==1:
            num_pallet -= 1
        else:
            num_pallet += 1
        num_operation += 1
        
    return num_operation

print(solution(15))