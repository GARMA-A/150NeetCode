class Solution {
	isAnagram(s: string, t: string): boolean {
		if (s.length != t.length)
			return false;
		let arr: number[] = new Array(26).fill(0);
		for (let idx = 0; idx < s.length; idx++) {
			arr[s.charCodeAt(idx) - 'a'.charCodeAt(0)]++;
			arr[t.charCodeAt(idx) - 'a'.charCodeAt(0)]--;
		}
		for (let i = 0; i < 26; i++) {
			if (arr[i] !== 0) {
				return false;
			}

		}
		return true;
	}
}
