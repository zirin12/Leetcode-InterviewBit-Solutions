class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0 or len(s) == 1 :
            return len(s)
        max_window_len = 1
        start_window = 0
        end_window = 1
        input_length = len(s)
        hash_map = {}
        hash_map[s[0]] = 0
        while end_window <= (input_length-1) and start_window<=end_window:
            if s[end_window] not in hash_map.keys():
                hash_map[s[end_window]]=end_window
                if ((end_window-start_window) + 1) > max_window_len:
                    max_window_len = (end_window-start_window) + 1
                end_window+=1
            else:
                del hash_map[s[start_window]]
                start_window+=1
        return max_window_len
