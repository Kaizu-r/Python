#BALANCED PARENTHESIS CHECKER
#takes input string
str = input("Enter a string of parenthesis: ")
flag = 0
#x acts as the current index within the string str
for x in str:
    #unexpected symbols
    if(x != '(' and x != ')'):
        print("Input string contains unknown symbols")
        exit()
    #a closing parenthesis was found without a matching open parenthesis
    if(flag < 0):
        print("Unbalanced Parenthesis")
        exit()
    #adds 1 if it finds an open parenthesis
    if(x == '('):
        flag = flag + 1
    #subtracts 1 if it finds a closing parenthesis
    else:
        flag = flag - 1
#flag is zero, therefore there are balanced parenthesis
if(flag == 0):
    print("Balanced Parenthesis")
else:
    print("Unbalanced Parenthesis")