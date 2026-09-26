# Bill of Materials — SpectraGuard Sensor Rig (Proposed)

This is our proposed component list for building a working prototype, scoped to
realistic off-the-shelf hardware rather than a full industrial hyperspectral
imaging system (which would cost lakhs and isn't feasible within hackathon scope).

| Component | Purpose | Approx. Cost (INR) |
|---|---|---|
| AS7265x Spectral Sensor Triad (18-channel) | Captures multispectral reflectance data across visible–NIR bands, standing in for full hyperspectral imaging | ₹6,000 – ₹9,000 |
| NIR/UV LED array + driver circuit | Active illumination at target wavelengths to reveal contamination signatures | ₹1,000 – ₹1,500 |
| Raspberry Pi 4 (4GB) or Jetson Nano | Edge compute for real-time classification | ₹6,000 – ₹15,000 |
| Relay module | Output signal to trigger downstream sorting actuator | ₹300 – ₹500 |
| Mounting rig / gantry frame | Positions sensor over conveyor | ₹1,500 – ₹2,500 |
| Mock conveyor belt (for demo) | Simulates production line motion for testing | ₹1,000 – ₹3,000 |
| Misc wiring, connectors, enclosure | Assembly | ₹1,000 – ₹2,000 |

**Estimated total: ₹17,000 – ₹33,500** depending on sensor grade and edge board choice.

## Notes

- This BOM assumes a **scaled proof-of-concept** using a multispectral sensor
  (fewer, broader bands) rather than a true hyperspectral camera (hundreds of
  narrow bands), which is standard practice for hackathon-stage hardware builds.
- A production deployment would need IP-rated (dust/moisture resistant) housing,
  which is not costed here since it depends on the specific plant environment.
- No dataset was provided with the problem statement; a real deployment would
  require lab-validated spectral signatures for Salmonella, Listeria and E. coli
  biofilms, likely developed in partnership with a food-testing lab or MoFPI.
