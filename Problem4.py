def main():
    num_1 = 100
    num_2 = 100
    largest_palindrome = 0
    
    while num_1 <= 999:
        while num_2 <=999:
            product = num_1 * num_2
            if str(product) == str(product)[::-1]:
                if largest_palindrome < product:
                    largest_palindrome = product
            num_2 += 1
            
        num_1 += 1
        num_2 = 100

    print largest_palindrome

if __name__ == '__main__':
    main()