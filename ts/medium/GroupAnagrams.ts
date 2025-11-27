class Solution {
	groupAnagrams(strs: string[]): string[][] {
		let mp = new Map<string, string[]>();
		for (const el of strs) { // N*Klong(K) // solution
			const sorted = el.split("").sort().join("");
			if (!mp.has(sorted)) {
				mp.set(sorted, []);
			}
			mp.get(sorted)!.push(el);
		}
		return Array.from(mp.values());
	}

	groupAnagrams2(strs: string[]): string[][] {
		let mp = new Map<string, string[]>();
		// N*M solution where N is size of the array and M size of the string
		// best solution !!
		for (const str of strs) {
			const counter = new Array(26).fill(0);
			for (let idx = 0; idx < str.length; idx++) {
				const index = str.charCodeAt(idx) - 97;
				counter[index]++;
			}
			const key = counter.join("#");
			if (!mp.has(key)) {
				mp.set(key, []);
			}
			mp.get(key)!.push(str);
		}

		return Array.from(mp.values());
	}
}
