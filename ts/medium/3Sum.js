const { resolve } = require("path");

class Solution {
	/**
	 * @param {number[]} nums
	 * @return {number[][]}
	 */
	threeSum(nums) {
		nums.sort((a, b) => a - b);
		const result = [];
		for (let idx = 0; idx < nums.length; idx++) {
			let currentNum = nums[idx];
			if (idx > 0 && currentNum == nums[idx - 1])
				continue;

			let [l, r] = [idx + 1, nums.length - 1];
			while (l < r) {
				if (nums[l] + nums[r] + currentNum > 0) {
					r--;
				} else if (nums[l] + nums[r] + currentNum < 0) {
					l++;
				} else {
					result.push([currentNum, nums[l], nums[r]]);
					while (l < r && nums[l] === nums[l + 1]) l++;
					while (l < r && nums[r] === nums[r - 1]) r--;
					l++;
					r--;
				}
			}
		}
		return result;

	}
}
