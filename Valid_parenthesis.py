def is_valid(s:str):
    if len(s)%2!= 0:
       return False
    if s[0]== [')','}',']']:
       return False
    bracket_map = {'(':')','[':']','{':'}'}
    stack = []
    for char in s :
        if char in bracket_map:
           top_element = stack.pop()if stack else'#'
        if bracket_map[char]!= top_element:
            return False
        else:
            stack.append(char)
        return len(stack) == 0
print(is_valid("{]("))
