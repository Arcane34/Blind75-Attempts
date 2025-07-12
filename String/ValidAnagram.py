# FINISHED
# https://leetcode.com/problems/valid-anagram/description/


def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """


        # Sorting solution where you sort the 2 strings and then compare them with each other

        """
        if len(s) != len(t):
            return False
        sortS = "".join(sorted(s))
        sortT = "".join(sorted(t))

        return( sortS == sortT)
        """


        # compare the counts of the first letter in the first string , for both strings, then remove all instances of that character in the first string,
        # then compare the first letter after that removal as the first letter will now be a unique character, repeat this until the first string is empty
        if len(s) != len(t):
            return False
        else:
            while s != "":
                if s.count(s[0]) != t.count(s[0]):
                    return False
                s = s.replace(s[0],"")
                
                
            return True
