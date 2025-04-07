# 괄호 유효성 검사
def isValid(s):
    stack = []
    for p in s:
        if p == "(":
            stack.append(")")
        elif p == "{":
            stack.append("}")
        elif p == "[":
            stack.append("]")
        elif not stack or stack.pop() != p:
            return False

    return not stack


valid = isValid("()(){}{}{{}}")
print(valid)
