import serial

ser = serial.Serial(
    port='COM20',
    baudrate=9600,
)

while True:
    if ser.readable():
        res = ser.readline()
        print(res.decode()[:len(res)-1])
