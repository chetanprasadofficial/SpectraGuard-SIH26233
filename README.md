# SpectraGuard
**Inline Microbial Contamination Detection Using Hyperspectral Edge Sensors**

© 2026 Team CROWNX. Submitted for Smart India Hackathon 2026, Problem Statement **26233**. All rights reserved.

---

## Problem Statement

| Field | Detail |
|---|---|
| PS ID | 26233 |
| PS Title | Inline Microbial Contamination Detection Using Hyperspectral Edge Sensors |
| Organization | Ministry of Food Processing Industries (MoFPI) |
| Theme | Agriculture, FoodTech & Rural Development |
| Category | Hardware |
| Team | CROWNX |

Food safety today relies on random batch sampling sent to labs for culture testing, which takes days. Contaminated products are often already packaged and shipped before pathogens are detected, causing costly recalls and public health risk.

## Our Solution — SpectraGuard

SpectraGuard is an inline, non-destructive hardware sensing system that scans every item moving on a production conveyor in real time, using multispectral sensing to detect invisible bacterial biofilms and early pathogens (Salmonella, Listeria, E. coli), and automatically reports results — including an end-of-day compliance summary — to the plant and the food safety authority (FSSAI).

### Core Process Workflow

```
SCAN → DETECT → FLAG → SORT → LOG → REPORT
```

1. **Scan** — Multispectral sensor rig (NIR/UV illumination) captures spectral data on every item, at full conveyor speed, with no stoppage.
2. **Detect** — Edge-AI classifier compares readings against a contamination spectral signature library, in milliseconds.
3. **Flag** — Contaminated items are instantly flagged.
4. **Sort** — A signal is sent to trigger a downstream sorting actuator to isolate flagged items.
5. **Log** — Every scan result (pass/flag) is timestamped and recorded locally.
6. **Report** — An aggregated report (e.g. "1,00,000 scanned, 99,742 passed, 258 flagged") is auto-transmitted to the plant and to FSSAI at end of day.

## Tech Stack

- **Sensing:** AS7265x multispectral sensor array (18-channel, visible–NIR), NIR/UV LED illumination
- **Edge Compute:** Raspberry Pi / Jetson Nano
- **Classification:** TensorFlow Lite (lightweight model), scikit-learn (prototyping)
- **Connectivity/Reporting:** MQTT / REST API sync to cloud compliance dashboard
- **Dashboard:** Web-based compliance reporting view

## Repository Structure

```
├── README.md                     ← you are here
├── software/
│   └── sensor_simulation.py      ← proof-of-concept: simulated sensor + classifier + EOD report
├── hardware/
│   └── BOM.md                    ← bill of materials for the sensor rig
├── docs/
│   └── architecture.md           ← system architecture & data flow notes
└── presentation/
    └── (SIH idea presentation PDF/PPTX goes here)
```

## Status

This is an **idea-stage submission** for SIH 2026. We have not yet built the physical hyperspectral rig — the `software/sensor_simulation.py` script demonstrates our proposed detection and reporting logic using simulated sensor data, since no public dataset was provided with the problem statement. A real deployment would use lab-validated spectral signature libraries for Salmonella, Listeria and E. coli.

## Team CROWNX

- CHETAN PRASAD — CSE
- AYUSH RANJAN — Electronics
- PRATIK RAJ — Electronics
- SAPNA KUMARI — Electronics
- SONALI KUMARI — Electronics
- CHANDAN SINGH BIST — CSE

## License

This repository is submitted as part of Smart India Hackathon 2026. All rights to the concept and content remain with Team CROWNX unless otherwise agreed with the problem-statement organization (MoFPI) per SIH's IP-sharing terms.
