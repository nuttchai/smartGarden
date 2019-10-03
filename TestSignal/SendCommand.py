import serial

data = serial.Serial('/dev/ttyACM0', 115200)
while True:
    i = input("choose command: ").encode() #Arduino is ascii; however, python is unicode .encode is important for converting. 
    data.write(i)
    while True:
        if (data.in_waiting > 0):
            result = data.readline()
            print(result.strip())
            break
