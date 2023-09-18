import serial
import subprocess

ser = serial.Serial('COM6', 9600)  # Replace 'COM6' with your Arduino's COM port.

# Define the path to the application you want to open.
app_path = r'C:\MyApp.exe'  # Replace with the actual path.


# Define the IR code you want to trigger the action.
target_ir_code = '5F0C'



while True:
    # Read the data from the Arduino.
    arduino_data = ser.readline().strip().decode('utf-8')
    
    # Print the received data.
    print("Received data:", arduino_data)

    # Check if the received IR code matches the target code.
    if arduino_data == target_ir_code:
        # If the code matches, open the application using subprocess.
        subprocess.Popen(app_path, shell=True)
        print("Opening app")
