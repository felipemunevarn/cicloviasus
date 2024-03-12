f1 = open("C:/Users/Administrator/Downloads/ListadoProductos.csv", 'r')
f2 = open("C:/Users/Administrator/Documents/cicloviasus/test.html", 'r')
lines1 = f1.readlines()
lines2 = f2.readlines()
for line1 in lines1:
    search = '<img alt="'
    search += line1.split(",")[1]
    print(search)
    # for idx, line2 in enumerate(lines2, start=1):
    #     if search in line2:
    #         print(f"'{search}' found in line {idx}: {line2}")
    #         break
