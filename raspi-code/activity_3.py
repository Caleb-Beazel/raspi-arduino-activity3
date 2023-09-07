#receive and print the counter
#every 10 seconds, reset the counter
import serial
import time

ser = serial.Serial('/dev/ttyACM0', 115200, timeout = 1.0)
time.sleep(3)
ser.reset_input_buffer()
print("Serial OK")

last_reset = time.time()
reset_interval = 10

try:
    while True:
        time.sleep(0.01)
        
        time_now = time.time()
        
        if time_now - last_reset >= reset_interval:
            last_reset = time_now
            ser.write("reset\n".encode('utf-8'))
            print("Reset sent.")
            
        
        if ser.in_waiting > 0:
            count = int(ser.readline().decode('utf-8').rstrip())
            print(count)
                   
except KeyboardInterrupt:
    print("Disconnected from Arduino.")
    ser.close()
        