#    images.py - takes 5 pictures 5 seconds apart and saves them all.
#    images named image0.jpg, image1.jpg, image2.jpg etc...

from picamera import PiCamera
from time import sleep
camera = PiCamera()
camera.start_preview(alpha=192)
for i in range(5):
    sleep(5)
    camera.capture("/home/pi/image{}.jpg".format(i))
camera.stop_preview()

#    CHALLENGE: Can You: 
#    Change the name of the image file?
#    Change the number of images taken?
#    Change the time between each image being taken?
#    Get a new "camera effect"
