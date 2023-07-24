
# Internet Speed Test- Python Project

The Internet Speed Test Checker is a Python-based application that allows users to measure their internet connection's performance by evaluating ping time, download speed, and upload speed. The project utilizes the Tkinter library to create an interactive graphical user interface (GUI) for conducting the speed tests with ease.

## Requirements

- Python 3.x
- Tkinter library
- Speedtest-cli library (to perform speed tests)

## Installation

1. Ensure you have Python 3.x installed on your system.
2. Install the required libraries using pip:


pip install tkinter
pip install speedtest-cli

## Functionality

1. **Ping Test**: Click on the "Start Ping Test" button to measure the ping time of your internet connection. The ping time represents the time taken for a small data packet to travel from your device to a server and back. A low ping time indicates a more responsive and stable internet connection.

2. **Download Speed Test**: Click on the "Start Download Test" button to measure the download speed of your internet connection. The download speed measures how quickly data can be retrieved from the internet. This is essential for activities such as browsing, streaming, and downloading content online.

3. **Upload Speed Test**: Click on the "Start Upload Test" button to measure the upload speed of your internet connection. The upload speed represents the speed at which data can be sent from your device to a server. This metric is crucial for tasks like uploading files or participating in video conferences.

4. **Results**: Once each test is completed, the results will be displayed on the GUI. You can view the ping time, download speed, and upload speed values.

5. **Multiple Tests**: You can perform multiple speed tests as needed. Simply click on the corresponding buttons to re-run the tests.

## Benefits

- Provides an easy-to-use tool for users to assess their internet connection's performance.
- Enables users to identify potential issues such as slow download/upload speeds or high ping times.
- Facilitates making informed decisions about internet service providers and optimizing internet usage.

## Acknowledgments

- This project was made possible by the `tkinter` library for creating the GUI and `speedtest-cli` library for conducting speed tests.
