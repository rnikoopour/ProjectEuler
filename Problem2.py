def main():
    i_minus_2_num = 1
    i_minus_1_num = 2
    
    evens = []
    fibonacci = [1,2]
    
    while True:
        if (i_minus_1_num % 2) == 0: evens.append(i_minus_1_num)

        

        next_fibonacci_num = i_minus_2_num + i_minus_1_num
        if next_fibonacci_num >= 4000000:
            break
        else:
            i_minus_2_num = i_minus_1_num
            i_minus_1_num = next_fibonacci_num
        
    print "The sum of all even fibonacci numbers between 1 and 3999999 is " \
            + str(sum(evens))
    
        
if __name__ == '__main__':
    main()