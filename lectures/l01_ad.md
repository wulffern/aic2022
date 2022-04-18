footer: Carsten Wulff 2022
slidenumbers:true
autoscale:true
theme: Plain Jane, 1
text:  Helvetica
header:  Helvetica

<!--pan_title:# Analog Design Fundamentals -->

<!--pan_skip: -->
## TFE4188 - Lecture 1
# Analog design fundamentals

---
<!--pan_skip: -->
| Week | Book          | Monday                                           | Project plan                          |
|------|---------------|--------------------------------------------------|---------------------------------------|
| 2    | CJM 1-6       | Course intro, what I expect you to know, project, analog design fundamentals | Specification                         |
| 3    | Slides        | ESD and IC Input/Output                                              | Specification                         |
| 4    | CJM 7,8       | Reference and bias                               | M1. Specification review              |
| 5    | CJM 12        | Analog Front-end                                  | Design                                |
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
<!--pan_skip: -->

Questions from previous lectures?

NDA

---

<!--pan_skip: -->

# Goal for today

Choosing transistor sizes is **complicated**

How to make **state-of-the-art** designs

**Recommendations** for transistor sizes

---

<!--


#[fit] Technology

---

| Parameter   | Description           | Notes                                              |
|-------------|-----------------------|----------------------------------------------------|
| Technology  | GF130BCDLite          | [https://europractice-ic.com/schedules-prices-2022/](https://europractice-ic.com/schedules-prices-2022/) |
| Metal stack | 1p7m\_2tm\_30k\_dp\_alrdl | 1P7M TM30K, Dual Passivation                       |
| Area        | 1.75 mm x 1.75 mm.    | Estimated cost 5625 EUR                            |
| Package     | 6 x 6 mm QFN48        |                                                    |

---
# Corners

| Corners     | Parameter | Min  | Typ | Max  |
|-------------|-----------|------|-----|------|
| Core supply | vdda      | 1.35 | 1.5 | 1.65 |
| IO supply   | vdde      | 2.4  | 3.0 | 3.6  |
| Temperature | t_temp    | -40  | 27  | 125  |

```
tech_gf130n/spectre/corners.csv
$PROJECT/lib/spectre/corners.csv
```
---

![original 80%](../media/corners.png)

---
-->

<!--pan_skip: -->

#[fit] Complicated

---

## Analog Design Process

[.column]
- Define the problem, what are you trying to solve?
- Find a circuit that can solve the problem (papers, books)
- **Find right transistor sizes. What transistors should be weak inversion, strong inversion, or don't care?**
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

Assume active ($$V_{ds} > V_{eff}$$ in strong inversion, or $$V_{ds} > 3 V_T$$ in weak inversion) <sub>For diode connected transistors, this is always true</sub>

Weak inversion 

 $$ I_{D} = I_{D0} \frac{W}{L} e^{V_eff / n V_T} $$, $$V_{eff} \propto \ln{I_D} $$

Strong inversion 

 $$ I_{D} = \frac{1}{2} \mu_n C_{ox} \frac{W}{L} V_{eff}^2$$, $$V_{eff} \propto \sqrt{I_D} $$

**Operating region for a diode connected transistor only depends on the current**

![right fit](../media/trop.png)

---



[.column]
![inline](../media/fig_pmos.pdf) ![inline](../media/fig_nmos.pdf)

[.column]

# Flavors

<!--pan_doc:

Mosfets come in flavors, we can separate into PMOS and NMOS. 

-->

1.5 V MOS (standard Vt, native Vt)

| Parameter | Min  | Max | Unit |
|-----------|------|-----|------|
| L         | 0.13 | 100 | um   |
| W         | 0.15 | 50  | um   |

Assume 5n quantization.  Permutations per transistor (P)
 $$P = 2 \times 19974 \times 9970 = 398 \text{ M} $$ 

Typical ADC ~ 20 k transistors 
 $$ P_{ADC} = 20 \text{ k} \times 2 \times 398 \text{ M} = 16 \text{ P}$$

**Too large solution space for exhaustive search**

---
# Picking transistor size

Not possible with exhaustive search

Simplify as much as possible

Use brain

![left fit](../media/aicdn.pdf)

---

#[fit] State-of-the-art

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

# My only <sub><sub>published</sub></sub> state-of-the-art design

![right fit](../media/ALGIC001_SAR9B_CV.pdf)


---

#[fit] Trigger

<!--pan_doc:

Back in November 2009 I was listening to Lanny Lewyn talk about regular layout at NorChip in Trondheim and idea struck 
'I'm pretty sure I'm able to write a script to generate this layout'. In 2010 I started writing the script. 

-->

![inline fit](../media/acdncmos.png)

![right fit](../media/trigger.png)

---
#[fit] Problem


<!--pan_doc:

Although I knew what I wanted to do, generate layout, I needed a problem to solve. It was not enough for me to make something to generate layout. I wanted the generated layout,
and the generated analog blocks, to be better than anything out there. It should be state of the art, even though it was generated, or compiled. 

I don't remember how I choose the problem, but I did see the overview of ADCs and noticed the lack of high efficiency, medium speed ADCs. I also knew from my PhD that 
Walden figure of merit favors low-resolution ADCs. 

-->

![right fit](../media/efficient_adcs.png)

---
#[fit] Architecture

<!--pan_doc:

In 2009 there was really only one type of ADC that made sense, the successive-approximation ADC. Using finger capacitors had become common, and 
it was demonstrated that it was OK to use really small capacitors, down to atto farads. 

The thermal noise power of an ADC is in part determined by the capacitor size, given by 

$$ P_{noise} = \frac{k T}{C} $$

Especially in nano-scale, and we were targeting 28 nm FDSOI, it was now possible to design both atto farad unit caps, and approach the thermal limit for 8-bit ADCs. 

I was not sure whether it would be 8-bit, 9-bit or 10-bit that would be the most power optimum for 28 nm FDSOI, so I wanted to make multiple versions.

-->

![inline 90%](../media/draxelmayr.gif)

![right fit](../media/draxl1.png)

---
<!--
![original ](../media/draxl_arch.pdf)

---
-->

#[fit] Question


Designing a SAR ADC from scratch takes times!

Could I design  "once and for all" a process independent SAR architecture that is tolerant towards supply, temperature, process, mismatch and process technology?


<!--pan_doc:

Could I generate multiple versions, one 8-bit, 9-bit and 10-bit? 

-->

---

#[fit] Plan 

9-bit SAR ADC with 28 nm FDSOI transistors

9-bit SAR ADC with IO voltage (180 nm) FDSOI transistors



---

![inline](../media/anadesign.pdf)

---

[.column]

# How to make multiple SAR ADCs with limited time?




Spend 50% of time for 6 months to **develop** a tool to make SAR ADCs

Spend 50% of time for 6 months to **make** the SAR ADCs

<!--pan_doc: 
At the time, my language of choice was Perl, so the first version of the script was a 16 k line Perl program that I named cnano.

Cnano was started while I worked at Nordic, and I was able to bring the code with me to NTNU when I started my post doc. 

In the end, cnano turned out out be slow, and the problem of variable type (numbers could be integer or float, but in a controlled manner) was becoming an issue.

As such, I started writing Custom IC Creator abbreviated cic (which actually meant Carstens IC creator ;-) )  in 2014. cic is written in C++, and was developed to replace cnano. After 2017, I stopped maintaining cnano. 

Below is an exceprt of the cic code. You can download cic from [https://github.com/wulffern/ciccreator](https://github.com/wulffern/ciccreator)

-->

[.column]

```cpp
#include "core/layoutcell.h"

typedef QMap<QString,QList<cIcSpice::SubcktInstance*>>  SARgroup;

namespace cIcCells{
    
    class SAR : public cIcCore::LayoutCell
    {
        Q_OBJECT

    public:    
        virtual void place();

        virtual void route();
        
        int getCellWidth(SARgroup groups,QString group);
        
        cIcCore::Instance* placeAlternateMirror(SARgroup groups,QString group, 
            int i, int x ,int y, int xoffset);
        
        int addSarRouting(int y,int msw,int mw);

        static bool sortGraph(cIcCore::Graph* a, cIcCore:: Graph *b);
    
    private:
        Rect* sarn;
        Rect* sarp;
    };       
}

```

---

<!--pan_doc:

I wanted the input data to cnano/cic to be human readable, easy to parse and independent of technology. I also wanted the input data to be independent of 
platform (linux,mac,windows) and CAD vendor (Cadence, Synopsys )

-->


![inline](../media/cnano.pdf)

16 k Perl lines. Ported to C++ for speed $$\Rightarrow$$ [ciccreator](https://github.com/wulffern/ciccreator)

---

![inline](../media/transistor.pdf)

---

![inline](../media/inverter.pdf)

---

![inline](../media/adcs.pdf)

---

[A Compiled 9-bit 20-MS/s 3.5-fJ/conv.step SAR ADC in 28-nm FDSOI for Bluetooth Low Energy Receivers](https://ieeexplore.ieee.org/document/7906479)

![inline](../media/wulff_fig_table.pdf)

---

![inline](../media/harald.pdf)![inline](../media/harald_layout.pdf)

---

#[fit] Result

![right fit](../media/our_work.png)

---

# SUN\_SAR9B\_GF130N
```
├── SAR9B_CV.json
├── SAR9B_CV.spi
├── capacitor.json
├── dmos_gf130nm_core.json
└── gf_130bcdlite.tech
```

9-bit is not the energy optimum for GF130N. The power consumption of the digital is too high. The energy optimum is more like 13-bit, however, the CDAC matching limits performance to about 10/11-bit

$$ \log2[(W_{130n} L_{130n})/(W_{28n} L_{28n} )] = \log2[(0.95\times0.14)/(0.258 \times 0.03)]=4\text{-bit extra}$$

![right fit](../media/GF130N_vs_28N.pdf)

---

#[fit] Recommendations 

---
#[fit] [https://github.com/wulffern/aicex](https://github.com/wulffern/aicex)

![right fit](../media/aicex.png)

---
Typical

![inline](../media/idgm_lvt_SchGtMttRtCtTtVtDtBt.pdf)

---
Temperature

![inline](../media/idgm_lvt_SchGtMttRlClBsDsTtThTlVt.pdf)

---
Process

![inline](../media/idgm_lvt_SchGtMttMssMffRlClBsDsTtVt.pdf)

---
Process and temperature

![inline](../media/idgm_lvt_SchGtMttMssMffRlClBsDsTtThTlVt.pdf)

---

#[fit] What $$gm/I_d$$ would you pick?

![right 150%](../media/idgm_lvt_SchGtMttMssMffRlClBsDsTtThTlVt.pdf)

---
Temperature and ```BINN 0 N1_0 i=i(VREF) tc1={0.3/100}```

![inline](../media/idgm_lvt_temp_SchGtMttRlClBsDsTtThTlVt.pdf)

---
Process, Temperature and ```BINN 0 N1_0 i=i(VREF) tc1={0.3/100}```

![inline](../media/idgm_lvt_temp_SchGtMttMssMffRlClBsDsTtThTlVt.pdf)

---

![left fit](../media/idgm_lvt_SchGtMttMssMffRlClBsDsTtThTlVt.pdf)

![right fit](../media/idgm_lvt_temp_SchGtMttMssMffRlClBsDsTtThTlVt.pdf)

---

![inline fit](../media/transistors.pdf)

---
# SUN\_TR\_GF130N
```
├── SUN_TR.json
├── components.json
├── components.spi
├── dig.json
├── dig.spi
├── dmos_gf130nm_core.json
├── gf_130bcdlite.tech
├── tr.json
└── tr.spi
```
---

## GMID = 15

| Param     | Vgs (Min) | Vgs (Max) | Id (Min) | Id (Max) | Gmro (Min) | Gmro (Max) |
|:----------|:----------|:----------|:---------|:---------|:-----------|:-----------|
| NCHDL     | 455.30m   | 734.70m   | 4.14u    | 7.57u    | 20.24      | 23.81      |
| NCHDLA    | 446.20m   | 723.90m   | 8.68u    | 15.61u   | 21.06      | 24.79      |
| NCHDLCM   | 465.40m   | 765.60m   | 422.40n  | 999n     | 163        | 272.90     |
| NCHDLCM2  | 465.40m   | 765.60m   | 844.70n  | 2u       | 163        | 272.90     |
| CNCHDLCM2 | 465.60m   | 765.90m   | 772.60n  | 1.83u    | 163        | 272.90     |

| Param     | Vgs (Min) | Vgs (Max) | Id (Min) | Id (Max) | Gmro (Min) | Gmro (Max) |
|:----------|:----------|:----------|:---------|:---------|:-----------|:-----------|
| PCHDL     | 387.10m   | 739.60m   | 1.01u    | 3.53u    | 27.26      | 28.64      |
| PCHDLA    | 385.70m   | 738.20m   | 5.71u    | 19.83u   | 27.32      | 28.69      |
| PCHDLCM   | 374.30m   | 742.90m   | 383.60n  | 1.53u    | 50.22      | 54.14      |
| PCHDLCM2  | 374.30m   | 742.90m   | 767.10n  | 3.06u    | 50.22      | 54.14      |
| CPCHDLCM2 | 372.40m   | 747.80m   | 620.10n  | 2.47u    | 50.22      | 54.14      |

---

## GMID = 10

| Param     | Vgs (Min) | Vgs (Max) | Id (Min) | Id (Max) | Gmro (Min) | Gmro (Max) |
|:----------|:----------|:----------|:---------|:---------|:-----------|:-----------|
| NCHDL     | 555.90m   | 848.30m   | 15.52u   | 29.15u   | 19.37      | 23.10      |
| NCHDLA    | 547.20m   | 839m      | 33.38u   | 61.50u   | 20.06      | 24.21      |
| NCHDLCM   | 582.50m   | 872.80m   | 1.75u    | 3.97u    | 134.30     | 196.90     |
| NCHDLCM2  | 582.50m   | 872.80m   | 3.50u    | 7.93u    | 134.30     | 196.90     |
| CNCHDLCM2 | 582.80m   | 873.20m   | 3.20u    | 7.27u    | 134.30     | 196.90     |

| Param     | Vgs (Min) | Vgs (Max) | Id (Min) | Id (Max) | Gmro (Min) | Gmro (Max) |
|:----------|:----------|:----------|:---------|:---------|:-----------|:-----------|
| PCHDL     | 503.40m   | 827.30m   | 4.90u    | 9.83u    | 24.16      | 26.74      |
| PCHDLA    | 501.80m   | 825.60m   | 27.53u   | 55.21u   | 24.24      | 26.81      |
| PCHDLCM   | 502.60m   | 837.60m   | 2.10u    | 4.55u    | 44.65      | 47.78      |
| PCHDLCM2  | 502.60m   | 837.60m   | 4.20u    | 9.10u    | 44.65      | 47.78      |
| CPCHDLCM2 | 500.40m   | 843m      | 3.28u    | 7.26u    | 44.65      | 47.78      |


---


## Use a few transistors that you know well <sub>know all **important** details </sub>

## Use M factor to scale current and $$gm$$  <sub>bus notation M1<9:0> on instance name in cadence</sub>

## Pick the right bias current for your circuit <sub>constant, constant gm, proportional to temperature</sub>

---

#[fit] Thanks!

