import numpy as np


def BWRSV1_func(P, T):
    z = np.transpose(np.array([[0.952, 0, 0.048, 0, 0, 0, 0, 0, 0, 0]]))

    M = np.array([[16, 30, 44, 58, 58, 72, 72, 44, 28, 34]])

    k = np.array([[0, 0, 0.035, 0.05, 0.048, 0.045, 0.05, 0.05, 0.05, 0.05],
                  [0, 0, 0, 0.025, 0.07, 0.1, 0.11, 0.12, 0.134, 0.134],
                  [0.035, 0, 0, 0.05, 0.045, 0.04, 0.036, 0.034, 0.028, 0.028],
                  [0.05, 0.025, 0.05, 0, 0.01, 0.023, 0.0275, 0.031, 0.036, 0.041],
                  [0.048, 0.07, 0.045, 0.01, 0, 0.0031, 0.004, 0.0045, 0.005, 0.006],
                  [0.045, 0.1, 0.04, 0.023, 0.0031, 0, 0.003, 0.0035, 0.004, 0.0045],
                  [0.05, 0.11, 0.036, 0.0275, 0.004, 0.003, 0, 0, 0.0008, 0.001],
                  [0.05, 0.12, 0.034, 0.031, 0.0045, 0.0035, 0, 0, 0.0008, 0.001],
                  [0.05, 0.134, 0.028, 0.036, 0.005, 0.004, 0.0008, 0.0008, 0, 0],
                  [0.05, 0.134, 0.028, 0.041, 0.006, 0.0045, 0.001, 0.001, 0, 0]])

    Tt = np.transpose(np.array([[-82.46, 32.23, 96.739, 134.98, 152.03, 187.22, 196.34, 30.94, -147, 100.24]]))

    Tc = 273.15 + Tt
    denc = np.transpose(np.array([[10.05, 6.757, 4.999, 3.801, 3.921, 3.247, 3.215, 10.683, 11.099, 10.526]]))

    w = np.transpose(np.array([[0.013, 0.1018, 0.157, 0.183, 0.197, 0.226, 0.252, 0.21, 0.035, 0.105]]))
    Aj = np.array(
        [[0.44369, 1.28438, 0.356306, 0.544979, 0.528629, 0.484011, 0.0705233, 0.504087, 0.0307452, 0.0732828,
          0.00645]])
    Bj = np.array(
        [[0.115449, -0.920731, 1.70871, -0.270896, 0.349261, 0.75413, -0.044448, 1.32245, 0.179433, 0.463492,
          -0.022143]])

    Pd = P * 1e3
    R = 8.3143
    R0 = 0.5193  # 8.3143
    Ro = np.zeros(100000)
    Ro[1] = Pd / R0 / T

    B0i = (Aj[0, 0] + Bj[0, 0] * w) / denc
    A0i = ((Aj[0, 1] + Bj[0, 1] * w) / denc * R * Tc)
    C0i = (Aj[0, 2] + Bj[0, 2] * w) / denc * R * Tc ** 3
    gamai = (Aj[0, 3] + Bj[0, 3] * w) / denc ** 2
    bi = (Aj[0, 4] + Bj[0, 4] * w) / denc ** 2
    ai = (Aj[0, 5] + Bj[0, 5] * w) / denc ** 2 * Tc * R
    alphai = (Aj[0, 6] + Bj[0, 6] * w) / denc ** 3
    ci = (Aj[0, 7] + Bj[0, 7] * w) / denc ** 2 * Tc ** 3 * R
    D0i = (Aj[0, 8] + Bj[0, 8] * w) / denc ** 2 * Tc ** 4 * R
    di = (Aj[0, 9] + Bj[0, 9] * w) / denc ** 2 * Tc ** 2 * R
    E0i = (Aj[0, 10] + Bj[0, 10] * w * np.exp(-3.8 * w)) / denc * Tc ** 5 * R

    A0 = np.sum(np.sum((z * z.T) * (A0i ** 0.5) * (A0i ** 0.5).T * (1 - k)))
    B0 = np.sum(z * B0i)
    C0 = np.sum(np.sum((z * z.T) * ((C0i ** 0.5) * (C0i ** 0.5).T) * (1 - k) ** 3))
    D0 = np.sum(np.sum((z * z.T) * ((D0i ** 0.5) * (D0i ** 0.5).T) * (1 - k) ** 4))
    E0 = np.sum(np.sum((z * z.T) * ((E0i ** 0.5) * (E0i ** 0.5).T) * (1 - k) ** 5))

    a = np.sum(z * ai ** (1 / 3)) ** 3
    b = np.sum(z * bi ** (1 / 3)) ** 3
    c = np.sum(z * ci ** (1 / 3)) ** 3
    d = np.sum(z * di ** (1 / 3)) ** 3
    gama = np.sum(z * gamai ** (1 / 2)) ** 2
    alpha = np.sum(z * alphai ** (1 / 3)) ** 3
    kk = 0
    FRo = np.zeros(100000)
    while abs(Ro[kk + 1] - Ro[kk]) > 1e-6:
        kk += 1
        # print(Ro[kk-1:kk+1])
        FRo[kk - 1:kk + 1] = Ro[kk - 1:kk + 1] * R0 * T + (
                    B0 * R0 * T - A0 - C0 / T ** 2 + D0 / T ** 3 - E0 / T ** 4) * Ro[kk - 1:kk + 1] ** 2 + \
                             (b * R0 * T - a - d / T) * Ro[kk - 1:kk + 1] ** 3 + alpha * (a + d / T) * Ro[
                                                                                                       kk - 1:kk + 1] ** 6 + \
                             c * Ro[kk - 1:kk + 1] ** 3 / T ** 2 * (1 + gama * Ro[kk - 1:kk + 1] ** 2) * np.exp(
            -gama * Ro[kk - 1:kk + 1] ** 2) - Pd

        Ro[kk + 1] = (Ro[kk - 1] * FRo[kk] - Ro[kk] * FRo[kk - 1]) / (FRo[kk] - FRo[kk - 1])

    # 计算其他物理量
    z1 = 1 + ((B0 * R0 * T - A0 - C0 / T ** 2 + D0 / T ** 3 - E0 / T ** 4) * Ro[kk + 1] ** 2 +
              (b * R0 * T - a - d / T) * Ro[kk + 1] ** 3 + alpha * (a + d / T) * Ro[kk + 1] ** 6 +
              c * Ro[kk + 1] ** 3 / T ** 2 * (1 + gama * Ro[kk + 1] ** 2) * np.exp(-gama * Ro[kk + 1] ** 2)) / (
                     Ro[kk] * R0 * T)
    den = Ro[kk]  # kmol/m^3
    Z = z1
    M1 = np.dot(M, z)
    denqti = M1 / 29.16
    r = denqti
    return Z, r, den
