import networkx as nx
import random
import sys

if sys.argv[1] == 's':
    # 25 - 50 students max 100 rowdy groups
    num_student = random.randint(25, 50)
    print("Small: " + str(num_student) + "\n")

    R = nx.gnm_random_graph(num_student, int(sys.argv[2]))

    print("Vertices: " + str(list(R.nodes)) + "\n")
    print("Edges: " + str(list(R.edges)) + "\n")

    # k = number of buses, s = capacity of buses
    k = 5
    s = 10

    # number of rowdy groups
    num_rowdy = int(sys.argv[3])
    rowdy_groups = []

    for i in range(num_rowdy):
        rowdy_groups.append(random.sample(range(0, num_student-1), random.randint(3, 5)))

    print("Rowdy Groups: \n" + str(rowdy_groups))

elif sys.argv[1] == 'm':
    print("medium")
    # 250 - 500 students max 1000 rowdy groups


elif sys.argv[1] == 'l':
    print("large")
    # 500 - 1000 students max 2000 rowdy groups



