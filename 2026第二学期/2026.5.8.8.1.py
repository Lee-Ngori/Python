class BracketChecker():
    def __init__(self):
        self.pairs = {')':'(', ']':'[','}':'{'}
        self.left_brackets = set(self.pairs.values())
    def check(self,string):
        stack = []
        for char in string:
            if char in self.left_brackets:
                stack.append(char)
            elif char in self.pairs:
                if not stack:
                    return False
                top = stack.pop()
                if top != self.pairs[char]:
                    return False
        return not stack
checker = BracketChecker()
test = '{[()]}'
print(checker.check(test))