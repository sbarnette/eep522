#!/usr/bin/env python3

import time

from gpiozero import Button, LED, PWMLED

import graph, plotter, camera


red = LED(21)
yellow = PWMLED(20)
green = LED(16)

shutter = Button(25)

tilt = Button(12)


# Status light shortcuts.
def status_ready():
    red.off()
    yellow.off()
    green.on()

def status_complete():
    green.off()
    yellow.off()
    red.on()

def status_processing():
    green.off()
    red.off()
    yellow.on()

def status_drawing():
    green.off()
    red.off()
    yellow.pulse()
    


def main():
    while True:
                
        ##status_complete()

        # Wait for flip & shake.
        ##tilt.wait_for_press()
        ##time.sleep(1)

        # Setup the camera interface.
        camera.prepare()
        print("Camera ready")
        ##status_ready()
        
        # Wait for shutter, then take picture.
        shutter.wait_for_press()
        print("Shutter pressed")
        ##status_processing()
        image = camera.take_photo()
        print("Photo taken")
        #image.save("raw-photo-%s.jpg" % (int(time.time())))
        ##print("loop entered")
        ##image = camera.process_image("circle.jpg")
        image = camera.process_image(image)
        #image.save("processed-photo-%s.jpg" % (int(time.time())))
        print("Image processed")

        # Process the image & generate plotter moves.
        moves = graph.generate_moves(image)
        print("moves generated")
        
        # Draw the paths.
        ##status_drawing()
        plotter.enqueue(moves)
        print("drawing complete")
        
        # Complete.
        #remove this break after testing
        break
    

    
if __name__ == "__main__":
    main()