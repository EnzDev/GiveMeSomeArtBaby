Give Me Some Art Baby
=====================

This repository is a Mathematical Python Art project.  
My aim was to make some generated *art* with as little math as possible  

It was build to run with PyPy (Python 3) allowing better performance for massive generation and very high quality rendering (Like 2^15 pixel square).

I also built a Twitter Bot [@GiveMeSomeArts](https://twitter.com/GiveMeSomeArts) and an [Angular WebSite](http://givemesomeartbaby.ml/) (with automatic generation).

It uses Pillow to draw on the image and that's it!   
Operators can easily be added to the Renderer by creating the class in the Operators module and importing it into Art.py and adding it at line 28.

Just run `main.py` to create a picture of 256x256 pixels.  
Two files will be created, a text file with the exact seed (and the size on the last line) and the picture itself.
