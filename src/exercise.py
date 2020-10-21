def smallest(number1, number2):
    # write your code here
    # do not print anything inside the method
    # there must be a return command at the end
    if(number1>number2):
      return number2
    else:
      return number1
 
def main():
    answer =  smallest(2, 7)
    print("Smallest: " + str(answer))
if __name__ == '__main__':
    main()
