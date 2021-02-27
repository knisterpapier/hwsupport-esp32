import numpy
from pyo import *
import time


if __name__ == '__main__':

 

    s = Server().boot()
    s.start()

    a = Input(chnl=0)
    d = WGVerb(a, feedback=[.90,.75], cutoff=8000, bal=.25, mul=.3).out()


    s.gui(locals())
    s.stop()

    # s = Server().boot()
    # s.start()
    
    # f = Adsr(attack=.01, decay=.2, sustain=.5, release=.1, dur=4, mul=.5)
    # a = Sine(mul=f).out()

    # f.play()
    # time.sleep(5)
    
    # f = Adsr(attack=.10, decay=.8, sustain=.2, release=.5, dur=4, mul=.5)
    # a = Sine(mul=f).out()
    # a.freq = 500
    # f.play()

    # s.gui(locals())
    # s.stop()
