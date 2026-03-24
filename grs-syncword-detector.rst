**********************
GRS Syncword Detector
**********************

Overview
========

GRS Syncword Detector is a C library component of SpaceLab's Ground Station signal processing pipeline. It sits between the demodulator and the decoder, and is responsible for identifying the start of a transmission by detecting a known synchronization word (syncword) within an incoming bit stream.

The component supports both MSB-first and LSB-first bit endianness, and performs tolerance-based matching by counting the number of bits that match the expected syncword pattern, allowing it to handle minor bit errors in the received stream.

Key Features
============

- **Syncword Detection**: Identifies the start of a transmission frame by searching for a known bit pattern in the incoming stream.
- **Endianness Support**: Handles both MSB-first and LSB-first bit ordering to accommodate different modulation and framing conventions.
- **Tolerance-Based Matching**: Counts matching bits rather than requiring a strict equality, providing robustness against minor bit errors.
- **Lightweight**: Written in C with no external dependencies, suitable for integration into larger ground station pipelines.

Architecture
============

The syncword detector is structured as a reusable library component:

- **Input**: A raw bit stream produced by the upstream demodulator.
- **Syncword Definition**: A configurable byte sequence and endianness that defines the expected synchronization pattern.
- **Bit Expansion**: Each syncword byte is expanded into its individual bits, respecting the configured endianness, for bit-level comparison.
- **Matching**: A sliding window scans the incoming bit stream and counts how many bits match the syncword pattern at each position.
- **Output**: The match score at each position, which the caller uses to determine the start of a transmission frame and pass it to the decoder.

Usage
=====

To use GRS Syncword Detector:

1. **Build the project**: Compile the component using the provided build system.
2. **Define the syncword**: Create a syncword instance by providing the expected byte sequence and bit endianness.
3. **Feed the bit stream**: Pass incoming bits from the demodulator through the matching function.
4. **Detect frame start**: Use the match score to determine when a valid syncword has been found and forward the frame to the decoder.
5. **Clean up**: Destroy the syncword instance to free allocated resources.
