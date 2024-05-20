from M import M

res = [46815, 54436, 41979, 52634, 9427, 38200, 30164, 30742, 37278, 27003, 60542, 47536, 61611, 9732, 18365, 23026, 41731, 25299, 3968, 11754, 5594, 13472, 47963, 62980, 14030, 45400, 27929, 22796, 6570, 1164, 9962, 23574, 19373, 17887, 58878, 20221, 52376, 54543, 36488, 25377, 56175, 20339, 35820, 26224, 7980, 43220, 8400, 51986, 54412, 3511, 43757, 22202, 19450, 39390, 19659, 27620, 47137, 36933, 11093, 6044, 4901, 2205, 13024, 12396]

n = 64
a = 0x10001
Zm = Zmod(a)

for idx, c in zip([0, 1, 2, n - 1], b"DH{}"):
    v = [0] * 64
    v[idx] = 1

    M.append(v)
    res.append(c)

M = Matrix(Zm, M)
res = vector(Zm, res)

flag = M.solve_right(res)
flag = [ZZ(k) for k in flag]
flag = bytes(flag).decode()

print(flag)