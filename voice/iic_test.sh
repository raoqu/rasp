#!/bin/sh
i2cdetect -y 1
echo 
echo Read IIC:
i2cget -y 1 0x0f 0x00