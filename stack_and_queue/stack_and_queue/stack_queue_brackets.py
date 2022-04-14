start = ["[", "{", "("]
end = ["]", "}", ")"]
stack = []
def validate_brackets(string):

    if type(string) != str:
        raise "Enter a valid string"

    for i in string:
        if i in start:
            stack.append(i)

        elif i in end:
            if len(stack) == 0:
                return False

            if start[end.index(i)] == stack[len(stack) - 1]:
                stack.pop()

            else:
                return False

    return True if len(stack) == 0 else False
    

# batool explaine the required from the CC and gave me line 23 
if __name__ == "__main__":
    print(validate_brackets("{***}"))
    print(validate_brackets(""))
    print(validate_brackets("}"))
    print(validate_brackets("{}(){}"))
    print(validate_brackets("(){}[[]]"))
    print(validate_brackets("(]("))
    print(validate_brackets(""))