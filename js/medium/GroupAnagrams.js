class Solution {
	/**
	 * @param {string[]} strs
	 * @return {string[][]}
	 */
	groupAnagrams(strs) {

		const res = {};
		for (const str of strs) {
			const arr = new Array(26).fill(0);
			for (const ch of str)
				arr[ch.charCodeAt(0) - 'a'.charCodeAt(0)] += 1;
			const key = arr.join(",");
			if (!res[key]) {
				res[key] = [];
			}
			res[key].push(str);
		}
		return Object.values(res);
	}
}

const s = new Solution();
console.log(s.groupAnagrams(["good", "gdo", "dogo", "odg", "har"]));
