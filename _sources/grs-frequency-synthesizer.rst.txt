************************
GRS Frequency Synthesizer
************************

Overview
========

The GRS Frequency Synthesizer is an internal component of SpaceLab's Ground Station software pipeline. It sits between the Station Manager and the IQ Receiver, responsible for computing the effective tuning frequency at any given moment by combining the base center frequency with a Doppler correction offset, and forwarding the result to the IQ Receiver as a tune command.

The IQ Receiver is autonomous and does not depend on the Frequency Synthesizer to operate — it simply reacts to tune commands whenever they arrive. The Frequency Synthesizer is an optional layer that handles Doppler correction math on top, as well as any changes in the center frequency.

Key Features
============

- **Doppler Correction**: Combines a base center frequency with a pre-computed Doppler offset to produce the effective tuning frequency at any given moment.
- **ZMQ Integration**: Subscribes to commands from the Station Manager and publishes tune commands to the IQ Receiver over ZMQ.
- **Graceful Startup**: Withholds tune commands until a valid center frequency has been received, preventing the IQ Receiver from being tuned to an undefined frequency.
- **Stateful Offset Tracking**: Maintains the current Doppler offset independently from the center frequency, updating either as new commands arrive.
- **Lightweight**: Implemented as a single Python class with minimal dependencies, designed to be embedded in the Station Manager process.

Architecture
============

The Frequency Synthesizer is structured as a managed pipeline component:

- **Input**: A ZMQ SUB socket connected to the Station Manager, subscribed to center frequency and Doppler offset update commands.
- **State**: Maintains the current center frequency and Doppler offset internally, updating each independently as commands arrive.
- **Computation**: The effective tuning frequency is calculated as the sum of the center frequency and the current Doppler offset.
- **Output**: A ZMQ PUB socket that publishes tune commands to the IQ Receiver whenever the effective frequency changes.

.. note::
   The Frequency Synthesizer does not compute Doppler shifts itself. It expects the Station Manager or a dedicated propagator module to supply pre-computed Doppler offsets.

Usage
=====

To use the GRS Frequency Synthesizer:

1. **Install dependencies**: Install the required Python packages.
2. **Instantiate the class**: Create a ``FrequencySynthesizer`` instance with the appropriate ZMQ addresses for the IQ Receiver and Station Manager.
3. **Start the synthesizer**: Call ``run()`` to begin listening for commands and publishing tune updates.
4. **Send a center frequency**: The Station Manager must send an initial ``freq`` command before any tune commands are forwarded to the IQ Receiver.
5. **Send Doppler offsets**: The Station Manager (or propagator module) sends periodic ``doppler`` commands to keep the tuning frequency compensated in real time.
6. **Stop gracefully**: Call ``stop()`` to shut down the synthesizer and release ZMQ resources.
