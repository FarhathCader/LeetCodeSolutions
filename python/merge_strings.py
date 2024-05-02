class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i,j,k = (0,0,0)
        n = len(word1) 
        m = len(word2) 
        result = ""
        while i < n or j < m :
            if(i == n):
                result += word2[j:]
                break
            if(j == m):
                result += word1[i:]
                break
            result += (word1[i] + word2[j])
            i += 1
            j += 1
            
        return result

        