
class Solution {
	twoSum(nums: number[], target: number): number[] {
		let mp = new Map<number, number>();
		for (let idx = 0; idx < nums.length; idx++) {
			let current_value = nums[idx];
			let complement = target - current_value;
			if (mp.has(complement)) {
				return [mp.get(complement)!, idx];
			}
			mp.set(current_value, idx);

		}

		return [];
	}
}
