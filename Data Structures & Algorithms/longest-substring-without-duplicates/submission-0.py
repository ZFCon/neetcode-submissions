class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        visited = {}
        max_length = 0
        
        while r < len(s):
            char = s[r]
            
            # If we hit a duplicate, shrink the window from the left
            while char in visited:
                left_char = s[l]
                # Remove the character at the left pointer from our hashmap
                del visited[left_char]
                # Move the left pointer forward
                l += 1
                
            # Add the new character and its index to the hashmap
            visited[char] = r
            
            # Update max_length if our current window is bigger
            current_window_size = r - l + 1
            if current_window_size > max_length:
                max_length = current_window_size
                
            # Move the right pointer forward
            r += 1
            
        return max_length