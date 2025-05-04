class Node:
    def __init__(self, name, dependencies, compute_fn):
        self.name = name
        self.dependencies = dependencies
        self.compute_fn = compute_fn


def compute(graph, inputs, outputs):
    computed = dict(inputs)

    def compute_node(node_name):
        if node_name in computed:
            return computed[node_name]

        if node_name not in graph:
            raise ValueError(f"Node {node_name} not in graph and not provided as input")

        node = graph[node_name]
        args = [compute_node(dep) for dep in node.dependencies]
        value = node.compute_fn(*args)
        computed[node_name] = value
        return value

    result = {}
    for output in outputs:
        if output not in graph and output not in inputs:
            raise ValueError(f"Output {output} cannot be computed or found in inputs")
        result[output] = compute_node(output)

    return result


def compute_a():
    return 1


def compute_b(a):
    return a + 2  # a linear shift


def compute_c(a):
    return a * 3  # a scaling factor


def compute_d(a, b, c):
    return a + b + c


def compute_e(a, c, d):
    return a + c + d


# Custom graph
graph_custom = {
    'A': Node('A', [], compute_a),
    'B': Node('B', ['A'], compute_b),
    'C': Node('C', ['A'], compute_c),
    'D': Node('D', ['A', 'B', 'C'], compute_d),
    'E': Node('E', ['A', 'C', 'D'], compute_e),
}
