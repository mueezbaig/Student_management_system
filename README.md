# Student Management System

![License](https://img.shields.io/badge/license-MIT-green)
![Python](https://img.shields.io/badge/python-3.x-blue)

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [System Architecture](#system-architecture)
- [Entity-Relationship Diagram](#entity-relationship-diagram)
- [Installation](#installation)
- [Usage](#usage)
- [Snapshots](#snapshots)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Introduction
The **Student Management System (SMS)** is a comprehensive web-based application designed to facilitate the efficient management of student-related administrative tasks in educational institutions. It provides functionalities such as user authentication, student record management, attendance tracking, department management, and communication features.

## Features
- User Authentication (Sign Up, Log In)
- Student Record Management (Add, Edit, Delete)
- Attendance Tracking
- Department Management
- Communication through Contact Form
- Search Functionality for Student Records
- Real-time Data Processing

## Technologies Used
- **Frontend:** HTML, CSS, JavaScript
- **Backend:** Python, Flask
- **Database:** SQL, SQLAlchemy
- **Tools:** VS Code, Git, GitHub

## System Architecture
The system follows a client-server architecture with a web-based frontend and a backend server for data processing and storage.

![System Architecture](./Images/System%20architecture.jpg)

## Entity-Relationship Diagram
The ER diagram represents the data model and relationships within the system.

![ER Diagram](./Images/System%20architecture.jpg)

## Installation
1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/student-management-system.git
   cd student-management-system

2. **Create and activate a virtual environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

3. **Install the dependencies:**
    ```bash
    pip install -r requirements.txt

4. **Set up the database:**
    ```bash
    flask db init
    flask db migrate -m "Initial migration"
    flask db upgrade

5. **Run the application:**
    ```bash
    flask run

## Usage

- Open your web browser and navigate to http://127.0.0.1:5000.

- Sign up or log in to access the dashboard.

- Use the dashboard to manage student records, track attendance, manage departments, and communicate through the contact form.

## Snapshots

![Homepage]()



## Contributing

### Contributions are welcome! Please follow these steps:

- Fork the repository.
- Create a new branch (git checkout -b feature-branch).
Make your changes.
- Commit your changes (git commit -m 'Add new feature').
- Push to the branch (git push origin feature-branch).
- Open a pull request.

## License

This project is licensed under the  [MIT License](LICENSE). See the LICENSE file for details.

## Acknowledgements

I would like to thank all those who contributed to this project, especially my guide Ms. Sariya Anjum and the faculty members of the Department of Computer Science & Engineering at Mysuru Royal Institute of Technology, Mandya. Special thanks to Pacewisdom for providing an excellent platform for learning and development.
