def balancedBrackets(brackets):
    matching={"]":"[","}":"{",")":"("}
    opening="{[("
    closing="}])"
    stack=[]
    for bracket in brackets:
        if bracket in closing:
            if(len(stack)==0):
                return False
            elif matching[bracket]==stack[-1]:
                stack.pop()
            else:
                return False
        else:
            stack.append(bracket)
    return len(stack)==0
brackets=input()
print(balancedBrackets(brackets))
