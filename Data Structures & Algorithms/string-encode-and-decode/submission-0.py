class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        #loop through the list
        for s in strs:
            #we want it in the format {(size) + # + string}
            res += str(len(s)) + "#" + s
    
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0 #we need a pointer to go through the strings

        while i < len(s):
            j = i
            while s[j] != '#': #so now j is passing through the string until it reaches #
                j += 1

            #once its found the length is equal to the num chats between i and j
            length = int(s[i:j]) 
            #both pointers are then moved forward to the next word
            i = j + 1
            j = i + length
            res.append(s[i:j])
            # j is now where i needs to be
            i = j

        return res

        

