# Real-Time Sign Language Detector

A computer vision project that detects sign language gestures in real time from a live camera feed, built with OpenCV and TensorFlow — wrapped in a full CI/CD pipeline that automatically builds, tests, and deploys the project to a live AWS server on every push.

## What this project demonstrates

This started as a computer vision project, but the bigger part of it is the infrastructure around it: a working CI/CD pipeline, containerization, and real cloud deployment — built and debugged from scratch.

- **Computer Vision**: Real-time gesture detection using OpenCV and TensorFlow, with detection accuracy between 80–95% depending on the gesture.
- **Containerization**: The entire application is Dockerized for consistent, reproducible builds across environments.
- **CI (Continuous Integration)**: GitHub Actions automatically builds a Docker image and verifies core dependencies on every push to `main`.
- **CD (Continuous Deployment)**: The built image is deployed to a live AWS EC2 instance (Amazon Linux), provisioned and configured manually — including security groups, SSH access, and Docker installation.

## Tech stack

| Layer | Tools |
|---|---|
| Language | Python |
| Computer Vision / ML | OpenCV, TensorFlow |
| Containerization | Docker |
| CI/CD | GitHub Actions |
| Cloud Deployment | AWS EC2 (Amazon Linux) |

## Pipeline overview

```
Push to GitHub
      │
      ▼
GitHub Actions (CI)
  ├─ Build Docker image
  └─ Verify core dependencies (OpenCV, TensorFlow, NumPy)
      │
      ▼
Deploy to AWS EC2
  ├─ Pull latest code
  ├─ Build Docker image on the server
  └─ Run container
```

## Note on the container's entrypoint

The container runs `healthcheck.py` by default instead of the full detection script (`main1.py`). This is intentional: the full detection pipeline requires a physical webcam, which isn't available on a headless remote server. The health check verifies that the environment — OpenCV, TensorFlow, NumPy, and all dependencies — builds and loads correctly, which is what the CI/CD pipeline is actually meant to prove.

To run full real-time detection, clone the repo and run `main1.py` locally on a machine with a connected webcam.

## Real challenges solved along the way

This pipeline didn't work on the first try. Along the way, I diagnosed and fixed:

- A branch name mismatch (`master` vs `main`) that silently prevented the workflow from triggering
- A malformed `requirements.txt` line that broke `pip install`
- A Windows-only package (`tensorflow-intel`) that doesn't exist on Linux
- A version conflict between `numpy`, `opencv-python`, and `tensorflow`
- Bugs introduced when converting a Jupyter Notebook to a plain Python script (Windows-style backslashes inside f-strings, missing `shell=True` flags, `get_ipython()` calls that only work inside Jupyter)
- A missing `git` binary inside the Docker image, needed for a step the original script performed at runtime

## Running it locally

```bash
git clone https://github.com/mr-coder77/real-time-sign-language-detector.git
cd real-time-sign-language-detector
docker build -t sign-detector .
docker run --rm sign-detector
```

For full real-time detection with a webcam, run `main1.py` directly with Python instead of through Docker.

## Author

Ahmed HasabAlrasoul NourEldin Eltahir
[GitHub](https://github.com/mr-coder77) · [LinkedIn](https://www.linkedin.com/in/ahmed-hasabalrsoul-ba19a3330/)
