Generate Images!
====

This is a super simple utility to generate images that follow specific patterns for testing use in computer vision projects. 

How to Use It.
====
Clone the repo locally. 
Open the generate_images.py file and change the `twoPowers` param to update the number of images being generated. Uncomment the type of image that you want to be generated (`horizontalStripeData`, `verticalStripeData`, `checkeredData`, or `xdata`). Then run `make`. The images you have generated will be placed in the image folder inside this repo. Move these images to your image folder by running `mv images <your image folder>` from within this repo. 