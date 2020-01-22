from microbit import display, Image, sleep

while True:
    display.show(Image.HAPPY)
    sleep(1000)
    display.scroll('Test')
    sleep(1000)
