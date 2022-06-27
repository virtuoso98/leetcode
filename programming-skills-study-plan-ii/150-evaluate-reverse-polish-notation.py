class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations_map = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            # Floor a // b vs truncation int(a / b)
            "/": lambda a, b: int(a / b)
        }
        
        stk = []
        for exp in tokens:
            if exp in operations_map:
                r_num = stk.pop()
                l_num = stk.pop()
                res = operations_map[exp](l_num, r_num)
                stk.append(res)
            else:
                stk.append(int(exp))

        return stk[0]