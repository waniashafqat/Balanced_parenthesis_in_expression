# Check expression for balanced parenthesis using stack.
par_dict = {
    "{": "}",
    "[": "]",
    "(": ")"
}

class Stack:
    # Special method to initialize the attributes.
    def __init__(self):
        self.s_data = []

    def push(self, val):
        self.s_data.append(val)

    def pop(self):
        return self.s_data.pop()

    def is_empty(self):
        return self.s_data == []

    # Function to check whether the expression has balanced parenthesis.
    def balanced_parenthesis(self, exprsn):
        for count, current_char in enumerate(exprsn):

            # CASE 01: If opening parenthesis, push immediately to stack.
            if current_char in (par_dict.keys()):
                self.push(current_char)

            # CASE 02: If closing parenthesis, check immediately if previous parenthesis was its open-counterpart.
            else:
                if self.is_empty():
                    return False

                previous_char = self.pop()

                if not (current_char == par_dict[previous_char]):
                    return False

        # Check for empty stack.
        if self.is_empty():
            return True
        else:
            return False


s = Stack()
lst = input("Please enter an expression including parenthesis: ")
exprsn = []

for l in lst:
    if (l in par_dict.keys()) or (l in par_dict.values()):
        exprsn.append(l)

print("\nExpression by user: ", lst)
print("\nExtracted parenthesis list: ", exprsn)

if s.balanced_parenthesis(exprsn):
    print("\nThe expression has balanced parenthesis.")

else:
    print("\nThe expression does not have balanced parenthesis.")