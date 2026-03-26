**************
GRS Demodulator
**************

Overview
========

The GRS Demodulator is a GMSK demodulator for SpaceLab's Ground Station signal processing pipeline. It sits between the IQ Receiver and the syncword detector and decoder, receiving a continuous stream of complex IQ samples over ZMQ and publishing a recovered bitstream for downstream processing.

Key Features
============

- **GMSK Demodulation**: Implements a full software GMSK demodulation pipeline operating on complex IQ samples.
- **GMSK Modulation**: Includes a GMSK modulator, enabling closed-loop simulation and unit testing of the full modulation/demodulation chain without hardware.
- **Gaussian Matched Filtering**: Applies a Gaussian filter matched to the signal's BT product to reduce inter-symbol interference prior to symbol decisions.
- **Symbol Timing Recovery**: Synchronizes sampling instants to symbol boundaries to reliably recover the bitstream under realistic channel conditions.
- **ZMQ Integration**: Subscribes to IQ sample frames from the IQ Receiver and publishes the recovered bitstream to downstream components over ZMQ.

Architecture
============

The GRS Demodulator is structured as a streaming DSP pipeline:

- **Input**: A ZMQ SUB socket receiving buffered complex IQ sample frames from the IQ Receiver.
- **Frequency Discriminator**: Extracts instantaneous frequency deviations by computing the phase derivative of the incoming IQ samples.
- **Gaussian Matched Filter**: Filters the frequency deviation signal with a Gaussian filter matched to the BT product, reducing inter-symbol interference.
- **Normalization**: Centers and scales the filtered signal to ensure reliable downstream symbol decisions.
- **Timing Recovery**: Recovers symbol timing from the filtered signal, aligning the sampling instants to the transmitted symbol boundaries.
- **Hard Decision**: Thresholds the soft symbols into a binary bitstream.
- **Output**: A ZMQ PUB socket publishing the recovered bitstream to the syncword detector and decoder.

Usage
=====

To use the GRS Demodulator:

1. **Install dependencies**: Install the required Python packages.
2. **Start the IQ Receiver**: Ensure the upstream IQ Receiver is running and publishing IQ sample frames.
3. **Run the demodulator**: Launch the application to begin consuming IQ frames and publishing the recovered bitstream.
4. **Start downstream components**: The syncword detector and decoder can now connect and begin processing the demodulated bitstream.
