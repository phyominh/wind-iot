import serial

def test_at_command():
    """
    AT Command to check the connection between Raspberry Pi and GSM module
    If the connection is successful, the response will contain 'OK' string.
    .............
    Pin out guide
    =============
      * Raspberry Pi, Pin 8 (TXD) -> GSM Module, RX
      * Raspberry Pi, Pin 10 (RXD) -> GSM Module, TX
      * Raspberry Pi, Ground -> GSM Module, Ground
    """
    port = serial.Serial('/dev/ttyAMA0', baudrate=9600, timeout=1)
    mesg = 'AT\r\n'.encode('utf-8')
    port.write(mesg)
    resp = port.read(10)
    resp = resp.decode("utf-8")
    OK = 'OK'
    OK_in_resp = resp.find(OK)
    assert OK_in_resp != -1
