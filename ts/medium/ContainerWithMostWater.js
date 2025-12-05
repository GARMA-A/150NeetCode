class Solution {
	/**
	 * @param {number[]} heights
	 * @return {number}
	 */
	maxArea(heights) {
		let [left, right] = [0, heights.length - 1];
		let mx_area = 0;
		while (left < right) {
			const curWidth = right - left;
			const curHeight = Math.min(heights[left], heights[right]);
			const curArea = curWidth * curHeight;
			mx_area = Math.max(mx_area, curArea);
			heights[left] < heights[right] ? left++ : right--;
		}
		return mx_area;

	}
}
