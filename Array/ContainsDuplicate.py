# FINISHED
# https://leetcode.com/problems/contains-duplicate/

def containsDuplicate(self, nums):
        

        """
        :type nums: List[int]
        :rtype: bool
        """
        

        # sort an array of numbers, if theres a duplicate you check with the next element and see if it is the same as you, thats it for the rest of the array
        """
        nums = sorted(nums)

        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
        
        return False
        """

        #sets are lists of unique items so it would have a different length if there are duplicates
        dictA = set(nums)

        if len(nums) != len(dictA):
            return True

        return False