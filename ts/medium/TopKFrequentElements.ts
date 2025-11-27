
class Solution {
	topKFrequent(nums: number[], k: number): number[] {
		const freqArray = new Array(2001).fill(0);
		const offset = 1000
		for (const el of nums)
			freqArray[el + offset]++;

		const bucket: number[][] = new Array(nums.length + 1).fill(0).map(() => []);

		for (let num = -1000; num <= 1000; num++) {
			const freq = freqArray[num + offset];
			if (freq > 0) {
				bucket[freq].push(num);
			}
		}
		let res: number[] = [];
		let counter = 0;
		for (let idx = bucket.length; idx >= 0; idx--) {
			if (counter == k) return res;
			if (bucket[idx].length > 0) {
				if (bucket[idx].length + counter >= k) {
					res.push(...bucket[idx].slice(0, k - counter));
					return res
				} else {
					res.push(...bucket[idx])
				}
			}

		}
		return [-1];
	}
}
