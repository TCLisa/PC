#   selfie.py - takes a single picture after 5 seconds 
#   the next two lines create libraries to add special features (or abilities) to your project.  When you see the word FROM - you know you are checking out special features (or abilities) from the library.
from picamera import PiCamera
from time import sleep
#   The camera = PiCamera() line connects to the PiCamera and names that connection "camera".  This enables (or allows) you to use the camera functions.
#   Here are some of the fancy things your camear can do: camera.brightness = 70 / camera.sharpness = 0 / camera.contrast = 0 /  camera.brightness = 50
#   and more fancy things: camera.saturation = 0 / camera.rotation = 0 / camera.color_effects = None / camera.crop = (0.0, 0.0, 1.0, 1.0)
camera = PiCamera()
# These last for lines start an image in preview (which is transparent), pause, capture an image, and then stop the preview.
camera.start_preview(alpha=192)
sleep(5)
camera.capture("/home/pi/image.jpg")
camera.stop_preview()
