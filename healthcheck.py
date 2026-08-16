"""
Health check script for the CI/CD pipeline.

This replaces running the full training/detection pipeline (main1.py) as the
container's default command. Running the full pipeline requires the complete
TensorFlow Object Detection API, a trained model checkpoint, and a physical
webcam — none of which make sense to run automatically inside a CI/CD build
or on a headless remote server.

This script instead verifies that the core dependencies the project relies on
(OpenCV, TensorFlow, NumPy) are installed correctly and importable, which is
what the CI/CD pipeline is actually meant to prove: that the environment
builds cleanly and consistently every time.
"""

import sys

print("Running environment health check...")

try:
    import cv2
    print(f"OpenCV OK — version {cv2.__version__}")
except ImportError as e:
    print(f"OpenCV import failed: {e}")
    sys.exit(1)

try:
    import tensorflow as tf
    print(f"TensorFlow OK — version {tf.__version__}")
except ImportError as e:
    print(f"TensorFlow import failed: {e}")
    sys.exit(1)

try:
    import numpy as np
    print(f"NumPy OK — version {np.__version__}")
except ImportError as e:
    print(f"NumPy import failed: {e}")
    sys.exit(1)

print("All core dependencies loaded successfully. Environment is healthy.")
