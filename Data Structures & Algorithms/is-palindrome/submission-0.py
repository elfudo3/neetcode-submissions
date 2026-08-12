class Solution:
    def isPalindrome(self, s: str) -> bool:
        #forward loop
    #   for char in s:
    #       if not char.isalnum():
    #            continue
            
        
    #    for char in s[::-1]:
    #        if not char.isalnum():
    #            continue
         
        s = "".join(char for char in s if char.isalnum())
        s = s.lower()
        return s == s[::-1]

            
        