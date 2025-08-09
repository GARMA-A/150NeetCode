class Solution {
	/**
	 * @param {number[]} nums
	 * @param {number} target
	 * @return {number[]}
	 */
	twoSum(nums, target) {
		// target = num1 + num2 ;
		// num1 = target - num2;
		const mp = {};
		for (let i = 0; i < nums.length; i++) {
			const complement = target - nums[i];
			if (mp[complement] !== undefined) {
				return [mp[complement], i]
			}
			mp[nums[i]] = i;

		}

	}

}

