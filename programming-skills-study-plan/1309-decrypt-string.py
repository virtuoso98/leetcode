class Solution:
    def freqAlphabets(self, s: str) -> str:
        str_builder = []
        i = 0
        ASCII_BASE = 96
        while i < len(s):
            # Just need to look for hex symbol to append
            if i < len(s) - 2 and s[i + 2] == "#":
                valid_ascii = ASCII_BASE + int(s[i:i + 2])
                str_builder.append(chr(valid_ascii))
                # Skip 3 indexes because pattern is 3 characters
                i += 3
            else:
                valid_ascii = ASCII_BASE + int(s[i])
                str_builder.append(chr(valid_ascii))
                i += 1
            
        return "".join(str_builder)