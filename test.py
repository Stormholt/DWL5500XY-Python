
import serial
import tilt_sensor # import custom module.
import time


sc = tilt_sensor.TiltSensor()
try:
    sc.open_connection('COM5') # Open a connection to the sensor via usb.
except:
    try:
        sc.open_connection('/dev/ttyUSB1') # Open a connection to the sensor via usb.
    except:
        try:
            sc.open_connection('/dev/ttyUSB2') # Open a connection to the sensor via usb.
        except:
            print("ERROR: Could not open serial connection to tilt sensor")
            sc.conn = None

if sc.conn != None:
    sc.initialize_sensor()
    sc.set_mode(sc.DUAL_MODE)
   
    # print("tilt sensor init done ")
sc.set_mode(sc.DUAL_MODE)

i = 0

try:
    
    time.sleep(0.5)
   # sc.set_mode(sc.ALT_DUAL_MODE)
    #time.sleep(0.5)
    i = 0
    while True:
        #sc.set_mode(sc.ALT_DUAL_MODE)
        
        while i < 10:
            sc.read_response()
            i = i + 1
        i = 0
        print("Setting zero\n")
        sc.set_alternate_zero_dualaxis()
        while i < 10:
            sc.read_response()
            i = i + 1
        sc.reset_alternate_zero_dualaxis() 
        i = 0
        print("Resetting zero\n")    
        
        
        
    
        
        sc.conn.reset_output_buffer()
        sc.reset_alternate_zero_dualaxis()
        while i< 100:
            sc.conn.reset_input_buffer()
            sc.read_response()
            i = i+1
        print("Setting alt zero\n")
        sc.set_alternate_zero_dualaxis()
        i = 0

        while i < 100 :
            sc.conn.reset_input_buffer()
            sc.read_response()
            i = i+1
        print("Resetting alt zero\n")
        i = 0
except KeyboardInterrupt:
    print('Terminated!')
# try:
#     while True:
        
#         sc.set_mode(sc.VIBRO_MODE)
#         sc.conn.reset_input_buffer()
#         sc.conn.flushInput()
#         sc.read_response()
#       #  time.sleep(2)

#         sc.conn.reset_output_buffer()
#         sc.conn.flushOutput()
#         sc.set_mode(sc.DUAL_MODE)
#         sc.conn.reset_input_buffer()
#         sc.conn.flushInput()
#         sc.read_response()
#        # time.sleep(2)
#         sc.conn.reset_output_buffer()
#         sc.conn.flushOutput()

# except KeyboardInterrupt:
#     print('Terminated!')