## PROBLEM #383: Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

## APPROACH 1: Counter

from collections import Counter
class Solution(object):
    def canConstruct(self, ransomNote, magazine):

        ransom_dict = Counter(ransomNote)
        mag_dict = Counter(magazine)

        for key in ransom_dict:
            if key not in mag_dict or mag_dict[key] < ransom_dict[key]:
                return False
        return True
      
#Final Time Complexity: O(m + n) -> iterating through both strings once
#Final Space Complexity: O(m + n) -> creating 2 dictionaries