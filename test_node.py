import pytest
from node import compute, graph_custom

# A = 1
# D = A + B + C = 1 + 3 + 3 = 7
# E = A + C + D = 1 + 3 + 7 = 11

# A = 2
# D = A + B + C = 2 + 4 + 6 = 12
# E = A + C + D = 2 + 6 + 12 = 20


@pytest.mark.parametrize("test_input,expected", [(1, {'D': 7, 'E': 11}), (2, {'D': 12, 'E': 20})])
def test_compute(test_input, expected):
    inputs = {'A': test_input}
    outputs = ['D', 'E']
    result = compute(graph_custom, inputs, outputs)
    assert result == result


def test_compute_non_existing_node():
    inputs = {'A': 1}
    outputs = ['F', 'E']
    with pytest.raises(ValueError, match="Output F cannot be computed or found in inputs"):
        compute(graph_custom, inputs, outputs)
