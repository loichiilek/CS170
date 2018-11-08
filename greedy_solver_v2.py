from collections import defaultdict
import random
import networkx as nx


def greedy_solver(G, num_buses, bus_cap, constraints):
    def score_graph(G, nodes_in_bus, constraints):
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
    temp_node_list = list(G.nodes)
    random.shuffle(temp_node_list)
    for node in temp_node_list:
        buses[bus_num].append(node)
        bus_alloc[node] = bus_num
        bus_num = (bus_num + 1) % num_buses
        print('done allocating buses')

    # 2. for each node, calculate score for shifting node to another bus and find max bus
    for node in G.nodes:
        max_swap_score = 0
        swap_bus = None

        # initialize base scores which are the scores of the bus the node currently belong to
        base_score = score_graph(G, buses[bus_alloc[node]], constraints)
        new_base_score = score_graph(G, buses[bus_alloc[node]].copy().remove(node), constraints)

        for i in range(num_buses):
            # calculate swap_score
            swap_score = score_graph(G, buses[i].copy().append(node), constraints) \
                         + new_base_score \
                         - score_graph(G, buses[i], constraints) \
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

        #else do nothing













        # bus_scores = {}
        # new_bus_scores = {}
        # for i in range(num_buses):
        #     if len(buses[i]) < bus_cap:
        #         bus_scores[i] = score_graph(G, buses[i], constraints)
        #         new_bus_scores[i] = score_graph(G, buses[i].append(node), constraints)
        #     else:
        #         bus_scores[i] = 999
        #         new_bus_scores[i] = 999

    # # 3. check constraints
    # for bus_num, bus_list in buses.items():
    #     for constraint in constraints:
    #         # if does not meet constraint
    #         if set(constraint).issubset(bus_list):
    #             # choose node with least neighbors
    #             neighbor_dict = dict()
    #             for node in bus_list:
    #                 neighbors = list(G.subgraph(bus_list).neighbors(node))
    #                 neighbor_dict[node] = neighbors
    #             min_node = min(neighbor_dict, key=neighbor_dict.get)
    #             # move to another random?/ OR available bus
    #             rand_bus = (bus_alloc[min_node] + random.randint(1, num_buses - 1)) % num_buses  # random bus
    #             buses[bus_alloc[min_node]].remove(min_node)
    #             buses[rand_bus].append(min_node)
    #             bus_alloc[node] = rand_bus

    return buses
