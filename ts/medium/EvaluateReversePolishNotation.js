
class Solution {
	/**
	 * @param {string[]} tokens
	 * @return {number}
	 */
	evalRPN(tokens) {
		const stack = [];
		for (const token of tokens) {
			if (token === "+") {
				const first = stack.pop();
				const second = stack.pop()
				stack.push(second + first);
			} else if (token === "-") {
				const first = stack.pop();
				const second = stack.pop()
				stack.push(second - first);
			} else if (token === "/") {
				const first = stack.pop();
				const second = stack.pop()
				stack.push(Math.trunc(second / first));
			} else if (token === "*") {
				const first = stack.pop();
				const second = stack.pop()
				stack.push(second * first);
			} else {
				stack.push(parseInt(token));
			}

		}
		return stack.pop();
	}
}
