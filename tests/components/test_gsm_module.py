import serial

def test_at_command():
    port = serial.Serial('/dev/ttyAMA0', baudrate=9600, timeout=1)
    mesg = 'AT\r\n'.encode('utf-8')
    port.write(mesg)
    resp = port.read(10)
    resp = resp.decode("utf-8")
    OK = 'OK'
    OK_in_resp = resp.find(OK)
    assert OK_in_resp != -1
