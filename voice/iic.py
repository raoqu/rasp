import smbus
DEVICE_BUS = 1
DEVICE_ADDR = 0x0f
bus = smbus.SMBus(DEVICE_BUS)
bus.write_byte_data(DEVICE_ADDR, 0x00, 0x01)
