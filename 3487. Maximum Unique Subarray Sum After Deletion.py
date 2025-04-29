class Solution:
    def maxSum(self, nums: List[int]) -> int:

      #dalegenensky

      positives = [i for i in set(nums) if i > 0]

      if positives:
        return sum(positives)
      else:
        return max(nums)
