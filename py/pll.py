#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

def plot(f,Hs,lbl):
    mag = 20*np.log10(abs(Hs))
    phase = 360*np.angle(Hs)/(2*np.pi)


    zero_crossings = np.where(np.diff(np.signbit(mag)))[0]

    plt.subplot(2,1,1)
    plt.semilogx(f,mag,label=lbl+  " UGBW=%.2g" %f[zero_crossings])
    plt.xlabel("Frequency [Hz]")
    plt.ylabel("Magnitude [dB]")
    plt.grid(True)
    plt.legend()
    plt.subplot(2,1,2)
    plt.semilogx(f,phase,label=lbl)
    plt.xlabel("Frequency [Hz]")
    plt.ylabel("Phase [Degrees]")
    plt.grid(True)
    plt.legend()



#- Loop Model
f = np.logspace(-4,10)

s = 1j*2*np.pi*f
R = 10e3
C1 = 1e-12
C2 = 300e-15

Kvco = 2*np.pi*1.88e9
Kpd = 100e-9/(2*np.pi)

KlpHlp = 1/np.multiply((C1 + C2),s)* \
    (1 + np.multiply(s,(R*C1)))/(1 + np.multiply(s,R*(C1*C2)/(C1 + C2)))
N = 128

Ls = np.divide(Kvco*Kpd*KlpHlp, N*s)
Cs = np.divide(1,1 + Ls)

#- Plot stuff
plot(f,Ls,"Loop ")
plot(f,Cs,"Closed Loop")

plt.savefig("pll.pdf")
plt.show()
