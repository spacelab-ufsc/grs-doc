********
Software
********

Software Architecture
=====================
.. _fig:software-diagram:

.. figure:: img/block-diagram-software.png
   :width: 100%
   :align: center

   Ground station software diagram.

Station Server
--------------

- **Rotor Manager**: TODO.
- **FFT**: `https://github.com/spacelab-ufsc/grs-fft <https://github.com/spacelab-ufsc/grs-fft>`__
- **IQ Receiver**: `https://github.com/spacelab-ufsc/grs-iq-rx <https://github.com/spacelab-ufsc/grs-iq-rx>`__
- **Demodulator**: `https://github.com/spacelab-ufsc/grs-demodulator <https://github.com/spacelab-ufsc/grs-demodulator>`__
- **Sync. Word Detector**: TODO.
- **Frequency Synth.**: TODO.
- **Modulator**: `https://github.com/spacelab-ufsc/grs-modulator <https://github.com/spacelab-ufsc/grs-modulator>`__
- **RF Front-End Controller**: TODO.

Control Server
--------------

- **Dashboard Backend**: Grafana.
- **Database**: TODO.
- **Data Link Layer Decoders**: TODO.
- **Network Layer Decoders**: TODO.
- **Satellite Data Decoders**: TODO.
- **Station Manager**: TODO.
- **Data Link Layer Encoder**: TODO.
- **Network Layer Encoder**: TODO.
- **Satellite TC Scheduler**: TODO.

Control Desktop
---------------

- **Dashboard**: TODO.
- **Satellite Tracker**: GPredict.
- **GRS Manager**: TODO.
- **Spectrum Monitor**: TODO.
- **Satellite TC Generator**: TODO.

Satellite Tracking
==================

To track the satellite and for orbit prediction, the GPredict software :cite:`gpredict` will be used. Gpredict is a real-time satellite tracking and orbit prediction application. It can track a large number of satellites and display their position and other data in lists, tables, maps, and polar plots (radar view). Gpredict can also predict the time of future passes for a satellite, and provide you with detailed information about each pass. Gpredict is free software licensed under the GNU General Public License. A picture of the main window of GPredict can be seen in :numref:`fig:gpredict`.

.. _fig:gpredict:

.. figure:: img/gpredict.png
   :width: 100%
   :align: center

   Main window of GPredict.
