import threading
import time

class TensionLoadCell:
    def __init__(self):
        self.load = 0.0
        self.lock = threading.Lock()

    def read(self):
        with self.lock:
            # Simulate reading from the load cell
            return self.load

    def set_load(self, load):
        with self.lock:
            self.load = load


class MotionSensor:
    def __init__(self):
        self.motion_detected = False
        self.lock = threading.Lock()

    def detect_motion(self):
        with self.lock:
            # Simulate motion detection logic
            return self.motion_detected

    def set_motion(self, detected):
        with self.lock:
            self.motion_detected = detected


class SensorAcquisitionSystem:
    def __init__(self, load_cell, motion_sensor):
        self.load_cell = load_cell
        self.motion_sensor = motion_sensor
        self.running = True
        self.lock = threading.Lock()

    def start_acquisition(self):
        while self.running:
            load = self.load_cell.read()
            motion = self.motion_sensor.detect_motion()
            self.process_sensor_data(load, motion)
            time.sleep(0.01)  # Sleep for 10 ms to achieve 100Hz sampling rate

    def process_sensor_data(self, load, motion):
        with self.lock:
            # Process the sensor data here
            print(f"Load: {load}, Motion Detected: {motion}")

    def stop_acquisition(self):
        self.running = False

# Instantiate sensors
load_cell = TensionLoadCell()
motion_sensor = MotionSensor()

# Create acquisition system
acquisition_system = SensorAcquisitionSystem(load_cell, motion_sensor)

# Start sensor acquisition in a separate thread
acquisition_thread = threading.Thread(target=acquisition_system.start_acquisition)
acquisition_thread.start()