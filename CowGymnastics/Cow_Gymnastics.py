infile = open('gymnastics.in', 'r')
out = open('gymnastics.out', 'w')
vals = infile.readline().split()
x = []
for i in range(int(vals[0])):
    a = infile.readline().split()
    a = [int(y) for y in a]
    x.append(a)
#print(x)
z = []
for i in range(int(vals[1])):
    z.append([0]*int(vals[1]))
#print(z)
for i in range(len(x)):
    for j in range(len(x[i])):
        for k in range(j,len(x[i])):
            #print(x[k],x[j],j,k)
            if z[(x[i][k]-1)][(x[i][j]-1)] == 0:
                z[x[i][k]-1][x[i][j]-1] = -1
            #print(k+1,j+1,z)
cntr = 0
for i in range(len(z)):
    for j in range(len(z[i])):
        if z[i][j] == 0:
            cntr += 1
out.write(str(cntr))
out.close()