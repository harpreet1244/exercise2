def display():
     row1 = [" "," "," "]
     row2 = [" "," "," "]
     row3 = [" "," "," "]
     result = int(input("select the position : "))
     row1[result] = "x"
     print(row1)
     print(row2)
     print(row3)
   

display()

def user_input():
    choice = " "
    acceptable_range = range(0,3)
    within_range = False
    while choice.isdigit() == False or within_range == False:
        choice = input("select the position (0 - 2): ")
        if choice.isdigit() == False:
            print("sorry this is not a digit") 
        if choice.isdigit() == True:
            if int(choice) in acceptable_range:
                within_range = True
                print(choice)
            else:
                print("hi your are out of the range")
                within_range = False

         
    return  int(choice)

user_input()


