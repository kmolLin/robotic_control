from math import ceil, sqrt, hypot
import matplotlib.pyplot as plt


sampling_time = 0.001
Amax = 2500


def s_shape_interplation(ox, oy, x, y, f):

    length = hypot((x - ox), (y - oy))
    Nss = 0
    Nc = 0
    amax = Amax
    # need to define Jmax
    Jmax = 50000
    Lmin = 2 * f * sqrt(f / Jmax)
    Nstr = ceil((Lmin / 2 / Jmax / sampling_time ** 3) ** (1 / 3))
    Tstr = Nstr * sampling_time

    if length <= Lmin:
        Nstr = ceil((length / 2 / Jmax / sampling_time ** 3) ** (1 / 3))
        Tstr = Nstr * sampling_time
        Jmax = length / (2 * Tstr ** 3)
        amax = Jmax * Tstr
        Vcmd = amax * Tstr
    else:
        Tc = length / f - 2 * Tstr
        Nc = ceil(Tc / sampling_time)
        Tc = Nc * sampling_time
        Vcmd = length / (2 * Tstr + Tc)
        amax = Vcmd / Tstr
        Jmax = amax / Tstr

    step1 = Nstr
    step2 = step1 + Nstr
    step3 = step2 + Nc
    step4 = step3 + Nstr
    step5 = step4 + Nstr

    t0 = 0
    t1 = step1 * sampling_time
    t2 = step2 * sampling_time
    t3 = step3 * sampling_time
    t4 = step4 * sampling_time
    t5 = step5 * sampling_time

    pos1 = (Jmax * (t1 - t0) ** 3) / 6
    pos2 = pos1 + Vcmd * (t2 - t1) - 0.5 * Jmax * (t2 ** 2 * (t2 - t1) - t2 *
                                                   (t2 ** 2 - t1 ** 2) + (t2 ** 3 - t1 ** 3) / 3)
    pos3 = pos2 + Vcmd * (t3 - t2)
    pos4 = pos3 + Vcmd * (t4 - t3) - (Jmax * (t4 - t3) ** 3 / 6)
    pos5 = pos4 + 0.5 * Jmax * (t5 ** 2 * (t5 - t4) - t5 * (t5 ** 2 - t4 ** 2) + ((t5 ** 3 - t4 ** 3) / 3))

    s_tmp = []
    v_tmp = []
    acc_tmp = []
    jerk_tmp = []

    for j in range(step5):
        t = j * sampling_time
        if j < step1:
            jerk = Jmax
            acc = Jmax * (t - t0)
            fed = 0.5 * Jmax * (t - t0) ** 2
            pos = (Jmax * (t-t0) ** 3)/6
        elif step1 <= j < step2:
            jerk = -Jmax
            acc = Jmax * (t2 - t)
            fed = Vcmd - 0.5 * Jmax * (t2 - t) ** 2
            pos = pos1 + Vcmd * (t - t1) - 0.5 * Jmax * (
                        t2 ** 2 * (t - t1) - t2 * (t ** 2 - t1 ** 2) + (t ** 3 - t1 ** 3) / 3)
        elif step2 <= j < step3:
            jerk = 0
            acc = 0
            fed = Vcmd
            pos = pos2 + Vcmd * (t - t2)
        elif step3 <= j < step4:
            jerk = -Jmax
            acc = -Jmax * (t - t3)
            fed = Vcmd - 0.5 * Jmax * (t - t3) ** 2
            pos = pos3 + Vcmd * (t - t3) - (Jmax * (t - t3) ** 3 / 6)
        elif j >= step4:
            jerk = Jmax
            acc = -Jmax * (t5 - t)
            fed = 0.5 * Jmax * (t5 - t) ** 2
            pos = pos4 + 0.5 * Jmax * (t5 ** 2 * (t - t4) - t5 * (t ** 2 - t4 ** 2) + ((t ** 3 - t4 ** 3) / 3))

        else:
            raise ValueError

        s_tmp.append(pos)
        v_tmp.append(fed)
        acc_tmp.append(acc)
        jerk_tmp.append(jerk)

    return s_tmp, v_tmp, acc_tmp, jerk_tmp