class Solution:
    def decodeString(self, s: str) -> str:

        num_stack = []
        str_stack = []

        current = ""
        num = 0

        for x in s:

            if x.isdigit():
                num = num * 10 + int(x)

            elif x == '[':
                num_stack.append(num)
                str_stack.append(current)

                num = 0
                current = ""

            elif x == ']':
                k = num_stack.pop()
                previous = str_stack.pop()

                current = previous + k * current

            else:
                current += x

        return current