from util import *


class Petcam:
    def __init__(self):
        self.state = 0
        self.wait()

    def off(self):
        if self.state == 2:
            offCamera()

        self.state = 0
        GPIO.output(led_yellow, False)
        GPIO.output(led_red, False)

    def wait(self):
        if self.state == 2:
            offCamera()

        self.state = 1
        GPIO.output(led_yellow, True)
        GPIO.output(led_red, False)
        Thread(target=self.detectMotion, daemon=True).start()

    def on(self):
        if self.state == 0:
            return

        self.state = 2
        GPIO.output(led_yellow, False)
        GPIO.output(led_red, True)
        onCamera()
        Thread(target=self.detectLeave, daemon=True).start()

    def toggle(self):
        if self.state == 0:
            self.wait()
        else:
            self.off()

    def display(self):
        if self.state == 2:
            lcd.lcd_display_string(curRecordTimeStr(), 1)
            lcd.lcd_display_string(curDistanceStr(), 2)
        else:
            lcd.lcd_display_string(curTimeStr(), 1)
            lcd.lcd_display_string(curDhtStr(), 2)

    def detectMotion(self):
        while self.state == 1 and GPIO.input(pir) == 0:
            sleep(0.2)
        if self.state == 1:
            self.on()

    def detectLeave(self):
        prev = False
        cnt = 0
        while self.state == 2 and cnt < 10:
            if distance() > 30:
                if not prev:
                    cnt = 0
                cnt += 1
                prev = True
            else:
                prev = False
            sleep(0.3)
        if self.state == 2:
            self.wait()