****************
Spectrum Monitor
****************

Overview
========

The Spectrum Monitor is a real-time visualization tool designed for the FloripaSat-2A ground station. It processes raw IQ samples via UDP, performs Fast Fourier Transform (FFT), and renders an interactive Waterfall display in the browser. This component is essential for monitoring signal quality and detecting interference during satellite passes.

Key Features
============

- **Real-time FFT Plot**: Displays the instantaneous spectral density as a line graph.
- **Waterfall Display**: Provides a historical view of frequency over time using a thermal color palette.
- **Dynamic Gain Control**: Allows users to adjust the visual sensitivity of the signal display.
- **Signal Detection**: Includes a configurable threshold line with visual alerts for signal detection.
- **Microservices Architecture**: Built to be easily integrated via Docker and WebSockets.

Architecture
============

The Spectrum Monitor is structured as follows:

- **Backend**: Python-based application using Flask and Socket.IO for real-time communication.
- **DSP Processing**: Utilizes NumPy for Digital Signal Processing (DSP), including Hamming windowing and FFT conversion.
- **Frontend**: HTML5 Canvas for high-performance rendering of the waterfall display.
- **Concurrency**: Managed by Eventlet to handle network threads and web server requests efficiently.

Usage
=====

To use the Spectrum Monitor:

1. **Start the Simulator**: Run the mock IQ sender to simulate radio signals.
2. **Launch the Server**: Start the backend processing server.
3. **Access the Interface**: Open a web browser to view the real-time spectrum data.

For integration with real hardware, the UDP stream can be configured to receive data from the Station Server.
