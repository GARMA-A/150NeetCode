class Solution {
	isPalindrome(s: string): boolean {
		s = s.toLowerCase();
		let [l, r] = [0, s.length - 1];
		let specialChar = /\W|_/;

		while (l < r) {
			if (specialChar.test(s[l])) {
				l++;
			} else if (specialChar.test(s[r])) {
				r--;
			} else if (s[l] !== s[r]) {
				return false
			} else {
				r--;
				l++;
			}
		}

		return true;
	}
}
