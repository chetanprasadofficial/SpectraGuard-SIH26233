"""
SpectraGuard — Proof-of-Concept Simulation
SIH 2026 | Problem Statement 26233 | Team CROWNX

This script simulates the core detection + reporting pipeline described in our
idea submission, since we do not yet have the physical hyperspectral sensor rig
built, and no public contamination-spectral dataset was provided with the PS.

It simulates:
1. Multispectral sensor readings for a batch of items (some "contaminated", some "clean")
2. A simple classifier flagging contaminated items based on spectral signature deviation
3. An end-of-day aggregated compliance report, matching the format we propose
   auto-sending to the plant and FSSAI in a real deployment.

Run: python sensor_simulation.py
"""

import random
import json
from datetime import datetime

# ---- Simulated config ----
NUM_SPECTRAL_CHANNELS = 18          # matches AS7265x (18-channel multispectral sensor)
CONTAMINATION_THRESHOLD = 0.72      # similarity score below this = flagged
PLANT_NAME = "XYZ Foods Pvt Ltd"


def simulate_clean_signature():
    """A 'clean' item's spectral reflectance profile (simulated baseline)."""
    return [round(random.uniform(0.80, 1.0), 3) for _ in range(NUM_SPECTRAL_CHANNELS)]


def simulate_contaminated_signature():
    """A 'contaminated' item's spectral profile — deviates in a subset of bands,
    mimicking how biofilms/pathogens alter reflectance in specific NIR/UV bands."""
    profile = simulate_clean_signature()
    # simulate deviation in a random subset of bands (where contamination shows up)
    affected_bands = random.sample(range(NUM_SPECTRAL_CHANNELS), k=random.randint(3, 6))
    for b in affected_bands:
        profile[b] = round(random.uniform(0.2, 0.6), 3)
    return profile


def classify(signature, reference=None):
    """Very simple similarity-based classifier (stand-in for a trained model).
    Compares the item's signature against a 'clean' reference and returns
    a similarity score; below threshold => flagged as contaminated."""
    if reference is None:
        reference = [1.0] * NUM_SPECTRAL_CHANNELS
    diffs = [abs(a - b) for a, b in zip(signature, reference)]
    similarity = 1 - (sum(diffs) / len(diffs))
    return round(similarity, 3)


def scan_batch(n_items=100000, contamination_rate=0.0026):
    """Simulates scanning a full day's production batch."""
    results = []
    n_contaminated = int(n_items * contamination_rate)
    n_clean = n_items - n_contaminated

    # NOTE: for speed, we simulate a representative sample rather than looping
    # n_items times individually — real edge hardware would process every item live.
    sample_size = min(n_items, 2000)
    contaminated_sample = int(sample_size * contamination_rate)
    clean_sample = sample_size - contaminated_sample

    for _ in range(clean_sample):
        sig = simulate_clean_signature()
        score = classify(sig)
        results.append(score >= CONTAMINATION_THRESHOLD)

    for _ in range(contaminated_sample):
        sig = simulate_contaminated_signature()
        score = classify(sig)
        results.append(score >= CONTAMINATION_THRESHOLD)

    passed_ratio = sum(results) / len(results)
    total_passed = round(n_items * passed_ratio)
    total_flagged = n_items - total_passed

    return {
        "plant": PLANT_NAME,
        "date": datetime.now().strftime("%d-%b-%Y"),
        "total_scanned": n_items,
        "passed": total_passed,
        "flagged": total_flagged,
        "status": "AUTO-SUBMITTED TO FSSAI",
    }


def print_report(report):
    print("=" * 50)
    print("SAMPLE DAILY COMPLIANCE REPORT — SpectraGuard")
    print("=" * 50)
    print(f"Plant:          {report['plant']}")
    print(f"Date:           {report['date']}")
    print(f"Total Scanned:  {report['total_scanned']:,}")
    print(f"Passed:         {report['passed']:,}")
    print(f"Flagged:        {report['flagged']:,}")
    print(f"Status:         {report['status']}")
    print("=" * 50)


if __name__ == "__main__":
    report = scan_batch(n_items=100000)
    print_report(report)

    # This is the JSON payload structure we propose auto-sending to
    # the plant dashboard + FSSAI reporting endpoint via MQTT/REST at end of day.
    with open("daily_report.json", "w") as f:
        json.dump(report, f, indent=2)
    print("\nSaved daily_report.json (example EOD payload for FSSAI auto-submission)")
