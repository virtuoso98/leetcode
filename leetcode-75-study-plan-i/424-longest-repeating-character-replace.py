class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ans, left = 0, 0
        max_freq = 0
        counter = collections.defaultdict(int)
        
        for right in range(len(s)):
            counter[s[right]] += 1
            max_freq = max(max_freq, counter[s[right]])

            if right - left + 1 > k + max_freq: 
                counter[s[left]] -= 1
                left += 1
			
        ans = right - left + 1
        return ans