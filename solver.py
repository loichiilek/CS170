import networkx as nx
import os
from collections import defaultdict
import random

###########################################
# Change this variable to the path to 
# the folder containing all three input
# size category folders
###########################################
path_to_inputs = "./all_inputs"

###########################################
# Change this variable if you want
# your outputs to be put in a 
# different folder
###########################################
path_to_outputs = "./outputs"

def parse_input(folder_name):
    '''
        Parses an input and returns the corresponding graph and parameters

        Inputs:
            folder_name - a string representing the path to the input folder

        Outputs:
            (graph, num_buses, size_bus, constraints)
            graph - the graph as a NetworkX object
            num_buses - an integer representing the number of buses you can allocate to
            size_buses - an integer representing the number of students that can fit on a bus
            constraints - a list where each element is a list vertices which represents a single rowdy group
    '''
    graph = nx.read_gml(folder_name + "/graph.gml")
    parameters = open(folder_name + "/parameters.txt")
    num_buses = int(parameters.readline())
    size_bus = int(parameters.readline())
    constraints = []
    
    for line in parameters:
        line = line[1: -2]
        curr_constraint = [num.replace("'", "") for num in line.split(", ")]
        constraints.append(curr_constraint)

    return graph, num_buses, size_bus, constraints

def solve(graph, num_buses, size_bus, constraints):
    def score_graph(G, nodes_in_bus, constraints):

        if not nodes_in_bus:
            return 0

        deactivated = set()
        for constraint in constraints:
            if set(constraint).issubset(nodes_in_bus):
                deactivated.update(constraint)
        new_nodes = [i for i in nodes_in_bus if i not in list(deactivated)]
        sub = G.subgraph(new_nodes)
        # plot_graph(sub)
        return len(sub.edges)

    buses = defaultdict(list)  # maps which people are in a bus numbered 1:num_buses
    bus_alloc = dict()  # maps which bus a person is in

    # 1. randomly initialize buses
    bus_num = 0
    temp_node_list = list(graph.nodes)
    random.shuffle(temp_node_list)
    for node in temp_node_list:
        buses[bus_num].append(node)
        bus_alloc[node] = bus_num
        bus_num = (bus_num + 1) % num_buses

    print('done allocating buses')
    # 2. for each node, calculate score for shifting node to another bus and find max bus
    for node in graph.nodes:
        max_swap_score = 0
        swap_bus = None

        # initialize base scores which are the scores of the bus the node currently belong to
        base_score = score_graph(graph, buses[bus_alloc[node]], constraints)
        new_base_score = score_graph(graph, buses[bus_alloc[node]].copy().remove(node), constraints)

        for i in range(num_buses):
            # calculate swap_score
            swap_score = score_graph(graph, buses[i].copy().append(node), constraints) \
                         + new_base_score \
                         - score_graph(graph, buses[i], constraints) \
                         - base_score

            # if larger swap_score, update max_swap_score and indicate bus to do swap
            if swap_score > max_swap_score:
                max_swap_score = swap_score
                swap_bus = i

        # swapping condition is positive
        if swap_bus is not None:
            # remove from original bus
            buses[bus_alloc[node]].remove(node)
            # add to new bus
            buses[swap_bus].append(node)
            # update back pointer
            bus_alloc[node] = swap_bus

    return buses

def main():
    '''
        Main method which iterates over all inputs and calls `solve` on each.
        The student should modify `solve` to return their solution and modify
        the portion which writes it to a file to make sure their output is
        formatted correctly.
    '''
    size_categories = ["small", "medium", "large"]
    if not os.path.isdir(path_to_outputs):
        os.mkdir(path_to_outputs)

    for size in size_categories:
        category_path = path_to_inputs + "/" + size
        output_category_path = path_to_outputs + "/" + size
        category_dir = os.fsencode(category_path)

        # print(os.listdir(category_dir))
        # print(category_path)
        
        if not os.path.isdir(output_category_path):
            os.mkdir(output_category_path)

        for input_folder in os.listdir(category_dir):
            # print(input_folder)
            input_name = os.fsdecode(input_folder)
            # print(input_name)
            graph, num_buses, size_bus, constraints = parse_input(category_path + "/" + input_name)
            solution = solve(graph, num_buses, size_bus, constraints)
            output_file = open(output_category_path + "/" + input_name + ".out", "w")

            for bus in solution:
                output_file.write("%s\n" % solution[bus])

            output_file.close()

if __name__ == '__main__':
    main()


