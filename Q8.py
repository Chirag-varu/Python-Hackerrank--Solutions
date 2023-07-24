def find_second_largest(numbers):
    if len(numbers) < 2:
        return "List should contain at least two numbers."
    
    largest = float('-inf')
    second_largest = float('-inf')
    
    for num in numbers:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num
    
    if second_largest == float('-inf'):
        return "There is no second largest number in the list."
    
    return second_largest


# Example usage
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    second_largest_number = find_second_largest(arr)
    print(second_largest_number)
