f = open("C:/Users/Administrator/Downloads/1 CRISTO LP HEB-100 500.STD", 'r', encoding='utf-8')
nodes, coords = [], []
for line in f:
    if "MEMBER INCIDENCES" in line:
        nodes = next(f).split(";")
        nodes = nodes[:-1]
        for i, node in enumerate(nodes):
            nodes[i] = node.lstrip().rstrip()
f2 = open("C:/Users/Administrator/Downloads/1 CRISTO LP HEB-100 500.STD", 'r', encoding='utf-8')
for line in f2:
    if "JOINT COORDINATES" in line:
        coords = next(f2).split(";")
        coords = coords[:-1]
        for i, coord in enumerate(coords):
            coords[i] = coord.lstrip().rstrip()
f3 = open("C:/Users/Administrator/Downloads/test.scr", 'a', encoding='utf-8')
for beam in nodes:
    f3.write("line")
    f3.write("\n")
    node_a = beam.split(" ")[1]
    node_b = beam.split(" ")[2]
    f3.write((coords[int(node_a) - 1][2:]).replace(" ",","))
    f3.write("\n")
    f3.write((coords[int(node_b) - 1][2:]).replace(" ",","))
    f3.write("\n")
    f3.write("\n")
    f3.write("ucs")
    f3.write("\n")
    f3.write((coords[int(node_a) - 1][2:]).replace(" ",","))
    f3.write("\n")
    f3.write("\n")
    f3.write("ucs")
    f3.write("\n")
    f3.write("za")
    f3.write("\n")
    f3.write((coords[int(node_a) - 1][2:]).replace(" ",","))
    f3.write("\n")
    f3.write((coords[int(node_b) - 1][2:]).replace(" ",","))
    f3.write("\n")
    f3.write("\n")

