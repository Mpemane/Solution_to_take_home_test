
# define a function for the ten digit isbn
def is_valid_isbn10(isbn10):
    # initiate two variables to keep track of the sum and the results of the computation
    result = -1
    total = 0
    isbn10 = isbn10[::-1] # reverse the string
    
    for i in range(len(isbn10)):
        # mapping the elemnt of the list to integers
        digit = int(isbn10[i])
        # Update the total
        total += digit * (i - 2)
    # update the results
    result = (11 - (total % 11)) % 11
    return result

# defind a function for the 13 digit isbn
def is_valid_isbn13(isbn13):
    # initiate two variables to keep track of the sum and the results of the computation
    result = -1
    total = 0
    # use a for loop to iterate through the list of the isbn13 elements
    for i in range(len(isbn13)):
        # mapping the elemnt of the list to integers
        digit = int(isbn13[i])
        # Update the total
        total += digit *(3 if (i%2 !=0) else 1)
    # update the results
    result = (10 -(total % 10))%10
    return result

# Test the functions if they work properly
# by asking the user to enter their codes and validate them
while True:
    if __name__ == "__main__":
        isbn =  input("Please enter what type of ISBN number you would like to verify, either isbn10 or isbn13 or enter e to exit: ").lower()
        
        if isbn == "isbn10":
            isbn10 = input("Please enter your isbn10 code: ")
            if is_valid_isbn10(isbn10) == False:
                print("Valid")
            else:
                print("Invalid")
        elif isbn == "isbn13":
            isbn13 = input("Please enter your isbn13 code")
            if is_valid_isbn13(isbn13) == False:
                print("Valid")
            else:
                print("Invalid")
        elif isbn == "e":
            print("Goodbye")
            break
            
        else:
            print("Invalid option")

# Reference
# https://en.wikipedia.org/wiki/ISBN#ISBN-13_check_digit_calculation
# https://www.hackerrank.com
# https://www.youtube.com/watch?v=fWrbzNOj5M0
