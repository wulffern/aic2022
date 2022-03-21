footer: Carsten Wulff 2021
slidenumbers:true
autoscale:true
theme:Plain Jane,1

# TFE4188 - Lecture 10
# Clock generation

---
# Housekeeping

Testbenches

Config views

SAR verilog model


---


| Week | Book                 | Monday                                                                       | Project plan             | Exercise |
|------|----------------------|------------------------------------------------------------------------------|--------------------------|----------|
| 2    | CJM 1-6              | Course intro, what I expect you to know, project, analog design fundamentals | Specification            |          |
| 3    | Slides               | ESD and IC Input/Output                                                      | Specification            | x        |
| 4    | CJM 7,8              | Reference and bias                                                           | Specification            |          |
| 5    | CJM 12               | Analog Front-end                                                             | M1. Specification review | x        |
| 6    | CJM 11-14            | Switched capacitor circuits                                                  | Design                   |          |
| 7    | JSSC, CJM 18         | State-of-the-art ADCs                                                        | Design                   | x        |
| 8    | Slides               | Low power radio recievers                                                    | Design                   |          |
| 9    | Slides               | Communication standards from circuit perspective                             | M2. Design review        | x        |
| 10   | CJM 7.4, CFAS,+DC/DC | Voltage regulation                                                           | Layout                   |          |
| 11   | CJM 19, CFAS         | **Clock generation**                                                         | Layout                   | x        |
| 12   | Paper                | Energy sources                                                               | Layout/LPE simulation    |          |
| 13   | Slides               | Chip infrastructure                                                          | Layout/LPE simulation    | x        |
| 14   |                      | Tapeout review                                                               | M4. Tapeout review       |          |
| 15   |                      | Easter                                                                       |                          |          |
| 16   |                      | Easter                                                                       |                          |          |
| 17   |                      | Exam repetition                                                              |                          |          |

---

# Goal

**Why** do we need to generate clocks 

Introduction to **PLLs**

Introduction to **Crystal Oscillators**

Introduction to **Relaxation-oscillators**

---

#[fit] Why

---

![fit](../media/l10_dk.pdf)

---

![fit](../media/l10_clockic.pdf)

---

![fit](../media/logic.pdf)

---

#[fit] PLL

---

![fit](../media/l10_fb.pdf)

---

![fit](../media/l10_freq_fb.pdf)

---

![fit](../media/l10_sch_top.pdf)

---

![fit](../media/l10_sch_rosc.pdf)

---

![fit](../media/l10_sch_divider.pdf)

---

![fit](../media/l10_sch_lpf.pdf)

---

![fit](../media/l10_sch_pfd.pdf)

---

# $$ f_{CK} = 128 \times 8\text{ MHz} = 1024\text{ MHz} $$ 

---

![fit](../media/l10_pll_sim.pdf)

---

#[fit]PLLs need calculation!

# \#nocowboydesign

---

# $$ \phi(t) = 2 \pi \int_0^t f(t) dt$$

---


![fit](../media/l10_pll_sm.pdf)

---

--
--
--



$$ \frac{\phi_d}{\phi_{in}} = \frac{1}{1 + L(s)}$$ 


$$ L(s) = \frac{ K_{osc} K_{pd} K_{lp} H_{lp}(s) }{N s} $$


![left fit](../media/l10_pll_sm.pdf)

---
--
--
--

# $$K_{osc} = 2 \pi\frac{ df}{dV_{cntl}}$$

TB\_SUN\_PLL\_KVCO 
$$K_{osc} =  2 \pi\times1.88 \text{ G rad/s}$$

![right fit](../media/l10_pll_kvco.pdf)

---

[.column]

--
--
--

# $$ K_{pd} = \frac{I_{cp}}{2 \pi} $$

[.column]

--
--
--

## TB\_SUN\_PLL\_ICP


$$ K_{pd} = \frac{100\text{ nA}}{2 \pi}$$

---

 $$ K_{lp}H_{lp}(s)= K_{lp}\left(\frac{1}{s} + \frac{1}{\omega_z}\right) $$

 $$ K_{lp}H_{lp}(s) = \frac{1}{s(C_1 + C_2)}\frac{1 + s R C_1}{1 +
sR\frac{C_1C_2}{C_1 + C_2}}$$


SUN\_PLL\_LPF
 $$ R = 10 k \Omega$$ 
 $$ C_1 = 1 p F $$
 $$ C_2 = 300 f F $$


![right fit](../media/l10_lpf.pdf)

---
[.column]

--
--
--
--

$$ L(s) = \frac{ K_{osc} K_{pd} K_{lp} H_{lp}(s) }{N s} $$

[.column]


[aic2020/py/pll.py](https://github.com/wulffern/aic2022/blob/main/py/pll.py)

```python
#- Loop Model
f = np.logspace(-4,10)

s = 1j*2*np.pi*f

Kvco = 2*np.pi*1.88e9

Kpd = 100e-9/(2*np.pi)

R = 10e3
C1 = 1e-12
C2 = 300e-15

KlpHlp = 1/np.multiply((C1 + C2),s)* \
 (1 + np.multiply(s,(R*C1)))/ \
 (1 + np.multiply(s,R*(C1*C2)/(C1 + C2)))

N = 128

Ls = np.divide(Kvco*Kpd*KlpHlp, N*s)
Cs = np.divide(1,1 + Ls)

```
---

![fit](../media/l10_py_pll.pdf)

---

#[fit] See book chapter 19.2.3 for how to fix it

---

![ fit](../media/l10_py_pll_fix.pdf)

---

![fit](../media/l10_pll_fixed.pdf)

---

#[fit] JSSC PLLs

---

![fit](../ip/l10_jssc_pll1.pdf)

---

![fit](../ip/l10_jssc_pll1_1.pdf)

---

![fit](../ip/l10_jssc_pll2_0.pdf)

---

![fit](../ip/l10_jssc_pll2_1.pdf)

---

![fit](../ip/l10_jssc_pll3_0.pdf)

---

![fit](../ip/l10_jssc_pll3_1.pdf)

---

![fit](../ip/l10_jssc_pll3_2.pdf)

---

![fit](../ip/l10_jssc_pll3_3.pdf)

---


#[fit] XO

---

![fit](../ip/l10_jssc_xo1_0.pdf)

---

![fit](../ip/l10_jssc_xo1_1.pdf)

---

![fit](../ip/l10_jssc_xo1_2.pdf)

---

![fit](../ip/l10_jssc_xo1_3.pdf)

---

#[fit] RC

---

![fit](../ip/l10_jssc_rcsc.pdf)

---

![fit](../ip/l10_jssc_rc3_0.pdf)

---

![fit](../ip/l10_jssc_rc3_1.pdf)

---

![fit](../ip/l10_jssc_rc3_2.pdf)

---

![left fit](../ip/l10_jssc_rc3_2.pdf)

![right fit](../ip/l10_jssc_rc3_3.pdf)

---

# Additional material

[The Crystal Oscillator - A Circuit for All Seasons](https://ieeexplore.ieee.org/document/7954123)   

[The Delay-Locked Loop - A Circuit for All Seasons ](https://ieeexplore.ieee.org/document/8447468) 

[The Ring Oscillator - A Circuit for All Seasons ](https://ieeexplore.ieee.org/document/8901474)       

[A Single-Trim Frequency Reference Achieving ±120 ppm Accuracy From −50 ◦C to 170 ◦C](https://ieeexplore.ieee.org/document/9477289) 

---



#[fit] Thanks!


