from petcam import *


petcam = Petcam()

def displayLcd():
    while True:
        petcam.display()
        sleep(0.5)

def detectBtnClick():
    while True:
        button.wait_for_press()
        button.wait_for_release()
        petcam.toggle()


th1 = Thread(target=displayLcd, daemon=True)
th2 = Thread(target=detectBtnClick, daemon=True)

th1.start()
th2.start()

th1.join()