danhsach1 = [1., 3.]
danhsach2 = [5., 7.]
danhsach = danhsach1 + danhsach2
print(danhsach)
danhsach_gapdoi = 2 * danhsach
print(danhsach_gapdoi)
danhsach_chiadoi = [x / 2 for x in danhsach]
print("danhsach_chiadoi:", danhsach_chiadoi)

mon_hoc = ["ToanCC", "DSTT", "ToanRR", "LaptrinhCB"]
thu_tu = [2, 3, 4, 1]
diem_so = [10, 9, 8, 7]

anh_xa = zip(thu_tu, mon_hoc, diem_so)
print(anh_xa)

tap_hop = set(anh_xa)
print(tap_hop)

anh_xa = zip(thu_tu, mon_hoc, diem_so)
lay_TT, lay_monhoc , lay_diem = zip(*anh_xa) 
print("lay_monhoc:", lay_monhoc)
list(zip(range(4), range(7, 12), reversed(range(11))))