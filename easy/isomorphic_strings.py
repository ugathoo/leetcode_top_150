## PROBLEM #205: Given two strings s and t, determine if they are isomorphic. Two strings s and t are isomorphic if the characters in s can be replaced to get t. All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

## APPROACH: If strings are isomorphic, mapping each character to a number should yield identical results. 
class Solution(object):
    def helper(self, s):
        mapping = {}
        ret = []

        for i, c in enumerate(s):
            if c not in mapping:
                mapping[c] = i
            ret.append(str(mapping[c]))

        return " ".join(ret)
    
    def isIsomorphic(self, s, t):
        return self.helper(s) == self.helper(t)
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        