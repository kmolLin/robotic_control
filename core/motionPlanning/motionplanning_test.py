# -*- coding: utf-8 -*-

from trapezoid import graph_chart
import matplotlib.pyplot as plt

if __name__ == '__main__':

    i = 0.
    sx_plot = []
    sy_plot = []
    ts = None
    with open("line.nc", "r") as f:
        text = f.read()
    sgo = []
    vgo = []
    ago = []
    jgo = []
    print(text)
    for tp in graph_chart(text):
        for s, v, a, j in tp.iter(
                tp.s,
                tp.v,
                tp.a,
                tp.j
        ):
            sgo.append((i, s))
            vgo.append((i, v))
            ago.append((i, a))
            jgo.append((i, j))
            i += tp.t_s
            if ts is None:
                ts = tp.t_s

    plt.plot([s[0] for s in sgo], [s[1] for s in sgo])
    plt.show()
