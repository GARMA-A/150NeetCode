class Solution {
	/**
	* @param {number[]} nums
	* @returns {boolean}
	*/
	hasDuplicate(nums) {
		const set = new Set();
		for (const num of nums) {
			set.add(num);
		}
		return (set.size !== nums.length);
	}

	
}

