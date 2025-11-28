
class Solution {
	productExceptSelf(nums: number[]): number[] {
		let preFix = new Array(nums.length + 1).fill(1);
		let postFix = new Array(nums.length + 1).fill(1);
		for (let idx = 1; idx < preFix.length; idx++) {
			preFix[idx] = preFix[idx - 1] * nums[idx - 1];
		}
		for (let idx = postFix.length - 2; idx >= 0; idx--) {
			postFix[idx] = postFix[idx + 1] * nums[idx];
		}
		let result = [];
		for (let i = 0; i < nums.length; i++) {
			result.push(preFix[i] * postFix[i + 1]);
		}
		return result;

	}
}



