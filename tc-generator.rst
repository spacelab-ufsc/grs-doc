**********************
Satellite TC Generator
**********************

Overview
========

The Satellite TC Generator is a web-based application designed for the generation and management of telecommands for satellites. It provides a user-friendly interface for creating, scheduling, and sending commands to the satellite.

Key Features
============

- **Web Interface**: Built with Flask, offering a responsive and intuitive UI for operators.
- **Command Management**: Allows for the creation and storage of telecommand definitions.
- **Database Integration**: Uses PostgreSQL for persistent storage of command history and configurations.
- **Microservices Architecture**: Designed to be deployed as a containerized service within the larger ground station ecosystem.

Architecture
============

The TC Generator follows a modular architecture:

- **Core Application**: Flask-based web server handling HTTP requests and routing.
- **Services Layer**: Encapsulates business logic for telecommand processing.
- **Repositories**: Manages data access using database adapters.
- **Models**: Defines the data structures for satellites and telecommands.

Usage
=====

To set up and run the TC Generator:

1. **Environment Setup**: Create a virtual environment and install dependencies.
2. **Database Initialization**: Run database migrations to set up the schema.
3. **Run Application**: Start the Flask server to access the web interface.

The application is configured via environment variables and can be easily deployed using Docker.
