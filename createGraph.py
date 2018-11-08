import networkx as nx
import random
import sys


num_student = int(sys.argv[2])

# if sys.argv[1] == 's':
#     # 25 - 50 students max 100 rowdy groups
#     num_student = random.randint(25, 50)
#     print("Small: " + str(num_student) + "\n")
#
# elif sys.argv[1] == 'm':
#     # 250 - 500 students max 1000 rowdy groups
#     num_student = random.randint(250, 500)
#     print("Medium: " + str(num_student) + "\n")
#
#
# elif sys.argv[1] == 'l':
#     # 500 - 1000 students max 2000 rowdy groups
#     num_student = random.randint(500, 1000)
#     print("Large: " + str(num_student) + "\n")


R = nx.gnm_random_graph(num_student, int(sys.argv[3]))

# print("Vertices: " + str(list(R.nodes)) + "\n")
# print("Edges: " + str(list(R.edges)) + "\n")

# k = number of buses, s = capacity of buses
k = sys.argv[5]
s = sys.argv[6]

# number of rowdy groups
num_rowdy = int(sys.argv[4])
rowdy_groups = []

for i in range(num_rowdy):
    rowdy_group = random.sample(range(0, num_student-1), random.randint(3, 5))
    rowdy_group.sort()
    rowdy_group = list(map(str, rowdy_group))

    while rowdy_group in rowdy_groups:
        rowdy_group = random.sample(range(0, num_student-1), random.randint(3, 5))
        rowdy_group.sort()
        rowdy_group = list(map(str, rowdy_group))

    rowdy_groups.append(rowdy_group)

# print("Rowdy Groups: \n" + str(rowdy_groups) + "\n")


if sys.argv[1] == 's':
    nx.write_gml(R, "./all_inputs/small/easy/graph.gml")
    with open('./all_inputs/small/easy/parameters.txt', 'w') as o:
        o.write("%s\n" % str(k))
        o.write("%s\n" % str(s))
        for group in rowdy_groups:
            o.write("%s\n" % group)

elif sys.argv[1] == 'm':
    nx.write_gml(R, "./all_inputs/medium/easy/graph.gml")
    with open('./all_inputs/medium/easy/parameters.txt', 'w') as o:
        o.write("%s\n" % str(k))
        o.write("%s\n" % str(s))
        for group in rowdy_groups:
            o.write("%s\n" % group)

elif sys.argv[1] == 'l':
    nx.write_gml(R, "./all_inputs/large/easy/graph.gml")
    with open('./all_inputs/large/easy/parameters.txt', 'w') as o:
        o.write("%s\n" % str(k))
        o.write("%s\n" % str(s))
        for group in rowdy_groups:
            o.write("%s\n" % group)



