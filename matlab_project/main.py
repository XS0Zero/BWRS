import numpy as np
import math
from matlab_project.BWRSV1 import BWRSV1_func
from matlab_project.JL3 import JL_func
from matlab_project.G import G_func
from matlab_project.MAXQd import MAXQd_func
import matplotlib.pyplot as plt
import matlab_project.BWRSV1 as BWRSV1

from matlab_project.Mz import Mz_func


def compute(Qg, Ql, r, P1, Pflq, T1, D, n, LL, LL1, LL2, LL3, n1, n2, n3, n4):
    # Qg = 300000  # 气产量m^3/d
    # Ql = 300  # 液体产量m^3/d
    # r = 0.62  # 天然气相对密度
    # P1 = 58.3  # 井口压力MPa
    # Pflq = 10  # 分离器处压力MPa
    # T1 = 54.85  # 节流前温度，℃
    R = 8.314  # 气体常数
    k = 1.2917  # 比热容比
    Tci = 190.69  # 临界温度，K
    Pci = 4.64  # 临界压力,Pa
    # D = 0.062  # 管径,m
    A = math.pi * float(D) ** 2 / 4  # 管截面积
    # n = 10  # 弯头总个数
    Qd = 0 #初始化Qd=0
    P2_bool = '无需一级节流'
    P22_bool = '无需二级节流'
    P222_bool = '无需三级节流'
    d = None
    dd = None
    ddd = None
    T2 = None
    T22 = None
    T222 = None
    P1j1 = None
    P1j2 = None
    P1j3 = None
    Pctiz1 = None
    Pctiz2 = None
    Pctiz3 = None
    Pctiz4 = None

    if r >= 0.7:
        Pc = (4881 - 386.11 * r) / 1000  # 压力,MPa
        Tc = 92 + 176.67 * r  # 温度,℃
    else:
        Pc = (4778 - 248.21 * r) / 1000  # 压力,MPa
        Tc = 92 + 176.67 * r  # 温度,℃
    c = 148

    #######一级节流前摩阻计算#######
    # n1 = 2  # 弯头个数
    # LL = np.zeros((1,n1+1))
    Lep = 30 * D * 1
    for i in range(n1):
        if (i != n1):
            LL[0, i] = LL[0, i] + Lep
        else:
            LL[0, i] = LL[0, i]
    # LL[0,0] = LL[0,0] + Lep
    # LL[0,1] = LL[0,1] + Lep
    # LL[0,2] = 5  # 前面数字代表弯头前的管线长度，弯头的摩阻统一为Lep

    T0 = T1 + 273.15
    den0 = BWRSV1_func(P1, T0)[2]
    Z0 = BWRSV1_func(P1, T0)[0]
    Bg = 3.447e-4 * Z0 * T0 / P1
    V0 = 4 * Qg * Bg / 86400 / math.pi / D ** 2
    # V0 = (Qg * T0 * 0.404 * Z0) / (8.64 * 293 * P1 * 3.1415926 * (D * 100)**2)
    P0, Pctiz1 = Mz_func(V0, LL, D, den0, P1)
    P1 = P0

    #######一级节流#######

    P2, T2, d, Qg1, Z1 = JL_func(P1, T1, Qg, r, k, R, Pc, Tc, Pci, Tci)
    Twash = T2 + 273.15

    Z2 = BWRSV1_func(P2, Twash)[0]  # 一级节流后的压缩因子
    den = BWRSV1_func(P2, Twash)[2]
    pm = (3484.48 * den * P2) / (Z2 * Twash) / 1000  # 一级节流前气体混合物密度 g/cm^3
    Vc = (Qg1 * Twash * 0.404 * Z2) / (8.64 * 293 * P2 * 3.1415926 * (d * 0.1) ** 2)  # 一级节流嘴流速 m/s
    Ve = c / den ** 0.5  # 临界冲蚀速率 m/s
    G1, OW1, Wr1, __ = G_func(Qg, Ql, T1, T2, P1, P2, r)
    # plt.plot(P2, T2, color='blue', marker='.', markersize=16)
    # plt.text(P2, T2, '一级节流')

    #######二级节流前摩阻计算#######

    # n2 = 2  # 弯头个数
    # LL1 = np.zeros(n2 + 1)
    Lep = 30 * D * 1
    # LL1[0] = 1 + Lep
    # LL1[1] = 2 + Lep
    # LL1[2] = 2

    for i in range(n2):
        if (i != n2):
            LL1[0, i] = LL1[0, i] + Lep
        else:
            LL1[0, i] = LL1[0, i]

    P20, Pctiz2 = Mz_func(Vc, LL1, D, den, P2)
    P2 = P20
    P1j1 = P2 + np.sum(Pctiz2)  # 一级节流后压力，MPa

    if P2 > Pflq:
        P11 = P2  # 一级节流后压力（减掉摩阻）
        P2_bool = '不满足产量要求'
    elif P2 <= Pflq:
        GG = G1
        n0 = n - n1 - n2
        Qd = MAXQd_func(den, P2, k, n0, D)  # 二级节流后极限处理产量
        P2_bool = '满足产量要求'
        return d, dd, ddd, T2, T22, T222, P1j1, P1j2, P1j3, P2_bool, P22_bool, P222_bool, Pctiz1, Pctiz2, Pctiz3, Pctiz4,
        raise ValueError('程序已完成,需要一级节流')

    #######二级节流#######
    T11 = T2  # 一级节流后温度
    P22, T22, dd, Qg11, __ = JL_func(P11, T11, Qg, r, k, R, Pc, Tc, Pci, Tci)
    Twash2 = T22 + 273.15  # 二级节流后温度，K
    denn = BWRSV1_func(P22, Twash2)[2]  # 二级节流后的压缩因子
    Z22 = BWRSV1_func(P22, Twash2)[0]
    pmm = (3484.48 * denn * P22) / (Z22 * Twash2) / 1000  # 二级节流前气体混合物密度 kg/m^3
    Vcc = (Qg11 * Twash2 * 0.404 * Z22) / (8.64 * 293 * P22 * 3.1415926 * (dd * 0.1) ** 2)  # 一级节流嘴流速 m/s
    Vee = c / (denn) ** 0.5  # 临界冲蚀速率 m/s
    G2, OW2, Wr2, __ = G_func(Qg, Ql, T11, T22, P11, P22, r)

    # plt.plot(P22, T22, color='red', marker='<', markersize=8)
    # plt.text(P22, T22, '二级节流')

    #######三级节流前摩阻#######
    # n3 = 2  # 弯头个数
    # LL2 = np.zeros(n3 + 1)
    Lep = 30 * D * 1

    # LL2[0] = 1 + Lep
    # LL2[1] = 2 + Lep
    # LL2[2] = 2

    for i in range(n3):
        if (i != n3):
            LL2[0, i] = LL2[0, i] + Lep
        else:
            LL2[0, i] = LL2[0, i]

    P30, Pctiz3 = Mz_func(Vcc, LL2, D, denn, P22)
    P22 = P30
    P1j2 = P22 + np.sum(Pctiz3)  # 三级节流前压力 ?
    if P22 > Pflq:
        P111 = P22  # 二级节流后压力（减掉摩阻后）
        P22_bool = '不满足产量要求'
    elif P22 <= Pflq:
        GG = G1 + G2
        n00 = n - n1 - n2 - n3
        Qd = MAXQd_func(denn, P22, k, n00, D)  # 二级节流后极限处理产量
        P22_bool = '满足产量要求'
        return d, dd, ddd, T2, T22, T222, P1j1, P1j2, P1j3, P2_bool, P22_bool, P222_bool, Pctiz1, Pctiz2, Pctiz3, Pctiz4,
        raise ValueError('程序已完成，需要二级节流')

    #######三级节流#######
    T111 = T22  # 二级节流后温度
    P222, T222, ddd, Qg111, __ = JL_func(P111, T111, Qg, r, k, R, Pc, Tc, Pci, Tci)
    Twash3 = T222 + 273.15  # 二级节流后温度，K
    dennn = BWRSV1_func(P222, Twash3)[2]  # 二级节流后的压缩因子
    Z222 = BWRSV1_func(P222, Twash3)[0]
    pmmm = (3484.48 * dennn * P222) / (Z222 * Twash3) / 1000  # 二级节流前气体混合物密度 kg/m^3
    Vccc = (Qg111 * Twash3 * 0.404 * Z222) / (8.64 * 293 * P222 * 3.1415926 * (ddd * 0.1) ** 2)  # 一级节流嘴流速 m/s
    Veee = c / (dennn) ** 0.5  # 临界冲蚀速率 m/s
    G3 = G_func(Qg, Ql, T111, T222, P111, P222, r)[0]

    plt.plot(P2, T2, color='blue', marker='.', markersize=16)
    # plt.text(P2, T2, '一级节流')
    plt.plot(P22, T22, color='red', marker='<', markersize=8)
    # plt.text(P22, T22, '二级节流')
    plt.plot(P222, T222, color='green', marker='*', markersize=8)
    plt.text(P2, T2, '一级节流')
    plt.text(P22, T22, '二级节流')
    plt.text(P222, T222, '三级节流')
    plt.show()

    #######三级节流后摩阻计算#######
    # n4 = 2  # 到分离器前弯头个数
    # LL3 = np.zeros(n4 + 1)
    Lep = 30 * D * 1

    # LL3[0] = 1 + Lep
    # LL3[1] = 2 + Lep
    # LL3[2] = 2  # 前面数字代表分离器前管线每个弯头前的长度

    for i in range(n4):
        if (i != n4):
            LL3[0, i] = LL3[0, i] + Lep
        else:
            LL3[0, i] = LL3[0, i]

    P40, Pctiz4 = Mz_func(Vccc, LL3, D, dennn, P222)
    P222 = P40
    P1j3 = P222 + sum(Pctiz4)  # 二级节流后压力，MPa ?

    if P222 > Pflq:
        P1111 = P222  # 三级节流后压力
        Qd = MAXQd_func(dennn, Pflq, k, n, D)  # 三级节流后极限处理产量
        P222_bool='不能满足产量要求'
        return d, dd, ddd, T2, T22, T222, P1j1, P1j2, P1j3, P2_bool, P22_bool, P222_bool, Pctiz1, Pctiz2, Pctiz3, Pctiz4, Qd
        raise Exception('程序已完成，不能满足产量要求')
    elif P222 <= Pflq:
        GG = G1 + G2 + G3
        n000 = n - n1 - n2 - n3 - n4
        Qd = MAXQd_func(dennn, P222, k, n000, D)
        P222_bool='满足产量要求'
        return d, dd, ddd, T2, T22, T222, P1j1, P1j2, P1j3, P2_bool, P22_bool, P222_bool, Pctiz1, Pctiz2, Pctiz3, Pctiz4, Qd
        raise Exception('程序已完成，需要三级节流')


