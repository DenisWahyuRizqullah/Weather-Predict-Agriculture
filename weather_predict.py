import time
import board
import adafruit_dht
import RPi.GPIO as GPIO
import I2C_LCD_driver
import numpy as np
import tensorflow as tf

class WeatherMonitor:
    def __init__(self, model_path='weather_model.tflite'):
        # GPIO setup
        GPIO.setmode(GPIO.BCM)
        
        # Sensor Configuration
        self.dht_sensor = adafruit_dht.DHT11(board.D4)  # GPIO 4
        self.sensor_read_attempts = 5  # Number of attempts to read sensor
        
        # LCD Configuration
        self.lcd = I2C_LCD_driver.lcd()
        
        # Load TensorFlow Lite model
        self.interpreter = tf.lite.Interpreter(model_path=model_path)
        self.interpreter.allocate_tensors()
        
        # Rain data tracking
        self.rain_data = [0] * 24
        self.rain_data_index = 0
        self.rain_count = 0
        
        # Time simulation variables
        self.current_hour = 0
        self.time_format = ["AM", "PM"]
        
        # Watering variables
        self.last_watering_hour = -6
        self.watering_interval = 6
        self.watering_needed = 0
    
    def get_sensor_data(self):
        """
        Read temperature and humidity directly from DHT11 sensor
        with error handling and multiple read attempts
        """
        for _ in range(self.sensor_read_attempts):
            try:
                # Attempt to read from DHT11 sensor
                humidity = self.dht_sensor.humidity
                temperature = self.dht_sensor.temperature
                
                # Validate sensor readings
                if humidity is not None and temperature is not None:
                    # Check if readings are within reasonable ranges
                    if 0 <= temperature <= 50 and 0 <= humidity <= 100:
                        return humidity, temperature
                
                # If reading is invalid, wait and try again
                print("Invalid sensor reading. Retrying...")
                time.sleep(2)
            
            except RuntimeError as error:
                # Handle specific DHT sensor errors
                print(f"DHT11 Sensor Error: {error}")
                print("Attempting to read again...")
                time.sleep(2)
            
            except Exception as error:
                # Catch any unexpected errors
                print(f"Unexpected error reading sensor: {error}")
                time.sleep(2)
        
        # If all attempts fail, log error and return None
        print("Failed to read from DHT11 sensor after multiple attempts")
        self.lcd.lcd_display_string("Sensor Error!", 1)
        return None, None

    def predict_weather(self, humidity, temperature):
        """Predict weather using TensorFlow Lite model"""
        # Fixed values for additional features
        atmospheric_pressure = 1013  # Standard atmospheric pressure
        uv_index = 5                # Example UV index
        season = 1                  # Summer season
        
        # Prepare input data for the model
        input_data = np.array([[temperature, humidity, atmospheric_pressure, uv_index, season]], dtype=np.float32)
        
        # Set input tensor
        input_details = self.interpreter.get_input_details()
        self.interpreter.set_tensor(input_details[0]['index'], input_data)
        
        # Run inference
        self.interpreter.invoke()
        
        # Get output tensor
        output_details = self.interpreter.get_output_details()
        prediction = self.interpreter.get_tensor(output_details[0]['index'])
        
        # Interpret prediction (adjust threshold as needed)
        return 'Hujan' if prediction[0][0] > 0.5 else 'Cerah'
    
    def run(self):
        """Main monitoring and display loop"""
        while True:
            # Get sensor data
            humidity, temperature = self.get_sensor_data()
            
            if humidity is not None and temperature is not None:
                # Predict weather condition using TensorFlow Lite model
                weather_condition = self.predict_weather(humidity, temperature)
                
                # Determine if it's raining
                is_raining = 1 if weather_condition == "Hujan" else 0
                
                # Update rain data
                self.rain_data[self.rain_data_index] = is_raining
                
                # Calculate total rain count
                self.rain_count = sum(self.rain_data)
                
                # Check watering needs
                if (self.current_hour - self.last_watering_hour >= self.watering_interval or 
                    self.current_hour + 24 - self.last_watering_hour >= self.watering_interval):
                    self.watering_needed = self.check_watering_need()
                    
                    if self.watering_needed:
                        self.last_watering_hour = self.current_hour
                        print("Penyiraman dilakukan!")
                
                # Display on LCD
                lcd_line1 = f"{temperature:.1f}C {humidity:.1f}% {'W' if self.watering_needed else 'X'}"
                lcd_line2 = f"{weather_condition} ({self.rain_count}x) {self.format_hour(self.current_hour)}"
                
                self.lcd.lcd_display_string(lcd_line1, 1)
                self.lcd.lcd_display_string(lcd_line2, 2)
                
                # Print to console for debugging
                print(f"Temperature: {temperature:.1f}°C")
                print(f"Humidity: {humidity:.1f}%")
                print(f"Weather: {weather_condition}")
                print(f"Watering Needed: {'Yes' if self.watering_needed else 'No'}")
                print("----------------------------")
            
            # Update indices
            self.rain_data_index = (self.rain_data_index + 1) % 24
            self.current_hour = (self.current_hour + 1) % 24
            
            # Wait to simulate 1-hour interval
            time.sleep(2)

def main():
    try:
        # Specify the path to your TensorFlow Lite model
        model_path = 'weather_model.tflite'
        weather_monitor = WeatherMonitor(model_path)
        weather_monitor.run()
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")
    finally:
        # Cleanup GPIO 
        GPIO.cleanup()

if __name__ == "__main__":
    main()