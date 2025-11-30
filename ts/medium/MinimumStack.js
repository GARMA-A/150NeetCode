class MinStack {
	constructor() {
		this.stack = [];
		this.minstack = [];
	}

	/**
	 * @param {number} val
	 * @return {void}
	 */
	push(val) {
		this.stack.push(val);
		if (this.minstack.length === 0 || this.minstack[this.minstack.length - 1] >= val) {
			this.minstack.push(val);
		}
	}

	/**
	 * @return {void}
	 */
	pop() {
		const top = this.stack.pop()
		if (this.minstack.length > 0 && this.minstack[this.minstack.length - 1] === top) {
			this.minstack.pop();
		}
	}

	/**
	 * @return {number}
	 */
	top() {
		return this.stack[this.stack.length - 1];
	}

	/**
	 * @return {number}
	 */
	getMin() {

		return this.minstack[this.minstack.length - 1];
	}
}
