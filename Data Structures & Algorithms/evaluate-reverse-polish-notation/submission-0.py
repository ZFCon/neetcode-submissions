class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])
        nums = []
        op = None
        result = 0
        
        for token in tokens:
            try:
                token = int(token)
            except:
                pass

            if type(token) == int:
                nums.append(token)
            elif op is None:
                op = token

            if op is not None:
                num2 = nums.pop()
                num1 = nums.pop()
                if op == "-":
                    result = num1 - num2
                elif op == "+":
                    result = num1 + num2
                elif op == "*":
                    result = num1 * num2
                elif op == "/":
                    result = int(num1 / num2)

                nums.append(result)
                op = None

        return result