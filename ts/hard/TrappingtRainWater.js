class Solution {
	/**
	 * @param {number[]} height
	 * @return {number}
	 */
	trap(height) {
		// i do not know how but the problem should solved by this equation
		// water_trapped+=min(leftMaxHeighArray[idx] , rightMaxHeighArray[idx]) - currentHeigh[idx] 
		let leftMaxHeightArray = new Array(height.length).fill(0);
		let curMx = 0;
		for (let idx = 0; idx < height.length; idx++) {
			curMx = Math.max(curMx, height[idx]);
			leftMaxHeightArray[idx] = curMx;
		}
		let rightMaxHeightArray = new Array(height.length).fill(0);
		curMx = 0;
		for (let idx = height.length - 1; idx >= 0; idx--) {
			curMx = Math.max(curMx, height[idx]);
			rightMaxHeightArray[idx] = curMx;
		}
		let waterTrapped = 0;
		for (let idx = 0; idx < height.length; idx++) {
			waterTrapped += Math.min(leftMaxHeightArray[idx], rightMaxHeightArray[idx]) - height[idx];
		}
		return waterTrapped;
	}
}
