class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        i = len(words)-1
        while i > 0:
            if Counter(words[i]) == Counter(words[i-1]):
                words.pop(i)
            i -= 1
        return words


        

            
