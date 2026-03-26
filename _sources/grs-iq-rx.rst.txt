***************
GRS IQ Receiver
***************

Overview
========

The GRS IQ Receiver is the SDR front-end of SpaceLab's Ground Station signal processing pipeline. It reads raw IQ samples from a Software Defined Radio (SDR) device and publishes them over ZMQ to downstream components such as the FFT Calculator and the demodulator.

The component is available in two implementations targeting different SDR hardware. Both normalize raw samples to floating-point IQ format and publish them continuously for consumption by downstream pipeline components.

Key Features
============

- **Dual Implementation**: Available as a C application targeting RTL-SDR devices, and as a Python application targeting Pluto and USRP devices.
- **Continuous IQ Streaming**: Publishes a continuous stream of normalized floating-point IQ samples over ZMQ for consumption by downstream components.
- **Dynamic Retuning**: The Python implementation listens for tune commands from the Frequency Synthesizer, allowing the center frequency to be updated at runtime without restarting.
- **Flexible Acquisition**: The C implementation supports both synchronous and asynchronous acquisition modes, with configurable gain, sample rate, bandwidth, PPM correction, and block size.
- **ZMQ Integration**: Built around the ZeroMQ messaging library for integration with other ground station microservices.

Architecture
============

The IQ Receiver sits between the Frequency Synthesizer and the downstream signal processing components:

- **SDR Input**: Acquires IQ samples directly from the connected SDR hardware.
- **Normalization**: Raw device samples are converted to normalized floating-point complex (IQ) format before publishing.
- **Buffering**: Samples are accumulated into fixed-size buffers before being dispatched to avoid flooding downstream subscribers.
- **ZMQ Output**: A ZMQ PUB socket continuously publishes buffered IQ sample frames to the FFT Calculator and demodulator.
- **Retune Input**: A ZMQ SUB socket listens for tune commands from the Frequency Synthesizer and updates the SDR center frequency at runtime.

Usage
=====

To use the GRS IQ Receiver:

1. **Install dependencies**: Install the required libraries for the chosen implementation.
2. **Connect the SDR hardware**: Ensure the SDR device is connected and recognized by the system.
3. **Start the IQ Receiver**: Launch the application with the desired center frequency, sample rate, and gain.
4. **Start downstream components**: The FFT Calculator and demodulator can now connect and begin consuming the published IQ stream.
5. **Retune at runtime**: Start the Frequency Synthesizer to send dynamic tune commands as the satellite pass progresses.
