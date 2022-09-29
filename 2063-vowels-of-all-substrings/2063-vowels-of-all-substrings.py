class Solution(object):
    def countVowels(self, word):
        """
        :type word: str
        :rtype: int
        """
        bef=0
        answer=0
        vowel=['a','e','i','o','u']
        for i in range(1,len(word)+1):
            if word[i-1] in vowel:
                temp=bef+i
            else:
                temp=bef
            answer+=temp
            bef=temp
        return answer
        