from setting import *


recordStartTime = 0

def distance():
    GPIO.output(ultra_trig, True)
    sleep(0.00001)
    GPIO.output(ultra_trig, False)

    while GPIO.input(ultra_echo) == 0:
        pass
    startTime = time()
    while GPIO.input(ultra_echo) == 1:
        pass

    dist = (time() - startTime) * 17150
    return dist

def onCamera():
    camera.start_preview()
    camera.start_recording('/home/pi/Desktop/record/video-' + curTimeStr() + '.h264')
    global recordStartTime
    recordStartTime = time()

def offCamera():
    camera.stop_recording()
    camera.stop_preview()

def curRecordTimeStr():
    recordTime = int(time() - recordStartTime)
    hour = recordTime // 3600
    minute = recordTime // 60 % 60
    second = recordTime % 60
    return "    {:02d}:{:02d}:{:02d}    ".format(hour, minute, second)

def curDistanceStr():
    return " dist:{:>7.2f}cm ".format(distance())

def curTimeStr():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def curDhtStr():
    while True:
        try:
            return "  {:.1f}{}C / {}%  ".format(dht.temperature, chr(223), dht.humidity)
        except:
            sleep(0.2)