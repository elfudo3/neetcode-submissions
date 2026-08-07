class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t) ## solution 1 space complexity: O(1) Time complexity O(n + m)

        return Counter(s) == Counter(t) 
        
        
        if (len(s) != len(t)):
            return False
        
        list_s = []
        list_t = []

        for letter in s:
            list_s.append(letter)
        
        for letter in t:
            list_t.append(letter)
        
        list_s.sort()
        list_t.sort()

        if(list_s == list_t):
            return True
        return False

        

        