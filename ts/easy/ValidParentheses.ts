class Solution {
	isValid(s: string): boolean {
		const stack = [];
		for (const el of s) {
			switch (el) {
				case "{":
				case "[":
				case "(":
					stack.push(el);
					break;
				case "}":
					if (stack.length === 0 || stack.pop() !== '{') {
						return false;
					}
					break;
				case ")":
					if (stack.length === 0 || stack.pop() !== '(') {
						return false;
					}
					break;
				case "]":
					if (stack.length === 0 || stack.pop() !== '[') {
						return false;
					}
					break;
			}

		}

		return stack.length === 0;
	}
}
