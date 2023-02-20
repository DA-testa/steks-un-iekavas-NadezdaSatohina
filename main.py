# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append(Bracket(next,i+1))
        if next in ")]}":
            if not opening_brackets_stack or not are_matching(opening_brackets_stack[-1].char, next):
                return i+1
            opening_brackets_stack.pop()
    if not opening_brackets_stack:
        return "Success"

def main():
    input_type = input()
    if "F" in input_type:
        input_name = input()
        with open (input_name) as f:
            text = f.read()
            mismatch = find_mismatch(text)
    elif "I" in input_type:
        text = input()
        mismatch = find_mismatch(text)
        if mismatch == "Success":
            print ("Success")
        else:
            print(mismatch)

if __name__ == "__main__":
    main()
