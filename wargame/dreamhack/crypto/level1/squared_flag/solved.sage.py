

# This file was *autogenerated* from the file solved.sage
from sage.all_cmdline import *   # import sage library

_sage_const_46815 = Integer(46815); _sage_const_54436 = Integer(54436); _sage_const_41979 = Integer(41979); _sage_const_52634 = Integer(52634); _sage_const_9427 = Integer(9427); _sage_const_38200 = Integer(38200); _sage_const_30164 = Integer(30164); _sage_const_30742 = Integer(30742); _sage_const_37278 = Integer(37278); _sage_const_27003 = Integer(27003); _sage_const_60542 = Integer(60542); _sage_const_47536 = Integer(47536); _sage_const_61611 = Integer(61611); _sage_const_9732 = Integer(9732); _sage_const_18365 = Integer(18365); _sage_const_23026 = Integer(23026); _sage_const_41731 = Integer(41731); _sage_const_25299 = Integer(25299); _sage_const_3968 = Integer(3968); _sage_const_11754 = Integer(11754); _sage_const_5594 = Integer(5594); _sage_const_13472 = Integer(13472); _sage_const_47963 = Integer(47963); _sage_const_62980 = Integer(62980); _sage_const_14030 = Integer(14030); _sage_const_45400 = Integer(45400); _sage_const_27929 = Integer(27929); _sage_const_22796 = Integer(22796); _sage_const_6570 = Integer(6570); _sage_const_1164 = Integer(1164); _sage_const_9962 = Integer(9962); _sage_const_23574 = Integer(23574); _sage_const_19373 = Integer(19373); _sage_const_17887 = Integer(17887); _sage_const_58878 = Integer(58878); _sage_const_20221 = Integer(20221); _sage_const_52376 = Integer(52376); _sage_const_54543 = Integer(54543); _sage_const_36488 = Integer(36488); _sage_const_25377 = Integer(25377); _sage_const_56175 = Integer(56175); _sage_const_20339 = Integer(20339); _sage_const_35820 = Integer(35820); _sage_const_26224 = Integer(26224); _sage_const_7980 = Integer(7980); _sage_const_43220 = Integer(43220); _sage_const_8400 = Integer(8400); _sage_const_51986 = Integer(51986); _sage_const_54412 = Integer(54412); _sage_const_3511 = Integer(3511); _sage_const_43757 = Integer(43757); _sage_const_22202 = Integer(22202); _sage_const_19450 = Integer(19450); _sage_const_39390 = Integer(39390); _sage_const_19659 = Integer(19659); _sage_const_27620 = Integer(27620); _sage_const_47137 = Integer(47137); _sage_const_36933 = Integer(36933); _sage_const_11093 = Integer(11093); _sage_const_6044 = Integer(6044); _sage_const_4901 = Integer(4901); _sage_const_2205 = Integer(2205); _sage_const_13024 = Integer(13024); _sage_const_12396 = Integer(12396); _sage_const_64 = Integer(64); _sage_const_0x10001 = Integer(0x10001); _sage_const_0 = Integer(0); _sage_const_1 = Integer(1); _sage_const_2 = Integer(2)
from M import M

res = [_sage_const_46815 , _sage_const_54436 , _sage_const_41979 , _sage_const_52634 , _sage_const_9427 , _sage_const_38200 , _sage_const_30164 , _sage_const_30742 , _sage_const_37278 , _sage_const_27003 , _sage_const_60542 , _sage_const_47536 , _sage_const_61611 , _sage_const_9732 , _sage_const_18365 , _sage_const_23026 , _sage_const_41731 , _sage_const_25299 , _sage_const_3968 , _sage_const_11754 , _sage_const_5594 , _sage_const_13472 , _sage_const_47963 , _sage_const_62980 , _sage_const_14030 , _sage_const_45400 , _sage_const_27929 , _sage_const_22796 , _sage_const_6570 , _sage_const_1164 , _sage_const_9962 , _sage_const_23574 , _sage_const_19373 , _sage_const_17887 , _sage_const_58878 , _sage_const_20221 , _sage_const_52376 , _sage_const_54543 , _sage_const_36488 , _sage_const_25377 , _sage_const_56175 , _sage_const_20339 , _sage_const_35820 , _sage_const_26224 , _sage_const_7980 , _sage_const_43220 , _sage_const_8400 , _sage_const_51986 , _sage_const_54412 , _sage_const_3511 , _sage_const_43757 , _sage_const_22202 , _sage_const_19450 , _sage_const_39390 , _sage_const_19659 , _sage_const_27620 , _sage_const_47137 , _sage_const_36933 , _sage_const_11093 , _sage_const_6044 , _sage_const_4901 , _sage_const_2205 , _sage_const_13024 , _sage_const_12396 ]

n = _sage_const_64 
a = _sage_const_0x10001 
Zm = Zmod(a)

for idx, c in zip([_sage_const_0 , _sage_const_1 , _sage_const_2 , n - _sage_const_1 ], b"DH{}"):
    v = [_sage_const_0 ] * _sage_const_64 
    v[idx] = _sage_const_1 

    M.append(v)
    res.append(c)

M = Matrix(Zm, M)
res = vector(Zm, res)

flag = M.solve_right(res)
flag = [ZZ(k) for k in flag]
flag = bytes(flag).decode()

print(flag)

