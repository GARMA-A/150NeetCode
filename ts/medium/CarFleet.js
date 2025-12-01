class Solution {
	/**
	 * @param {number} target
	 * @param {number[]} position
	 * @param {number[]} speed
	 * @return {number}
	 */
	carFleet(target, position, speed) {
		if (position.length === 0) return 0;
		let posSpeedArr = position
			.map((p, idx) => [p, speed[idx]])
			.sort((a, b) => a[0] - b[0]);

		let [lastCarPos, lastCarSpeed] = posSpeedArr[posSpeedArr.length - 1];
		let frontCarTimeToArrive = (target - lastCarPos) / lastCarSpeed;
		let fleetCounter = 1;

		for (let idx = posSpeedArr.length - 2; idx >= 0; idx--) {
			let [currentPos, currentSpeed] = posSpeedArr[idx]

			let currentTime = (target - currentPos) / currentSpeed;
			if (frontCarTimeToArrive < currentTime) {
				fleetCounter++;
				frontCarTimeToArrive = currentTime;
			}
		}
		return fleetCounter;

	}
}




