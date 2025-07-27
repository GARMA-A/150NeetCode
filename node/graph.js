const Graph = {
	A: ['B', 'C'],
	B: ['F'],
	C: ['E', 'D'],
	D: [],
	E: []
}

const DFS = (graph = Graph, source = 'A') => {
	const stack = [source];
	while (stack.length > 0) {
		const current = stack.pop();
		console.log(current, " ")
		for (const ch of graph[current]) {
			stack.push(ch);
		}
	}

}
DFS();

