def main():
    starting_num = 1
    ending_num = 1000
    nums = range(starting_num, ending_num)
    multiples = []
    
    for num in nums:
        if num not in multiples:
            if ((num % 3) == 0) or ((num % 5) == 0): multiples.append(num)
     
    print "Sum of all the multiples of 3 and 5 between " \
            + str(starting_num) \
            + " and " \
            + str(ending_num) \
            + " is " \
            + str(sum(multiples))
            
        
        
if __name__ == '__main__':
    main()