def balancedbrackets(brackets):
    matching={"}":"{","]":"[",")":"("}
    opening="{(["
    closing="]})"
    stack=[]
    for bracket in brackets:
        if bracket in closing:
            if(len(stack)==0):
                return False
            else:
                if(stack[-1]==matching[bracket]):
                    stack.pop()
                else:
                    return False
        else:
            stack.append(bracket)
    return len(stack)==0
brackets=list(input())
if(balancedbrackets(brackets)):
    print("Yes")
else:
    print("No")

                    
    