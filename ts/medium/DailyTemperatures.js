class Solution {
	/**
	 * @param {number[]} temperatures
	 * @return {number[]}
	 */
	dailyTemperatures(temperatures) {
		const stack = [];
		const result = new Array(temperatures.length).fill(0);

		for (let idx = 0; idx < temperatures.length; idx++) {
			const currentTemp = temperatures[idx];
			while (stack.length !== 0 && currentTemp > stack[stack.length - 1][0]) {
				const [_, stackIdx] = stack.pop()
				const days = idx - stackIdx;
				result[stackIdx] = days;
			}
			stack.push([currentTemp, idx]);
		}
		return result;
	}
}
