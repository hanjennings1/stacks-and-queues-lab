def is_valid_parentheses(s: str) -> bool:
    """
    Return True if the string contains valid, balanced parentheses.
    Only (), {}, and [] are considered valid.
    """

    # Each closing bracket mapped to the opening bracket it must match
    pairs = {")": "(", "]": "[", "}": "{"}

    # A plain list used as a stack: the end of the list is the top of the stack
    stack = []

    # Look at each character in the string, one at a time
    for char in s:

        # Is this character an opening bracket: (, [, or { 
        if char in pairs.values():
            # Yes, so add it to the top of the stack to remember it's open
            stack.append(char)

        # Is this character a closing bracket: ), ], or } 
        elif char in pairs:

            # If the stack is empty, nothing is open, so this closing bracket has no partner
            if not stack:
                return False

            # Take the most recent opening bracket off the top of the stack
            top = stack.pop()

            # Check that it's the correct partner for this closing bracket
            if top != pairs[char]:
                return False

    # Valid only if every opening bracket was closed
    return len(stack) == 0
