def bracket_pair_checker(brackets: str) -> bool:
    stack: list[str] = []
    for bracket in brackets:
        if bracket in '[{(':
            stack.append(bracket)
        if bracket in ']})':
            if bracket == '}' and stack[-1] == '{':
                stack.pop()
            elif bracket == ']' and stack[-1] == '[':
                stack.pop()
            elif bracket == ')' and stack[-1] == '(':
                stack.pop()
            else:
                return False

    return len(stack) == 0


print(bracket_pair_checker('{{([][])}()}'))
print(bracket_pair_checker("{}[]()"))
