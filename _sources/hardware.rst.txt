********
Hardware
********

This section describes the hardware side of the UFSC ground station and details the main peripherals that will be used in this project. Most of the components described here are represented in the block diagram.

Antennas
========

There are four antennas in the ground station: One for VHF, two for the UHF band, and one for the S-Band. The main characteristics of these antennas can be seen in :numref:`tab:antennas`.

.. _tab:antennas:

.. list-table:: Main characteristics of the ground segment antennas.
   :name: Antennas
   :header-rows: 1
   :widths: 15 15 15 15 15

   * - **Characteristic**
     - **VHF Antenna**
     - **UHF Antenna**
     - **UHF Antenna**
     - **S-Band Antenna**
   * - Brand
     - M²
     - M²
     - M²
     - TBD
   * - Model
     - 2MCP14
     - 403CP20
     - 466CP42
     - TBD
   * - Type
     - Yagi
     - Yagi
     - Yagi
     - TBD
   * - Number of elements
     - 14
     - 10
     - 20
     - TBD
   * - Frequency range
     - 143-148 MHz
     - 398-408 MHz
     - 462-470 MHz
     - TBD
   * - Gain
     - 12.34 dBi
     - 14 dBi
     - 19 dBi
     - TBD
   * - Power rating
     - 1500 W
     - 1500 W
     - 600 W
     - TBD
   * - Boom length
     - 3.2 m
     - 1.95 m
     - 5.54 m
     - TBD
   * - Longest element
     - 1.02 m
     - 0.381 m
     - 0.297 m
     - TBD
   * - Weight
     - 2.72 kg
     - 2.72 kg
     - 5.90 kg
     - TBD

More information about the VHF and UHF antennas can be found in :cite:`2mcp14`, :cite:`403CP20` and :cite:`466CP42` respectively.

Surge Protector
---------------

To protect the ground station electronics of possible atmospheric discharges in the outside components, two surge protectors will be used (one for each antenna). The gas surge protectors safely discharge/deflect up to 5000 A of peak current to earth without causing damage to an independent ground. This kind of device is installed near the antennas, in cascade with the RF cables.

For this project the model MFJ-270N will be used, and a picture of it can be seen in :numref:`fig:mfj-270n`.

.. _fig:mfj-270n:

.. figure:: img/mfj-270n.jpeg
      :width: 50%
      :align: center
      :alt: Surge protector.

      MFJ-270N surge protector.

Rotator
=======

All antennas track the satellite through a two-axis rotator (azimuth and elevation). The used model is the Hy-Gain RAS-2, which is a heavy-duty antenna rotator designed for medium to large HF and VHF/UHF antennas. It features a robust construction with a 1,000 lb (454 kg) thrust bearing and 200 lb (91 kg) continuous wind load rating, making it suitable for demanding installations. The rotator uses a dual-drum cable system for precise 360-degree rotation and includes automatic braking to prevent unwanted movement.

A picture of this rotator can be seen in :numref:`fig:ras-2`, and the main characteristics can be found in :numref:`tab:grs-rotor`.

.. _fig:ras-2:

.. figure:: img/ras-2.jpg
   :width: 60%
   :align: center

   Hy-Gain RAS-2 rotator and controller.

.. _tab:grs-rotor:

.. list-table:: Main characteristics of antennas' rotators.
   :widths: 45 25
   :header-rows: 1

   * - **Characteristic**
     - **Value**
   * - Brand
     - Hy-Gain
   * - Model
     - RAS-2
   * - Voltage requirement
     - 12-24 V\ :sub:`DC`
   * - Current consumption
     - 3-5 A
   * - Motor voltage
     - 13.8-24 V\ :sub:`DC`
   * - Rotation time (elevation, 180\ :sup:`°`)
     - 80 sec (12 V), 40 sec (24 V)
   * - Rotation time (azimuth, 360\ :sup:`°`)
     - 120 sec (12 V), 60 sec (24 V)
   * - Rotation torque (elevation)
     - 58 kg·m
   * - Rotation torque (azimuth)
     - 58 kg·m
   * - Braking torque (elevation and azimuth)
     - 276 kg·m
   * - Vertical load
     - 318 kg
   * - Pointing accuracy
     - 1 degree
   * - Wind surface area
     - 2.8 m\ :sup:`2`
   * - Weight
     - 20 kg

More information about the ground station rotator can be found in :cite:`ras-2`.

Amplifiers
==========

Power Amplifiers (VHF/UHF)
--------------------------

A picture of the power amplifier can be seen in :numref:`fig:zhl-50w`, and the main characteristics are available in :numref:`tab:zhl-50w-specs`.

.. _fig:zhl-50w:

.. figure:: img/zhl-50w.png
   :width: 30%
   :align: center

   Mini-Circuits ZHL-50W-52-S+ power amplifier.

.. _tab:zhl-50w-specs:

.. list-table:: Main characteristics of the ZHL-50W-52-S+ power amplifier.
   :widths: 40 30
   :header-rows: 1

   * - **Characteristic**
     - **Value**
   * - Brand
     - Mini-Circuits
   * - Model
     - ZHL-50W-52-S+
   * - Frequency range
     - 50-500 MHz
   * - Gain
     - 47-52 dB
   * - Noise figure
     - 4.5-7.0 dB
   * - DC supply voltage
     - 24-25 V
   * - Max. supply current
     - 9.3 A

More information about this PA can be found in :cite:`zhl-50w`.

Power Amplifiers (S-Band)
--------------------------

.. note::
    TODO

Low-Noise Amplifier (VHF/UHF)
-----------------------------

For the LNA of the VHF/UHF bands, the Mini-Circuits ZFL-500LN+ model is being used. It operates over a wide frequency range of 0.1 to 500 MHz, making it suitable for communications, test equipment, and signal boosting in weak-signal environments. A picture of this device is available in :numref:`fig:zfl-500ln`, the main specs can be seen in :numref:`tab:zfl-500ln-specs`.

.. _fig:zfl-500ln:

.. figure:: img/zfl-500ln.png
   :width: 30%
   :align: center

   Mini-Circuits ZFL-500LN+ LNA.

.. _tab:zfl-500ln-specs:

.. list-table:: Main characteristics of the ZFL-500LN+ LNA.
   :widths: 40 30
   :header-rows: 1

   * - **Characteristic**
     - **Value**
   * - Brand
     - Mini-Circuits
   * - Model
     - ZFL-500LN+
   * - Frequency range
     - 0.1 to 500 MHz
   * - Noise figure
     - 2.9 dB
   * - Gain
     - 24 dB (Min.)
   * - Maximum output power
     - 5 dBm
   * - Input voltage
     - 15 V
   * - Current consumption
     - 15 mA (Nominal)

More information about this LNA can be found in :cite:`zfl-500ln`.

Software Defined Radio
----------------------

As presented in :numref:`fig:grs-block-diagram`, the ground segment also has three SDR transceivers. The deployed model is the USRP N210 from Ettus Research :cite:`n210`, a high-performance, networked software-defined radio platform. Unlike single-board designs with integrated RFICs (e.g., AD9361), the N210 features a modular architecture with:

- **Frequency coverage**: DC to 6 GHz (via interchangeable daughterboards like SBX/WBX).
- **FPGA processing**: Xilinx Spartan 3A-DSP 1800 for customizable signal processing.
- **Host connectivity**: Gigabit Ethernet (1 GbE) for high-throughput streaming.
- **Synchronization**: 10 MHz reference clock and PPS input for multi-unit coordination.

The platform supports the USRP Hardware Driver (UHD), enabling seamless integration with GNURadio and other SDR frameworks. A picture of the USRP N210 SDR (with enclosure) can be seen in :numref:`fig:usrp-n210`.

.. _fig:usrp-n210:

.. figure:: img/usrp-n210.jpg
   :width: 60%
   :align: center

   Ettus USRP N210 SDR.


The :numref:`tab:n210-specs` lists the key hardware specifications of the USRP N210 SDR.

.. _tab:n210-specs:

.. list-table:: USRP N210 Hardware Specifications
   :widths: 30 70
   :header-rows: 1
   :class: longtable

   * - **Category**
     - **Specification**
   * - **RF Performance**
     -
   * - Frequency Range
     - DC – 6 GHz (with compatible daughterboard)
   * - Maximum Bandwidth
     - 50 MHz (25 MHz usable in practice)
   * - ADC Resolution
     - 14-bit
   * - DAC Resolution
     - 16-bit
   * - **Processing & Connectivity**
     -
   * - FPGA
     - Xilinx Spartan 3A-DSP 1800
   * - Host Interface
     - Gigabit Ethernet (1 GbE)
   * - Sample Rate (Complex)
     - Up to 100 MS/s
   * - **Synchronization**
     -
   * - Reference Clock Input
     - 10 MHz (external)
   * - PPS Input
     - Yes (for timing synchronization)
   * - **Expansion & Power**
     -
   * - Daughterboard Slots
     - 2 (supports SBX, WBX, etc.)
   * - MIMO Capability
     - Yes (2x2 with secondary USRP)
   * - Power Supply
     - 6–12 V DC (9–12 V recommended)
