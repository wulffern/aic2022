footer: Carsten Wulff 2022
slidenumbers:true
autoscale:true
theme: Plain Jane, 1
text:  Helvetica
header:  Helvetica
    
## TFE4188 - Lecture 1 
# Advanced Integrated Circuits Introduction


## [Source](https://github.com/wulffern/aic2022/blob/main/lectures/l1_intro.md)

---

#[fit] Who

---

# Carsten Wulff [carstenw@ntnu.no](carstenw@ntnu.no)

![inline](../media/timeline_black.png)

---

# Teaching assistants

- Fredrik Esp Feyling
- Simen Fossum Morken

---

#[fit] Why

---

#[fit] I want you to learn the necessary skills to make your own ICs

---

[.column]


![inline](../media/analog_world.png)

<sub> [https://circuitcellar.com/insights/tech-the-future/kinget-the-world-is-analog/](https://circuitcellar.com/insights/tech-the-future/kinget-the-world-is-analog/)</sub>


[.column]

![inline](../media/dig_des.png)

---

[.column]
![inline](../media/IC.png)

[.column]

## I want us to tapeout an IC

<sub>But I'm not sure we'll make it this year </sub>

We need:

- Infrastructure (bias, supply, reset, clocks)
- IO (input, output, ESD)
- Control interface
- Your design

---

- _Project flow support_: **Confluence**, JIRA, risk management (DFMEA), failure analysis (8D)
- _Language_: **English**, **Writing English (Latex, Word, Email)**
- _Psychology_: Personalities, convincing people, presentations (Powerpoint, Deckset), **stress management (what makes your brain turn off?)**
- _DevOps_: **Linux**, bulid systems (CMake, make, ninja), continuous integration (bamboo, jenkins), **version control (git)**, containers (docker), container orchestration (swarm, kubernetes)
- _Programming_: Python, Go, C, C++, Matlab <sub>Since 1999 I’ve programmed in Python, Go, Visual BASIC, PHP, Ruby, Perl, C#, SKILL, Ocean, Verilog-A, C++, BASH, AWK, VHDL, SPICE, MATLAB, ASP, Java, C, SystemC, Verilog, and probably a few I’ve forgotten.</sub>
- _Firmware_: signal processing, algorithms
- _Infrastructure_: **Power management**, **reset**, **bias**, **clocks**
- _Domains_: CPUs, peripherals, memories, bus systems
- _Sub-systems_: **Radio’s**, **analog-to-digital converters**, **comparators**
- _Blocks_: **Analog Radio**, Digital radio baseband
- _Modules_: Transmitter, **receiver**, de-modulator, timing recovery, state machines
- _Designs_: **Opamps**, **amplifiers**,  **current-mirrors**, adders, random access memory blocks, standard cells
- _Tools_: **schematic**, **layout**, **parasitic extraction**, synthesis, place-and-route, **simulation**,  (System)Verilog, **netlist** 
- _Physics_: transistor, pn junctions, quantum mechanics

---
[.background-color: #000000]
[.text: #FFFFFF]

> Find a problem that you really want to solve, and learn programming to solve it. There is absolutely no point in saying "I want to learn programming", then sit down with a book to read about programming, and expect that you will learn programming that way. It will not happen. The only way to learn programming is to do it, a lot. 
-- Carsten Wulff 


```perl
s/programming/analog design/ig
```

---

### Zen of IC design (stolen from Zen of Python)

[.column]
- Beautiful is better than ugly.
- Explicit is better than implicit.
- Simple is better than complex.
- Complex is better than complicated.
- Readability counts (especially schematics).
- Special cases aren't special enough to break the rules.
- Although practicality beats purity.

[.column]

- In the face of ambiguity, refuse the temptation to guess.
- There should be one __and preferably only one__ obvious way to do it.
- Now is better than never.
- Although never is often better than *right* now.
- If the implementation is hard to explain, it's a bad idea.
- If the implementation is easy to explain, it may be a good idea.

---


#[fit] Course

---

[.column]

# Plan

Lecture Monday's at 10:15 - 12:00 (for now, it's digital)

First Hour: Monolog from me (although please ask questions)

Second Hour: Discuss article and discuss project

[Description](https://www.ntnu.no/studier/emner/TFE4188#tab=omEmnet)

[Time schedule](https://tp.uio.no/ntnu/timeplan/?id=TFE4188&sem=22v&sort=form&type=course)

[.column]





---

![inline](../media/cjm.png)![inline](../media/jssc.png)![inline](../media/cfas.png)

+ slides and videos

---

| Week | Book          | Monday                                           | Project plan                          |
|------|---------------|--------------------------------------------------|---------------------------------------|
| 2    | CJM 1-6       | Course intro, what I expect you to know, project | Specification                         |
| 3    | Slides        | ESD and IC Input/Output                                              | Specification                         |
| 4    | CJM 7,8       | Reference and bias                               | M1. Specification review              |
| 5    | CJM 12        | Analog Frontend                                  | Design                                |
| 6    | CJM 11-14     | Switched capacitor circuits                      | Design                                |
| 7    | JSSC, CJM 18  | State-of-the-art ADCs                            | Design                                |
| 8    | Slides        | Low power radio recievers                        | M2. Design review                     |
| 9    | Slides        | Communication standards from circuit perspective | Layout                                |
| 10   | CJM 7.4, CFAS,+DC/DC | Voltage regulation                               | Layout                                |
| 11   | CJM 19, CFAS  | Clock generation                                 | M3. Layout DRC/LVS clean              |
| 12   | Paper         | Energy sources                                   | Layout Parasitic Extracted simulation |
| 13   | Slides        | Chip infrastructure                              | Layout Parasitic Extracted simulation |
| 14   |               | Tapeout review                                   | M4. Tapeout review                    |
| 15   |               | Easter                                           |                                       |
| 16   |               | Easter                                           |                                       |
| 17   |               | Exam repetition                                  |                                       |

---

#[fit] Exam

---

- May/June 2022?
- 4 hours
- D aids code - No handwritten or printed aids allowed. Preapproved calculator, in accordance to the exam regulations,
  allowed. Digital exam
- 55% of the final grade
- A - F grade (F = Fail)

---

#[fit] Time to take responsiblity for your own future 

---

#[fit] Exercises

---

- Exercises on blackboard now
- Solutions on blackboard after the deadline
- Two options:
  - Don't do the exercises, don't get feedback
  - Do the exercises, hand them in within deadline, get feedback
- The TA's will only support the exercises in the marked weeks

---

| Date       | Week | Topic         |
|------------|------|---------------|
| 2022-01-21 | 3    | Transistors   |
| 2022-02-04 | 5    | Bandgap       |
| 2022-02-17 | 7    | Noise         |
| 2022-03-04 | 9    | Discrete time |
| 2022-03-18 | 11   | PLL           |
| 2022-04-01 | 13   | LDO           |

---

#[fit] Project

---

45 % of final grade

Deadline: 22 of April 

Strict deadline, if you hand in 23 of April at 00:00:01, then it's a fail.

---

### [SUN (2022)](https://www.ntnu.no/wiki/pages/viewpage.action?pageId=209453241) <sub> "It's not you, it's me, I don't like you." – Ayrun Sun, Farscape</sub>

[.column]



Design a circuit that senses something from the real world and provides a digital value.

![inline](../media/temp_sch.png)

[.column]

![inline](../media/temp.png)

---

#[fit] Project Report $$\Rightarrow$$ Paper

#[fit] [A Compiled 9-bit 20-MS/s 3.5-fJ/conv.step SAR ADC in 28-nm FDSOI for Bluetooth Low Energy Receivers](https://ieeexplore.ieee.org/document/7906479)

[IEEE journal template](https://ctan.org/pkg/ieeetran?lang=en), [Example](https://github.com/wulffern/jssc2017)

Must use `\documentclass[journal,11pt,letterpaper]{IEEEtran}`

Strict page limit for report, max 8 pages (excluding bio and references). More than 8 pages $$\Rightarrow$$ Fail 

---

#[fit] Software

Linux servers: aurora, jupiter, venus

If you don't have access, contact me

[Getting Started](https://www.ntnu.no/wiki/display/tfe4487/Getting+started)

---

# Lower your expectations on EDA software

---

# Expect that you will spend at least $$2\pi$$ times more time than planned *(mostly due to software issues)* 

---

#[fit] Questions 

---

## Do
- google
- ask a someone in your class
- use the "øvingstime and labratorieøvelse" to talk to teaching assistants. Don't ask about future exercises
- ask in the teams channels
- come to the office (B311) on Mondays

---

#[fit] Thanks!


