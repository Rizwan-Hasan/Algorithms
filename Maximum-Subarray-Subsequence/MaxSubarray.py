def maxSubArray(self, nums: list):
	mx = val = sys.maxsize * -1
	for i in nums:
		val = max(i, i + val)
		if val > mx:
			mx = val
	return mx