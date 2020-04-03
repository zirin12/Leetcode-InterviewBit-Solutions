class Solution:
    '''
        Given a string, find the length of the longest substring without repeating characters.
    '''
    # Sliding Window with hashmap approach
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
    
    # Optimized sliding window where we skip characters 
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_window_len = 0
        start_window = 0
        end_window = 0
        input_length = len(s)
        hash_map = {}
        while end_window < input_length:
            if s[end_window] in hash_map.keys():
                start_window = max(start_window,hash_map[s[end_window]])
            max_window_len = max(max_window_len,end_window-start_window+1)
            hash_map[s[end_window]] = end_window+1
            end_window+=1
        return max_window_len
    
