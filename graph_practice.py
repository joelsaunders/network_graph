import networkx as nx
import matplotlib.pyplot as plt
from networkx.drawing.nx_agraph import graphviz_layout

class Compiler:
    name = None

    def find_predecessors(self, graph):
        return graph.predecessors(self.name)

    def find_sucessors(self, graph):
        return graph.successors(self.name)


class CompilerOne(Compiler):
    name = 'one'

    def __init__(self):
        self.requirements = []


class CompilerTwo(Compiler):
    name = 'two'

    def __init__(self):
        self.requirements = [CompilerOne, CompilerThree]


class CompilerThree(Compiler):
    name = 'three'

    def __init__(self):
        self.requirements = []


class CompilerFour(Compiler):
    name = 'four'

    def __init__(self):
        self.requirements = []


class CompilerFive(Compiler):
    name = 'five'

    def __init__(self):
        self.requirements = [CompilerFour]


class CompilerSix(Compiler):
    name = 'six'

    def __init__(self):
        self.requirements = [CompilerTwo, CompilerFive]


class CompilerSeven(Compiler):
    name = 'seven'

    def __init__(self):
        self.requirements = [CompilerFour]


class CompilerEight(Compiler):
    name = 'eight'

    def __init__(self):
        self.requirements = [CompilerSeven]


class CompilerNine(Compiler):
    name = 'nine'

    def __init__(self):
        self.requirements = []


class CompilerTen(Compiler):
    name = 'ten'

    def __init__(self):
        self.requirements = [CompilerNine]


class Compile:
    def __init__(self, field, graph):
        self.field = field
        self.graph = graph

    def find_successors_tree(self):
        return nx.algorithms.dfs_successors(self.graph, self.field)

    def find_subgraph_nodes(self):
        sub_graphs = [x for x in nx.weakly_connected_components(self.graph)]
        for graph in sub_graphs:
            if self.field in graph:
                return graph
        return None

    def sort_subgraph_nodes(self):



def create_graph(compilers):
    # create graph
    G = nx.DiGraph()
    # add nodes

    for comp in compilers:
        # G.add_node(comp)
        for requirement in comp.requirements:
            G.add_edge(requirement.name, comp.name)
    return G

compiler_mapping = dict(
    comp1 = CompilerOne(),
    comp2 = CompilerTwo(),
    comp3 = CompilerThree(),
    comp4 = CompilerFour(),
    comp5 = CompilerFive(),
    comp6 = CompilerSix(),
    comp7 = CompilerSeven(),
    comp8 = CompilerEight(),
    comp9 = CompilerNine(),
    comp10 = CompilerTen()
)
compilers = compiler_mapping.values()

graph = create_graph(compilers)
compile_field = Compile(compiler_mapping['comp2'].name, graph)

# print(compiler_mapping['comp2'].find_predecessors(graph))
# print(compile_field.find_successors_tree())


# pos = graphviz_layout(graph, prog='dot')
# nx.draw(graph, with_labels=True)
# plt.savefig("path_graph1.png")
# plt.show()

print('done')
