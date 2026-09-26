# System Architecture — SpectraGuard

## Data Flow

```
┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│   Conveyor    │────▶│  Multispectral │────▶│  Edge Compute │
│  (food item)  │     │  Sensor + LEDs │     │ (Pi / Jetson) │
└──────────────┘     └──────────────┘     └───────┬──────┘
                                                     │
                                    classification result
                                                     │
                      ┌──────────────────────────────┼───────────────────────┐
                      ▼                               ▼                       ▼
              ┌───────────────┐              ┌───────────────┐      ┌────────────────┐
              │  Sort Actuator │              │  Local Log DB  │      │  EOD Aggregate  │
              │ (flag/divert)  │              │  (timestamped) │      │  Report Builder │
              └───────────────┘              └───────────────┘      └────────┬────────┘
                                                                               │
                                                                               ▼
                                                                    ┌──────────────────┐
                                                                    │ Plant Dashboard +  │
                                                                    │ FSSAI Reporting API│
                                                                    └──────────────────┘
```

## Components

1. **Sensing Layer** — AS7265x multispectral sensor + NIR/UV LED illumination captures
   reflectance data for every item passing under the rig.
2. **Edge Inference Layer** — A lightweight classifier (TensorFlow Lite / scikit-learn
   model) running on-device compares the live reading against a contamination
   spectral-signature reference, producing a pass/flag decision within milliseconds.
3. **Actuation Layer** — On a flag decision, a relay signal triggers a downstream
   sorting mechanism to divert the item, without stopping the conveyor.
4. **Logging Layer** — Every scan result is timestamped and stored locally (handles
   network downtime gracefully).
5. **Reporting Layer** — At end of day, an aggregate report (total scanned / passed /
   flagged) is compiled and auto-transmitted via MQTT/REST to:
   - The plant's own compliance dashboard
   - FSSAI's reporting endpoint (format TBD — would need alignment with FSSAI's
     actual data submission API/schema, which we would need to confirm with them
     directly in a real deployment)

## Why a proxy multispectral sensor instead of true hyperspectral imaging

True hyperspectral cameras (capturing hundreds of narrow spectral bands) cost
lakhs of rupees and require weeks of calibration — not feasible within a
hackathon build. The AS7265x is an 18-channel multispectral sensor spanning
visible to near-infrared, which is a realistic, honestly-scoped proxy that
still demonstrates the core detection principle: certain wavelength bands
reflect differently in the presence of biofilms/pathogens versus clean
surfaces. A production-grade version would likely use a proper line-scan
hyperspectral imager for higher accuracy.
