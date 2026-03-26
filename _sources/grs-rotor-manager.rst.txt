****************
GRS Rotor Manager
****************

Overview
========

The GRS Rotor Manager is an internal component of SpaceLab's Ground Station software pipeline. It is responsible for sending positioning commands to an AlfaSpid RAS-2 azimuth/elevation rotator via the Rot2Prog binary serial protocol, allowing the ground station antenna to physically track a satellite pass.

The component is driven by the Station Manager, which supplies azimuth and elevation angles computed by a propagator module. The Rotor Manager translates these angles into binary protocol packets and dispatches them to the rotator over ZMQ, while also handling status queries and stop commands.

Key Features
============

- **Antenna Tracking**: Commands the AlfaSpid RAS-2 rotator to continuously point the antenna at the satellite by accepting azimuth and elevation targets from the Station Manager.
- **Rot2Prog Protocol**: Encodes all commands as 11-byte binary packets following the Rot2Prog protocol, compatible with the AlfaSpid controller.
- **Status Polling**: Supports querying the rotator's current position, returning the live azimuth and elevation reported by the hardware.
- **ZMQ Integration**: Sends commands over a ZMQ PUSH socket and receives status responses over a ZMQ SUB socket, integrating seamlessly with the rest of the ground station pipeline.
- **Hardware Simulator**: Ships with a standalone rotator simulator for testing the pipeline without physical hardware.

Architecture
============

The Rotor Manager acts as the bridge between the Station Manager and the physical rotator hardware:

- **Input**: Method calls from the Station Manager — ``set_position()``, ``stop()``, and ``request_status()`` — supplying azimuth and elevation angles.
- **Encoding**: Target angles are encoded into the Rot2Prog 11-byte binary packet format.
- **ZMQ Output**: Packets are dispatched over a ZMQ PUSH socket to the rotator or its simulator.
- **Status Input**: A ZMQ SUB socket receives status responses from the rotator, returning the current azimuth and elevation as packed 32-bit floats.

Usage
=====

To use the GRS Rotor Manager:

1. **Install dependencies**: Install the required Python packages.
2. **Set the rotator to CPU mode**: Ensure the AlfaSpid RAS-2 front panel is set to CPU (Auto) mode so it accepts software commands.
3. **Instantiate the class**: Create a ``RotorManager`` instance, passing the ZMQ address of the rotator or simulator.
4. **Issue positioning commands**: Call ``set_position()`` with the azimuth and elevation to point the antenna.
5. **Poll status as needed**: Call ``request_status()`` to retrieve the rotator's current position.
6. **Stop and clean up**: Call ``stop()`` to halt the rotator and ``close()`` to release ZMQ resources after the satellite pass.

.. note::
   For testing without hardware, run the included ``rotor_simulator.py`` in place of the physical rotator. It accepts the same ZMQ commands and responds with simulated position data.
