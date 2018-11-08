from collections import defaultdict
import random


def greedy_solver(G, num_buses, bus_cap, constraints):
    buses = defaultdict(list)  # maps which people are in a bus numbered 1:num_buses
    bus_alloc = dict()  # maps which bus a person is in
    # 1. randomly initialize buses
    for node in G.nodes:
        rand = random.randint(0, num_buses - 1)
        while 1:
            # if bus is below capacity
            if len(buses[rand]) < bus_cap:
                buses[rand].append(node)
                bus_alloc[node] = rand
                break
            # add to another random bus
            else:
                rand = random.randint(0, num_buses - 1)

    # 2. while number of friends can be increased, shift person
    friend_count = [0 for x in range(num_buses)]
    node_list = list(G.nodes)
    while len(node_list) > 0:
        # get the number of friends in each bus
        node = random.choice(node_list)
        for bus_num in range(1, num_buses + 1):
            for neighbor in G.neighbors(node):
                if neighbor in buses[bus_num]:
                    friend_count[bus_num] += 1
        while (1):
            # get the best possible bus he could go to
            best_bus = friend_count.index(max(friend_count))
            # if there is an improvement
            if len(buses[best_bus]) > len(buses[bus_alloc[node]]):
                # and if the bus is under capacity, change bus
                if len(buses[best_bus]) < bus_cap:
                    print('shifting friend')
                    buses[bus_alloc[node]].remove(node)
                    buses[best_bus].append(node)
                    bus_alloc[node] = best_bus
                    break
            # if best bus is the same, don't shift
            else:
                break
            friend_count.remove(friend_count[best_bus])
            print('removed friend_count, length', len(friend_count))

        # remove node from nodelist
        node_list.remove(node)
        print('removed node, length', len(node_list))

    # 3. check constraints
    for bus_num, bus_list in buses.items():
        for constraint in constraints:
            # if does not meet constraint
            if set(constraint).issubset(bus_list):
                # choose node with least neighbors
                neighbor_dict = dict()
                for node in bus_list:
                    neighbors = list(G.subgraph(bus_list).neighbors(node))
                    neighbor_dict[node] = neighbors
                min_node = min(neighbor_dict, key=neighbor_dict.get)
                # move to another random?/ OR available bus
                rand_bus = (bus_alloc[min_node] + random.randint(1, num_buses - 1)) % num_buses  # random bus
                buses[bus_alloc[min_node]].remove(min_node)
                buses[rand_bus].append(min_node)
                bus_alloc[node] = rand_bus

    # if we want to find buses which meet all constraints
    def check_bus(buses, constraint):
        for bus in buses.items():
            if not set(constraint).issubset(bus_list):
                if len(bus) < bus_cap:
                    return bus

    return buses
