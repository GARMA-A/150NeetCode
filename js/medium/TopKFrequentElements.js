class Solution {
	/**
	 * @param {number[]} nums
	 * @param {number} k
	 * @return {number[]}
	 */
	topKFrequent(nums, k) {
		const heap = new Heap((a, b) => a[1] - b[1]);
		const freq = {};
		for (const num of nums) {
			if (!freq[num]) {
				freq[num] = 0;
			}
			freq[num]++;
		}

		for (const num in freq) {
			heap.enq([parseInt(num), freq[num]]);
			if (heap.size() > k) {
				heap.deq();
			}
		}
		const result = [];
		while (heap.size() > 0) {
			result.push(parseInt(heap.deq()[0]));
		}
		return result;

	}
}

