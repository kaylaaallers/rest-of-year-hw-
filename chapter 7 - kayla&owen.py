numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
def count_odd (numlist):
    count = 0
    for x in numlist:
        if not x % 2:
    	     count+=1
    
    return count

print("Number of odd numbers :",count_odd(numbers))

