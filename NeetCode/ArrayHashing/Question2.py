class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countS, countT = {}, {}
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0) # gets the current ammount of the character and adds 1 to it 
            print(countS[s[i]])
            countT[t[i]] = 1 + countT.get(t[i], 0)
            print(countT[t[i]])
        return countS == countT # compare the hashmaps 
