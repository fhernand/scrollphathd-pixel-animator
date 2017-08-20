# scrollphathd-pixel-animator
*Animate [Pimoroni scrollphat HD](https://github.com/pimoroni/scroll-phat-hd) LED matrix using python*

These example scripts show how an array of several frames of matrix brightness values are used to display animations, such as this [candle animation]().

## 1. How to generate the array files

Unfortunately, this project is not as powerful as its name suggests. Quite some manual work maybe needed to animate your own videos. But I hope that these steps help you to do it. To generate these arrays you can use [ASCII-Video](https://github.com/fossage/ASCII-Video). That project allows you to take a video and render it as ASCII characters, in our case as brightness values to control the LED brightness of the scrollphat matrix. Important, before generating the output file you need to:

- edit the contained ImageToAscii command to apply a pixel array with numbers so that scrollphat can render them as values
- disable the coloration to generate just the brightness values
```
imageToAscii(tmpDirPath + files[idx], {
      pixels = [],
      colored = false,
      image_type: 'jpg'
    }
```
instead of:
```
imageToAscii(tmpDirPath + files[idx], {
      image_type: 'jpg'
    }
```
Then you can take the output file and use it for the python script

## 2. How to use them to display the animation

Take a look at one of the provided examples, and adapt it to use your output file. You need to take care that the Array indexes remain in the allowed range, and that the scrollphat set_pixel command accesses pixels that exist.

## 3. Things to consider

- The input video should have a reasonable number of frames. You can clip the video to the required number of frames by using VLC, for example
- The input video should have a reasonable size to fit in the LED matrix. You can use an online tool to crop your video such as [this](https://ezgif.com/crop-video) one
- By resizing the command line window of ASCII-Video you can affect the size of the generated array, so try to tweak the window size so that the resulting array size corresponds to the size of the LED matrix (17x7 pixels).
