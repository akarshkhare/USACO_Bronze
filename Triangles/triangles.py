infile = open('triangles.in', 'r')
out = open('triangles.out', 'w')
x = infile.readline()
posts = []
for i in range(int(x)):
    y = infile.readline().split()
    y[0] = int(y[0])
    y[1] = int(y[1])
    posts.append(y)
#print(posts)
xdif = 0
ydif = 0
temp = 0
max = 0
for i in range(len(posts)):
    for j in range(len(posts)):
        if [posts[i][0],posts[j][1]] in posts or [posts[j][0],posts[i][1]] in posts:
            xdif = abs(posts[i][0]-posts[j][0])
            ydif = abs(posts[i][1]-posts[j][1])
            temp = xdif * ydif
            if temp > max:
                max = temp
out.write(str(max))
out.close()