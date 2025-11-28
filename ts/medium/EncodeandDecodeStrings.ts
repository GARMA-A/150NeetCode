class Solution {
	encode(strs: string[]): string {
		let encode = "";
		for (const str of strs) {
			encode += `${str.length}#` + str;
		}
		return encode;
	}

	decode(str: string): string[] {
		let decode: string[] = [];
		let i = 0;
		while (i < str.length) {
			let counter = 0;
			let numberStr = "";
			while (/[0-9]/.test(str[i]) && /[0-9]/.test(str[i])) {
				numberStr += str[i];
				i += 1;
			}
			i++;
			counter = parseInt(numberStr);
			decode.push(str.slice(i, i + counter));
			i += counter;
		}
		return decode;
	}
}
