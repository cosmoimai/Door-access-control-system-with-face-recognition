# Door-access-control-system-with-face-recognition

## Requirements:-
<ul>
  <h3>Software Requirements</h3>
  <li>Arduino installed on your os <a href= "https://linoxide.com/how-to-install-arduino-ide-on-ubuntu-20-04/">Refer installation documents</a></li>
  <li>python</li>
  <li>C++</li>
  <li>VS Code</li>
</ul>
<ul>
  <h3>Python library required</h3>
  <li>Open Cv</li>
  <li>Pandas</li>
  <li>face_recognition</li>
  <li>numpy</li>
  <li>urllib.request</li>
</ul>
<ul>
  <h3>Hardware Requirements</h3>
  <li>ESP32 CAM WiFi Module Bluetooth with OV2640 Camera Module 2MP For Face Recognition</li>
  <li>FT232RL USB to TTL 3.3V 5.5V Serial Adapter Module</li>
  <li>Bread Board</li>
  <li>Arduino Uno</li>
  <li>Jumper wires</li>
  <li>Serial port USB cable 5V mini </li>
  <li>PCB Mounted Passive Buzzer Module</li>
  <li>2 Channel 5V Relay Module with Optocoupler</li>
  <li>Battery</li>
  <li>Electronic door lock 12V</li>
</ul>

### 1. Installing the ESP32 Board
<li>Open the preferences window from the Arduino IDE. Go to Arduino > Preferences</li>
<li>Enter <b>https://dl.espressif.com/dl/package_esp32_index.json</b> into the “Additional Board Manager URLs” field as shown in the figure below. Then, click the “OK” button:</li>
<li>Open boards manager. Go to Tools > Board > Boards Manager…</li>
<li>Search for ESP32 and press install button for the “ESP32 by Espressif Systems“:</li>
<li>That’s it. It should be installed after a few seconds:</li>

### 2. Testing the Installation
<li>Plug the ESP32 board to your computer</li>
<li>Open the Arduino IDE</li>
<li>Select your Board in Tools > Board menu (in my case it’s the DOIT ESP32 DEVKIT V1)</li>
<li>Select the Port (if you don’t see the COM Port in your Arduino IDE, you need to install the ESP32 CP210x USB to UART Bridge VCP Drivers):</li>
<li>Open the following example under File > Examples > WiFi (ESP32) > WiFi Scan</li>
<li>A new sketch opens:</li>
<li>Press the Upload button in the Arduino IDE. Wait a few seconds while the code compiles and uploads to your board.</li>
<li>If everything went as expected, you should see a “Done uploading.” message.</li>
<li>Open the Arduino IDE Serial Monitor at a baud rate of 115200:</li>
<li>Press the ESP32 on-board Enable button and you should see the networks available near your ESP32:</li>

### 3. Installing ESP32CAM Library
<li>Here we will not use the general ESP webserver example rather another streaming process. Therefore we need to add another ESPCAM library. The esp32cam library provides an object oriented API to use OV2640 camera on ESP32 microcontroller. It is a wrapper of esp32-camera library.</li>
<li>Go to the following <a href="https://github.com/yoursunny/esp32cam">Github</a> Link and download the zip library as in the image</li>
<li>Once downloaded add this zip library to Arduino Libray Folder. To do so follow the following steps:
Open Arduino -> Sketch -> Include Library -> Add .ZIP Library… -> Navigate to downloaded zip file -> add</li>
<li>Source Code/Program for ESP32 CAM Module</li>
<li>Here is a source code for Face Recognition Based Attendance System using ESP32 CAM & OpenCV. Copy the code and paste it in the Arduino IDE.</li>
<li>Before Uploading the code you have to make a small change to the code. Change the SSID and password variable and in accordance with your WiFi network.</li>
</li>
  <li>Now compile and upload it to the ESP32 CAM Board. But during uploading, you have to follow few steps every time.</li>
  <ul>
    <li>Make sure the IO0 pin is shorted with the ground when you have pressed the upload button.</li>
    <li>If you see the dots and dashes while uploading press the reset button immediately</li>
    <li>Once the code is uploaded, remove the I01 pin shorting with Ground and press the reset button once again.</li>
    <li>If the output is the Serial monitor is still not there then press the reset button again.</li>
  </ul>
</li>
<li>Now copy the IP address visible in the serial port monitor, we will be using it to edit the URL in python code</li>
<h2 href="https://visualstudio.microsoft.com/downloads/">Install visual stdio</h2>
