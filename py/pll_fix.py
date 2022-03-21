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
    plt.semilogx(f,phase,label=lbl+ "PhUGBW=%.2g"%phase[zero_crossings])
    plt.xlabel("Frequency [Hz]")
    plt.ylabel("Phase [Degrees]")
    plt.grid(True)
    plt.legend()

# w3db = 2pi * 800e3
# wpll = 2pi * 0.5*800e3
# wpll = sqrt(Kpd*Klp*Kosc/N)

#- Loop Model
f = np.logspace(-4,10)

s = 1j*2*np.pi*f


Kvco = 2*np.pi*1.88e9
Kpd = 100e-9/(2*np.pi)

R = 550e3
C1 = 10e-12
C2 = 1e-12

Klp = 1/C1
N = 128

wpll = np.sqrt(Kpd*Klp*Kvco/N)
wz = 1/(R*C1)
w3db = wpll**2/wz
print(" wpll=%.2g"%wpll)
print(" w3db=%.2g"%w3db)

KlpHlp = 1/np.multiply((C1 + C2),s)* \
    (1 + np.multiply(s,(R*C1)))/(1 + np.multiply(s,R*(C1*C2)/(C1 + C2)))



Ls = np.divide(Kvco*Kpd*KlpHlp, N*s)
Cs = np.divide(1,1 + Ls)

#- Plot stuff
plot(f,Ls,"Loop ")
plot(f,Cs,"Closed Loop")

plt.savefig("pll.pdf")
plt.show()
