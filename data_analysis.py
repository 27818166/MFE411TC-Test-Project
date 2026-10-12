"""
MFE411TC: Big Data Analysis for Manufacturing
Coursework Practice Script
Description: Simulated sensor data anomaly detection for manufacturing equipment.
"""

import numpy as np
import pandas as pd


def generate_sensor_data(n_samples: int = 100) -> pd.DataFrame:
    """Generate simulated industrial sensor data (temperature and vibration).

    Args:
        n_samples (int): Number of time points to simulate.

    Returns:
        pd.DataFrame: Simulated sensor readings with timestamps.
    """
    np.random.seed(42)
    timestamps = pd.date_range(
        start="2026-01-01", periods=n_samples, freq="1min"
    )

    # Simulate normal manufacturing temperature (around 75 deg C) with random noise
    temperature = np.random.normal(loc=75.0, scale=2.5, size=n_samples)
    # Simulate normal vibration amplitude (around 0.5 mm/s)
    vibration = np.random.normal(loc=0.5, scale=0.08, size=n_samples)

    # Inject simulated anomalies for testing
    temperature[20] = 95.5  # High-temperature fault
    vibration[50] = 1.2  # Excessive vibration fault

    data = pd.DataFrame(
        {
            "timestamp": timestamps,
            "temperature_celsius": temperature,
            "vibration_amplitude": vibration,
        }
    )
    return data


def detect_anomalies(
    df: pd.DataFrame, temp_threshold: float = 85.0
) -> pd.DataFrame:
    """Detect equipment anomalies based on a temperature threshold.

    Args:
        df (pd.DataFrame): Sensor dataframe.
        temp_threshold (float): Safe operating temperature limit.

    Returns:
        pd.DataFrame: Records exceeding the safety threshold.
    """
    anomalies = df[df["temperature_celsius"] > temp_threshold]
    return anomalies


if __name__ == "__main__":
    print("=== Manufacturing Big Data Analysis: Practice Run ===")

    # Step 1: Ingest sensor stream data
    sensor_stream = generate_sensor_data(n_samples=100)
    print(f"Loaded {len(sensor_stream)} sensor readings.")

    # Step 2: Perform quality control and anomaly detection
    faults = detect_anomalies(sensor_stream, temp_threshold=85.0)
    print(f"Warning: {len(faults)} anomalous events detected in operation!")
    print(faults)