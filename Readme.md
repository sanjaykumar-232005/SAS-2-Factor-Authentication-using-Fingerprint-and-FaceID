<!-- SAS (Secure Authentication System) - 2 Factor Authentication Project -->
## Overview
SAS (Secure Authentication System) is a project designed to enhance authentication mechanisms through the use of two-factor authentication (2FA) combining fingerprint data and face data. The project includes a graphical user interface (GUI) and stores data securely in a MySQL database.

## Key Features
* Two-Factor Authentication (2FA): Enhances security by requiring two forms of authentication - fingerprint and face data.
* Fingerprint and Face Data: Utilizes biometric data for authentication.
* Graphical User Interface (GUI): User-friendly interface built with Tkinter.
* Data Storage: Securely saves data in a MySQL database.

## Built With
* Programming Languages: Python, MySQL
* Libraries and Tools: Tkinter, CSV, NumPy, Hashlib, Dlib, CMake, Python Pillow

## Requirements
- Python
- MySQL Server
- [shape_predictor_68_face_landmarks.dat file](https://github.com/italojs/facial-landmarks-recognition/blob/d37b6a7426e98094e28fa99254e270a3e9b6d591/shape_predictor_68_face_landmarks.dat)
- Tkinter
- CSV
- NumPy
- Hashlib
- Dlib
- CMake
- Python Pillow
- Installation
- Clone the repository

## Installation

#### 1. Clone the repository:

   ```bash
git clone https://github.com/sanjaykumar-232005/SAS-2-Factor-Authentication-using-Fingerprint-and-FaceID.git
cd SAS-2-Factor-Authentication-using-Fingerprint-and-FaceID
```
#### 2. Install required Python packages
```bash
pip install -r requirements.txt
```
#### 3. Download the shape predictor file
Download the shape_predictor_68_face_landmarks.dat file from dlib's model repository and extract it into the project directory.

## Set up MySQL database
* Install MySQL server if not already installed.
* Create a new database for the project by simply running the Database Creator SAS.py file.
* Update the database configuration in the project files with your MySQL credentials.

## Usage
#### Run the application
```bash
python3 SAS 2FA.py
```

## Authentication Process

Register by providing fingerprint and face data.
Log in using the registered biometric data.

## Contributing
Contributions are welcome! Please fork the repository and create a pull request with your changes.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
