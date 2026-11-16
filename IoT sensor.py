import numpy as np 
n = int(input("Enter number of sensor readings: "))
readings = []
for i in range(n):
    value = float(input(f"Enter reading {i + 1}: "))
    readings.append(value)
sensor_data = np.array(readings)
print("Sensor Data:", sensor_data) 
print("Mean       :", round(np.mean(sensor_data), 2)) 
print("Median     :", round(np.median(sensor_data), 2)) 
print("Minimum    :", np.min(sensor_data)) 
print("Maximum    :", np.max(sensor_data)) 
print("Std. Dev.  :", round(np.std(sensor_data), 2)) 
threshold = 28.0 
high_values = sensor_data[sensor_data > threshold] 
print("Values above", threshold, ":", high_values) 