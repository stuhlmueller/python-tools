#!/usr/bin/python

import math, datetime
import rpy2.robjects.lib.ggplot2 as ggplot2
import rpy2.robjects as ro
from rpy2.robjects.packages import importr
base = importr('base')
grdevices = importr('grDevices')


__all__ = ['line_plot', 'stacked_area_plot', 'plot', 'make_dataframe']


def make_dataframe(data, xid, yid, factorid):
    ns = []
    steps = []
    runtimes = []
    for (n, v1) in data.items():
        for (step, runtime) in v1.items():
            ns.append(n)
            steps.append(step)
            runtimes.append(runtime)
    df = ro.DataFrame({xid : ro.IntVector(ns),
                       factorid : ro.StrVector(steps),
                       yid : ro.IntVector(runtimes)})
    return df


def plot(data, filename, title, ggplotter, xid="N", yid="RunTime", factorid="Step"):
    df = make_dataframe(data, xid, yid, factorid)
    grdevices.pdf(file=filename, width=10, height=6)
    gp = ggplot2.ggplot(df)
    pp = gp + \
        ggplot2.aes_string(x=xid, y=yid) + \
        ggplot2.aes_string(size=.5) + \
        ggplotter() + \
        ggplot2.aes_string(colour='factor(%s)' % factorid) + \
        ggplot2.aes_string(fill='factor(%s)' % factorid) + \
        ggplot2.opts(title=title) + \
        ggplot2.scale_fill_brewer(palette="Set2") + \
        ggplot2.scale_colour_brewer(palette="Set2")
    pp.plot()
    grdevices.dev_off()

    
def stacked_area_plot(data, filename, title, **kwargs):
    return plot(data, filename, title, ggplot2.geom_area, **kwargs)


def line_plot(data, filename, title, **kwargs):
    return plot(data, filename, title, ggplot2.geom_line, **kwargs)
