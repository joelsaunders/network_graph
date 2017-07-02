import networkx as nx
import matplotlib.pyplot as plt
from networkx.drawing.nx_agraph import graphviz_layout


class Compiler:

    def find_predecessors(self, graph):
        return graph.predecessors(self)

    def find_sucessors(self, graph):
        return graph.successors(self)

    def compile(self):
        print('compiled {}'.format(self.__class__.__name__))


class CompilerOne(Compiler):
    @staticmethod
    def requirements():
        return []


class CompilerTwo(Compiler):
    @staticmethod
    def requirements():
        return [CompilerOne, CompilerThree]


class CompilerThree(Compiler):
    @staticmethod
    def requirements():
        return []


class CompilerFour(Compiler):
    @staticmethod
    def requirements():
        return []


class CompilerFive(Compiler):
    @staticmethod
    def requirements():
        return [CompilerFour]


class CompilerSix(Compiler):
    @staticmethod
    def requirements():
        return [CompilerTwo, CompilerFive]


class CompilerSeven(Compiler):
    @staticmethod
    def requirements():
        return [CompilerFour]


class CompilerEight(Compiler):
    @staticmethod
    def requirements():
        return [CompilerSeven]


class CompilerNine(Compiler):
    @staticmethod
    def requirements():
        return []


class CompilerTen(Compiler):
    @staticmethod
    def requirements():
        return [CompilerNine]


class CompileManager:
    def __init__(self, fields, graph):
        self.fields = fields
        self.graph = graph

    # def find_successors_tree(self):
    #     return nx.algorithms.dfs_successors(self.graph, self.field)

    def find_subgraph_nodes(self, field):
        sub_graphs = [x for x in nx.weakly_connected_components(self.graph)]
        for graph in sub_graphs:
            if field in graph:
                return graph
        return None

    def sort_subgraph_nodes(self):
        recompile_nodes = set()
        # Todo: optimisation here: if node already in set then assume entire sub-graph is
        for field in self.fields:
            nodes = self.find_subgraph_nodes(field)
            recompile_nodes.update(nodes)
        return nx.topological_sort(graph, nbunch=recompile_nodes)

    def compile(self):
        for node in self.sort_subgraph_nodes():
            node().compile()


def create_graph(compilers):
    # create graph
    G = nx.DiGraph()
    # add nodes

    for compiler in compilers:
        # G.add_node(comp)
        for requirement in compiler.requirements():
            G.add_edge(requirement, compiler)
    return G

compilers = [
    CompilerOne,
    CompilerTwo,
    CompilerThree,
    CompilerFour,
    CompilerFive,
    CompilerSix,
    CompilerSeven,
    CompilerEight,
    CompilerNine,
    CompilerTen
]


graph = create_graph(compilers)
compile_field = CompileManager([CompilerOne], graph)
compile_field.compile()

# print(nx.algorithms.dfs_successors(graph, CompilerFour))

# pos = graphviz_layout(graph, prog='dot')
# # # nicer labels
# labels = {v: v.__name__ for v in compilers}
# nx.draw(graph, with_labels=True, pos=pos, labels=labels)
# plt.savefig("path_graph1.png")
# plt.show()

print('done')
