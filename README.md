# Solution_to_take_home_test
Solutions to hyperiondev take home test
# Section A solution Code Review Python Task.
The code, that the student submitted was grade on the following critiria
## Scores
####  <br /> -Documentation = 0/4
#### <br /> -Style = 1/4
#### <br /> -Efficiency = 1/4
#### <br /> -Correctness = 2/4
## Positive
Well done on a great attempt on this task, you  have showed good understanding of classes and implimenting they objects.
## Improve
<br /> line 3 to 10 on your code, are not corretly indinted, which causes a compiling error
<br /> line 5 is missing an arguement, which causes a running time error
<br /> your code is not documented/commented.
<br /> may you please also add some references, 
 You can improve your code’s readability by paying attention to the style and documentation. Please have a look at Google's style guide for Python with standards expected from your code style and documentation: https://www.python.org/dev/peps/pep-0008/. Addding comments on your code,can easily communicate your logic on the code to the next person and improve readability.
## Overall
Good Submission, May you please attandend to the suggested corrections and resubmit.
# Section B link to a project.
This project uses Machine Learning to build a RNN model which you can use to classify movie reviews as either negative or positive, which is a sentiment analysis project.
https://github.com/Mpemane/classify-a-movie-review
# Section C 
<br />I have solve the International Standard Book Numbers(ISBN) challenge, using python.

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
<br /> I have also included a python file name ISBN.py that contains the solution to the Verication code of the ISBN.
# Section D Loom video.
The link below, will take you to my loom videos, is about 2 and half minute long.
https://www.loom.com/share/12d6394e72f348889546f41545bafb3e
