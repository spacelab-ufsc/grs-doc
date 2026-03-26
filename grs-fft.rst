*******
GRS FFT
*******

Overview
========

GRS FFT is a real-time Fast Fourier Transform (FFT) calculator for SpaceLab's Ground Station. It is part of the ground station's signal processing pipeline, sitting between the IQ sample receiver and the spectrum visualization components.

The program subscribes to a ZMQ publisher socket where it receives a continuous stream of raw IQ samples. Once a full frame is accumulated, it applies a Hann window to reduce spectral leakage and computes a complex FFT, which can be used by downstream components.

Key Features
============

- **Real-time IQ Processing**: Continuously receives IQ sample streams over ZMQ.
- **Hann Windowing**: Applies a Hann window to both I and Q components before transformation to minimize spectral leakage.
- **ZMQ Integration**: Built around the ZeroMQ messaging library for seamless integration with other ground station microservices.
- **Lightweight and Efficient**: Written in C with minimal dependencies, optimized for low-latency signal processing.

Architecture
============

GRS FFT is structured around a simple and efficient signal processing pipeline:

- **Input**: A ZMQ SUB socket connected to the upstream IQ receiver.
- **Buffering**: IQ samples are accumulated into fixed-size frames before processing.
- **DSP Processing**: A Hann window is applied prior to FFT computation.
- **FFT Computation**: An in-place forward complex DFT is performed on each windowed sample frame.
- **Output**: The resulting frequency-domain data is made available to downstream components such as the Spectrum Monitor.

Usage
=====

To use GRS FFT:

1. **Install dependencies**: Install the required libraries.
2. **Build the project**: Compile the project using the provided build system.
3. **Start the IQ receiver**: Ensure the upstream IQ sample publisher is running and reachable.
4. **Run GRS FFT**: Execute the compiled binary to begin receiving samples and computing FFT frames in real time.
