#Test script using most aspects of the DWL5500XY module.

import DWL5500XY # import custom module.


sc = DWL5500XY.TiltSensor()
try:
    sc.open_connection('COM5') # Open a connection to the sensor via usb. Windows exmaple
except:
    try:
        sc.open_connection('/dev/ttyUSB0') # Open a connection to the sensor via usb. Linux example
    except:
        print("ERROR: Could not open serial connection to tilt sensor")
        sc.conn = None

if sc.conn != None:
    sc.initialize_sensor()
    try:
        i = 0
        while True:
            print("Going into DUAL_MODE")
            sc.set_mode(sc.DUAL_MODE) 
            while i < 100:
                sc.read_response()
                i = i + 1
            i = 0

            print("Setting alternate zero for DUAL_MODE\n")
            sc.set_alternate_zero_dualaxis()
            while i < 100:
                sc.read_response()
                i = i + 1
            i = 0

            print("Resetting alternate zero ofr DUAL_MODE\n")    
            sc.reset_alternate_zero_dualaxis()
            while i< 10:
                sc.read_response()
                i = i+1
            i = 0

            print("Going into SINGLE_MODE")
            sc.set_mode(sc.SINGLE_MODE) 
            while i < 100:
                sc.read_response()
                i = i + 1
            i = 0

            print("Setting alternate zero for SINGLE_MODE\n")
            sc.set_alternate_zero_singleaxis()
            while i < 100:
                sc.read_response()
                i = i + 1
            i = 0

            print("Resetting alternate zero ofr SINGLE_MODE\n")    
            sc.reset_alternate_zero_singleaxis()
            while i< 10:
                sc.read_response()
                i = i+1
            i = 0

            print("Going into VIBRO_MODE")
            sc.set_mode(sc.VIBRO_MODE) 
            while i < 100:
                sc.read_response()
                i = i + 1
            i = 0
    except KeyboardInterrupt:
        print('Terminated!')
else:
    print("Enter correct device name in code")
 
