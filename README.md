# Vaccination Tracking System

## Overview
This project consists of two main components:
1. **Flutter Project**: A mobile app for parents to keep track of their children's vaccinations and healthcare providers to maintain digital vaccination records.
2. **Python Project**: A web app built with Django for healthcare providers to maintain digital vaccination records and parents to keep track of their children's vaccinations.

Both the mobile and web apps aim to replace the traditional paper-based system, which can be prone to loss and damage, with a more reliable and accessible digital solution.

## Advantages of Vaccination Tracking
- **Improved Record Keeping**: Digital records are less likely to be lost or damaged compared to paper records.
- **Accessibility**: Parents and healthcare providers can access vaccination records anytime and anywhere.
- **Efficiency**: Streamlines the process of tracking and updating vaccination records.
- **Reminders**: Automated reminders for upcoming vaccinations.
- **Data Security**: Enhanced security measures to protect sensitive health information.

## Installation

### Flutter Project
1. **Clone the repository**:
    ```bash
    git clone https://github.com/JamesMungai254/PLP_FLUTTER_PYTHON.git
    ```
2. **Navigate to the project directory**:
    ```bash
    cd '/Flutter Project/vaccination-tracker'
    ```
3. **Install dependencies**:
    ```bash
    flutter pub get
    ```
4. **Run the app**:
    ```bash
    flutter run
    ```

### Python Django Project
1. **Clone the repository**:
    ```bash
    git clone https://github.com/JamesMungai254/PLP_FLUTTER_PYTHON.git
    ```
2. **Navigate to the project directory**:
    ```bash
    cd '/Python Project/vaccination-tracker'
    ```
3. **Create a virtual environment**:
    ```bash
    python -m venv venv
    ```
4. **Activate the virtual environment**:
    - On Windows:
        ```bash
        venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```bash
        source venv/bin/activate
        ```
5. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
6. **Apply migrations**:
    ```bash
    python manage.py migrate
    ```
7. **Run the server**:
    ```bash
    python manage.py runserver
    ```

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
