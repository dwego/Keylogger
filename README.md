# Keylogger
This is a simple keylogger program written in Python. It captures keystrokes and saves them to a log file, which can be periodically emailed to a specified email address.

# Requirements
The following libraries are required to run this program:

- pythoncom
- smtplib
- pyHook
- win32api
You can install these libraries using pip:

```python
pip install pythoncom smtplib pyHook pypiwin32
```
# Usage
To use this program, follow these steps:

- Set the login and password variables to your email login credentials.
- Run the program with Python.
- The program will start logging keystrokes.
- To stop the program, press the Escape key.
- The program will email the log file to the specified email address every 6 hours.
# License
This program is licensed under the MIT License. Feel free to modify and distribute it as you wish. However, I am not responsible for any damages caused by the use of this program. Use at your own risk.
