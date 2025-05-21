<h1 align="center">
    <a href="https://spacelab-ufsc.github.io/grs-doc/"><img src="https://github.com/spacelab-ufsc/grs-doc/blob/main/img/logo-wide.png" alt="SpaceLab-GRS" width="30%"></a>
    <br>
    SPACELAB'S GROUND STATION
    <br>
</h1>

<h4 align="center">A ground station for transmiting telecommands and receiving telemetries of the SpaceLab's missions.</h4>

<p align="center">
	<a href="https://github.com/spacelab-ufsc/grs-doc">
        <img src="https://img.shields.io/badge/status-development-green?style=for-the-badge">
	</a>
    <a href="https://github.com/spacelab-ufsc/grs-doc/releases">
        <img alt="GitHub commits since latest release (by date)" src="https://img.shields.io/github/commits-since/spacelab-ufsc/grs-doc/latest?style=for-the-badge">
    </a>
    <a href="https://github.com/spacelab-ufsc/grs-doc/blob/main/LICENSE">
        <img src="https://img.shields.io/github/license/spacelab-ufsc/grs-doc?style=for-the-badge">
    </a>
    <a href="https://github.com/spacelab-ufsc/grs-doc/actions">
        <img src="https://img.shields.io/github/actions/workflow/status/spacelab-ufsc/grs-doc/sphinx_build.yml?style=for-the-badge">
    </a>
</p>

<p align="center">
    <a href="#overview">Overview</a> •
    <a href="#licenses">Licenses</a>
</p>

## Overview

This documentation provides a comprehensive overview of the UFSC ground station developed by SpaceLab, detailing its architecture, components, and operational capabilities. Designed to support ongoing satellite missions, the ground station features a robust and flexible system for reliable signal transmission and reception across multiple frequency bands. It's key features are:

* **Multi-band antenna systems** (VHF, UHF, S-Band) mounted on an azimuth/elevation rotor for precise satellite tracking.
* **Integrated protection and amplification** with surge protectors, LNAs, and PAs to ensure signal integrity.
* **Software Defined Radios (SDRs)** for versatile signal processing.
* **Remote operation and monitoring** via a central server.

## Dependencies

The following dependencies are required for building this project:

* [sphinx-rtd-theme](https://pypi.org/project/sphinx-rtd-theme/)
* [sphinxcontrib-bibtex](https://pypi.org/project/sphinxcontrib-bibtex/)

## Building

After installing the required dependencies, just execute the following command:

```
make html
```

## License

This documentation is licensed under  Creative Commons BY-SA 4.0 license.
