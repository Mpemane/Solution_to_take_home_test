from num2words import num2words # import the library that is needed for this task.
num = int(input("Please enter the number that you want to know how  its pronounce: ")) # Prompt the use to enter a number.
def num_to_words(num): # defines the function.
    out_put = num2words(num) # initiate a variable output, that outputs the numbers the way it i pronounce
    print(out_put) # print out the output.

num_to_words(num) # calling the function and outputing the answer.
