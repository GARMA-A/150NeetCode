class Solution {
	/**
	 * @param {string} s
	 * @param {string} t
	 * @return {boolean}
	 */
	isAnagram(s, t) {
		if (s.length !== t.length) {
			return false;
		}
		let counts = {}, countt = {};
		for (let i = 0; i < s.length; i++) {
			counts[s[i]] = (counts[s[i]] || 0) + 1;
			countt[t[i]] = (countt[t[i]] || 0) + 1;
		}
		console.log(counts, countt);

		for (const key in counts) {
			if (counts[key] !== countt[key]) {
				return false;
			}

		}

		return true;


	}
}



const s = new Solution();

console.log(s.isAnagram("a", "jam"));



