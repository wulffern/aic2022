footer: Carsten Wulff 2022
slidenumbers:true
autoscale:true
theme: Plain Jane, 1
text:  Helvetica
header:  Helvetica

## TFE4188 - Lecture 4
# AFE (Analog Front-End)

---
# Housekeeping

---


# How to make state-of-the-art designs


Know what is **known**

Find a good **problem** to solve

Find an **architecture** that could work

Work through all **important** details

If publishing, have some **luck**

**There is no magic in state-of-the-art designs**

<sub><sub>However, a fast brain might get there faster. A slow brain may never reach the end.</sub></sub>

---
## Analog Design Process

[.column]
- Define the problem, what are you trying to solve?
- Find a circuit that can solve the problem (papers, books)
- Find right transistor sizes. What transistors should be weak inversion, strong inversion, or don't care?
- Check operating region of transistors (.op)
- Check key parameters (.dc, .ac, .tran)

[.column]
- Check function. Exercise all inputs. Check all control signals
- Check key parameters in all corners. Check mismatch (Monte-Carlo simulation)
- Do layout, and check it's error free. Run design rule checks (DRC). Check layout versus schematic (LVS)
- Extract parasitics from layout. Resistance, capacitance, and inductance if necessary.
- On extracted parasitic netlist, check key parameters in all corners and mismatch (if possible).
- If everything works, then your done.

*On failure, go back as far as necessary*

---
| Week | Book                 | Monday                                                                       | Project plan             | Exercise |
|------|----------------------|------------------------------------------------------------------------------|--------------------------|----------|
| 2    | CJM 1-6              | Course intro, what I expect you to know, project, analog design fundamentals | Specification            |          |
| 3    | Slides               | ESD and IC Input/Output                                                      | Specification            | x        |
| 4    | CJM 7,8              | Reference and bias                                                           | Specification            |          |
| 5    | CJM 12               | **Analog Front-end**                                                           | M1. Specification review | x        |
| 6    | CJM 11-14            | Switched capacitor circuits                                                  | Design                   |          |
| 7    | JSSC, CJM 18         | State-of-the-art ADCs                                                        | Design                   | x        |
| 8    | Slides               | Low power radio recievers                                                    | Design                   |          |
| 9    | Slides               | Communication standards from circuit perspective                             | M2. Design review        | x        |
| 10   | CJM 7.4, CFAS,+DC/DC | Voltage regulation                                                           | Layout                   |          |
| 11   | CJM 19, CFAS         | Clock generation                                                             | M3. Layout review        | x        |
| 12   | Paper                | Energy sources                                                               | Layout/LPE simulation    |          |
| 13   | Slides               | Chip infrastructure                                                          | Layout/LPE simulation    | x        |
| 14   |                      | Tapeout review                                                               | M4. Tapeout review       |          |
| 15   |                      | Easter                                                                       |                          |          |
| 16   |                      | Easter                                                                       |                          |          |
| 17   |                      | Exam repetition                                                              |                          |          |


---
# Goal for today

Understand **why** we need analog front-end

Introduction to **filter architectures**

---

#[fit] Why

---

![fit](../media/l4_achai.pdf)

---

![fit](../media/l4_radio.pdf)

---

![fit](../media/l4_radio_rfe.pdf)

---

#[fit] You must know application before you make the AFE!

---

#[fit] Filter synthesis

---

#[fit] A combination of 1'st and 2'nd order stages can synthesize any order filter

---

![left fit](../media/l4_first_order.pdf)

[.column]
# First order filter


$$ H(s) =\frac{V_o(s)}{V_i(s)}  = \frac{ k_1 s + k_0 }{s + w_o}$$

---
# Second order filter 

Bi-quadratic is a general purpose second order filter

![left fit](../media/l4_biquad.pdf)


 $$ H(s) = \frac{k_2 s^2 + k_1 s + k_0}{s^2 + \frac{\omega_0}{Q} s +
 \omega_o^2}$$
 
---

Assume that we have a wanted H(s), broken down into second order, and first order sections. 
 
# How do we implement the filter sections?
 

---

#[fit] Gm-C

---


[.column]
![fit](../media/l4_gmc.pdf)

[.column]



$$ V_o = \frac{I_o}{s C} = \frac{\omega_{ti}}{s} V_i $$


$$ \omega_{ti} = \frac{G_M}{C}$$


---

![fit](../media/l4_gmc_diff.pdf)

---

![left fit](../media/l4_cap.pdf)

![right fit](../media/fig_capacitors_vertical.pdf)

---

[.column]
![fit](../media/l4_gmc1st.pdf)


[.column]

 $$ H(s) = \frac{ k_1 s + k_0 }{s + w_o}$$
 
 $$ H(s) = \frac{s \frac{C_x}{C_a + C_x} + \frac{G_m}{C_a + C_x}}{s +
 \frac{G_m}{C_a + C_x}}$$
 
---

![fit](../media/l4_diffpair.pdf)

---



#[fit] Does  $$ i_o = g_m v_i \Rightarrow I_o = G_m V_i $$?  
 
---

#[fit] Active-RC
---

![left fit](../media/l4_activerc.pdf)
 
 $$ H(s) = \frac{A_0}{(1 + s A_o R C)(1 + \frac{s}{w_{ta}})}$$
 
 $$ \Rightarrow \frac{1}{(\frac{1}{A_0} + sRC)(\frac{1}{A_0} + \frac{s}{A_0
 w_{ta}})}$$
 
 $$\Rightarrow{A_0 \rightarrow \infty} \Rightarrow H(s) =  \frac{1}{sRC}$$
 
---

![left fit](../media/l4_radio.pdf)

#[fit] Do we have to separate filter and ADC into two blocks?

---

![left fit](../media/l4_sdloop.pdf)

---

![left fit](../media/l4_sdloop.pdf)

![right fit](../media/l4_sd.pdf)

---

[A 56 mW Continuous-Time Quadrature Cascaded Sigma-Delta Modulator With 77 dB DR in a Near Zero-IF
20 MHz Band](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=4381437)


![inline](../ip/qt_sd.png)![inline](../ip/qt_sd_response.png)

---

# Goal for today

Understand **why** we need analog front-end

- we may need to amplify small signals
- we may need frequency selectivity 
- don't start to design a filter without know application

Introduction to **filter architectures**

- Gm-C: hard to get high linearity, but can be low power

- Active-RC: easy to get high linearity <sub>just use current enough current and
  complex OPAMP </sub>

---


#[fit] Thanks!

---
