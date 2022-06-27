class Solution:
    def interpret(self, command: str) -> str:
        """Not the best solution, but works"""
        str_builder = []
        for c in command:
            if c == "G":
                str_builder.append("G")
            # Can check i and i + 1 index instead
            if c == "(":
                is_opening = True
            if c == "a":
                str_builder.append("al")
                is_opening = False
            if c == ")" and is_opening:
                str_builder.append("o")
                is_opening = False
        return "".join(str_builder)