class Solution {
	longestConsecutive(nums: number[]): number {
		let mx = 0;
		let numSet = new Set<number>();
		for (const num of nums)
			numSet.add(num);
		for (const num of nums) {
			let counter = 1;
			let i = 1;
			while (numSet.has(num - i)) {
				counter++;
				i++;
			}
			mx = Math.max(mx, counter);

		}
		return mx;
	}
}
