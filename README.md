# Pemanfaatan-Edge-AI-Untuk-Prediksi-Cuaca-Dalam-Pengelolaan-Pertanian
## Project Description
This Project Focuses on Implementing Artificial Intelligence with Edge Devices, Primarily Implementing it on Raspberry Pi 3 and using Sensors as an input.

## Problem Statement
1. Indonesia, as an agrarian country, relies heavily on the agricultural sector, especially for rural communities.

2. Agricultural productivity is often disrupted by weather uncertainties such as:
  - Unexpected rainfall,
  - Strong winds, and
  - Droughts.

3. These weather issues lead to significant losses, including:
  - Reduced harvest yields, and
  - Inefficient use of resources.

4. There is a critical need for an accurate and responsive weather prediction system

## Solution Statement
1. The proposed solution leverages Edge AI technology for weather prediction in agriculture.

2. Key capabilities of Edge AI:
  - Processes environmental data such as temperature, humidity, wind speed, cloud cover, and rainfall locally.
  - Provides real-time weather predictions directly on local devices.

3. Applications in agricultural management:
Optimizing irrigation:
  - Avoid water wastage by halting irrigation before rain.
  - Ensure sufficient water during hot weather conditions.

4. Enhances decision-making for farmers with timely and accurate weather information.
Impact:
  - Improves resource efficiency.
  - Reduces losses caused by unpredictable weather.
  - Boosts agricultural productivity and sustainability.

## Dataset
We used public dataset provided from kaggle in the link below:
- [Weather Classification Dataset - Kaggle] (https://www.kaggle.com/datasets/nikhil7280/weather-type-classification)

## Achitecture and Pinout Raspberry pi 3
### Pinout Raspberry pi 3
![pinout](https://github.com/user-attachments/assets/20b3236f-ca01-4671-9092-a7d183bafd76)

### Architecture Sistem
![Weather_predict_architecture_bb](https://github.com/user-attachments/assets/150d4512-954d-43fa-8cad-7183dfb82188)

The circuit above utilizes a Raspberry Pi 3 Model B as the central controller to read data from the sensor and display information on the LCD. The sensor used is the DHT11, which functions to measure air temperature and humidity. This sensor connects to the Raspberry Pi via three pins: the VCC pin (red) connects to the 5V pin on the Raspberry Pi for power, the GND pin (black) connects to the ground (GND), and the DATA pin (green) connects to GPIO4 (pin 7) for data transmission. Additionally, a 16x2 LCD module with an I2C interface (LCM1602) is used to display the data processed by the Raspberry Pi. This module connects through four wires: GND (black) to ground, VCC (red) to the 5V pin for power, SDA (yellow) to the SDA pin (GPIO2 or pin 3), and SCL (blue) to the SCL pin (GPIO3 or pin 5).

## Flowchart
![Edge-weather drawio](https://github.com/user-attachments/assets/f4d7e8db-9dac-466b-ac4b-759a57660c49)

The flowchart above explains the workflow of a weather prediction system using temperature and humidity data with an ANN (Artificial Neural Network) model. Here is a detailed explanation of each step in the flowchart:

1. **Start**  
   The process begins by running the weather prediction system.

2. **Input: Temperature and Humidity Data**  
   The system receives input in the form of temperature and humidity data. This data can be sourced from a DHT11 sensor connected to the Raspberry Pi.

3. **Weather Prediction Using ANN Model**  
   Temperature and humidity data are processed using a weather prediction model based on an ANN (Artificial Neural Network). The result is a prediction of whether the weather will be rainy or clear.

4. **Is the Weather Rainy?**  
   The system evaluates the prediction results:
   - If the weather is predicted to be rainy, the `is_raining` value is set to 1, and the rain data (`rain_data`) is updated.
   - If the weather is predicted to be clear, the `is_raining` value is set to 0, and the `rain_data` is updated accordingly.

5. **Are There More Than 2 Rain Data Points in the Last 8 Hours?**  
   The system checks the number of rain data points recorded in the last 8 hours:
   - If there are more than 2 rain data points, watering is not required. The system will display the symbol **"W"** (watering not needed) on the LCD.
   - If there are 2 or fewer rain data points, watering is needed. The system will display the symbol **"X"** on the LCD.

6. **Display Data on the LCD**  
   The system displays the following information on the LCD:
   - Temperature
   - Humidity
   - Weather prediction (rainy or clear)
   - Recorded rain data.

7. **End**  
   After all the data is displayed, the process is completed, and the system is ready for the next iteration.

## Output 
![output](https://github.com/user-attachments/assets/6077de78-c309-438c-8a03-73d669400f10)

The image above represents an example of the LCD output from the weather detection system that was built. The detailed explanation regarding the system's output is as follows:

1. On the **first line** of the LCD, data such as temperature, humidity, and decision-making based on the collected data are displayed. In the decision-making section, the system will display an **"X"** if it determines that no watering is needed within the next 8 hours. However, if a water drop icon is shown, it indicates that watering is required within the next 8 hours.

2. On the **second line** of the LCD, the weather prediction from the previously trained model is displayed, followed by the number of rain occurrences within the last 24 hours, and finally, the time at which the data was collected from the DHT11 sensor.
