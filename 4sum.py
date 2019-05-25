#4sum problem that can execute in O(n**2)

def fourNumberSum(array, targetSum):
    result = []
    seen = {}
    for current_index, current_element in enumerate(array):
        
        for fwd_index,fwd_element in enumerate(array[current_index+1:]):
            if targetSum - (current_element+fwd_element) in seen:
                for pair in seen[targetSum - (current_element+fwd_element)]:
                    result.append(pair + [current_element,fwd_element])
                    
        for bwd_index,bwd_element in enumerate(array[:current_index]):
            if bwd_element + current_element not in seen:
                seen[bwd_element+current_element] = []
            seen[bwd_element+current_element].append([bwd_element,current_element])
    
    return result

fourNumberSum([7,6,4,-1,1,2],16])