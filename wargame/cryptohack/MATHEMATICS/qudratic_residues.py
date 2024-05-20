p = 29
ints = [14, 6, 11]
q_r = []

for i in range(1, (p-1)//2):
    q_r.append(i*i%p)

for i in range(len(ints)):
    if(ints[i] in q_r):
        print(q_r.index(ints[i])+1)