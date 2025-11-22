# Posterize

In this problem set you will be implementing a program that takes an image and a number of colors and returns a new image that has been posterized. Posterization is a technique used to reduce the number of colors in an image. The result is an image with a limited number of colors that can be used to create a cartoon-like effect.

One of the decisions when posterizing an image is what colors should the image be reduced to? To determine the colors that will be used for posterization, we will be using the k-means algorithm to cluster the colors in an image. The k-means algorithm will take the colors in the image and group them into k clusters. After the algorithm has run, we will use the average color of each cluster (the centroids of each cluster) as the colors that will be used for posterization. The actual k-means code is provided from the book (CCSPiP Chapter 6). I have modified the code to not use z-scores, since RGB colors are all on an equal scale anyway.

To posterize, we will use a technique called quantization. Quantization involves taking a palette (the k colors), and comparing each pixel in the image to the colors in the palette. The color in the palette that is closest to the pixel color will be used as the color for the pixel in the posterized image. To find the closest color, multiple techniques can be used, including euclidean distance. You can write your own quantization code or use the `quantize()` method from the `Pillow` library's `Image` module.

## Steps

1. Install the Pillow library (`pip3 install Pillow` or `pip install Pillow`)
2. Write a function that will convert the pixels in the image to a list of `DataPoint`s. The function should return a list of colors where each color becomes a `DataPoint` composed of three values (RGB). Be sure to only call this function with a thumbnail of the original image, because otherwise k-means will be too slow (too many data points). You will likely need to look at the [Pillow documentation](https://pillow.readthedocs.io/en/stable/index.html) to understand how to get the pixels from an image (code for creating the thumbnail is provided).
3. Write a function that will take a list of `DataPoint`s and a number of clusters and return a list of `Cluster`s. The function should use the k-means code from the book to cluster the colors. Remember, each `Cluster` has an embedded centroid.
4. Write a function that will take an image and a list of centroids (these are just `DataPoints`s) to return a quantized version of the image using the centroids as the palette. You can use the [`quantize()`](https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.quantize) method from the `Pillow` library's `Image` module, or you can write your own quantization code by comparing each pixel to the centroids. If you use `quantize()`, make sure to turn off dithering (`Image.Dither.NONE`). You can find examples of how to use it on the Web.
5. Put together the above three functions along with the provided code (number of colors, opening the initial image, saving/showing the final image) to create a program that will posterize an image. Make sure to quantize the original image, not the thumbnail you used for k-means. Please use NUM_COLORS = 7 for your posterized images.
6. Include your posterized sunflowers image in your repository (`sunflowers_quantized.png`). There is an example, so you can see if you're on the right track. Remember, k-means includes some randomness, so your image may not look exactly like the example.

## Hints
- You do not need to write much code for this problem set. For example, my solution is only 20 lines of additional code.
- Make sure you have read CCSPiP Chapter 6 before you begin. It explains how to use the provided code. z-score normalization is commented out in the provided code, because we don't need it.
- Make sure you checkout the Pillow library's documentation and feel free to do a Web search for some examples of how to use it for what you need. Just cite any sources you copy code from.
- This problem set is much more about learning to use a valuable library (Pillow) and showing some understanding of what k-means is doing than it is about writing a lot of code. You should be able to complete this problem set fairly quickly if you did the reading and understand what k-means is doing.

## Rules

1. You must use the provided k-means code. Do not write your own or use a library.
2. The only allowed libraries are Pillow and the standard library.
3. This is an individual assignment. You can discuss it with anyone you would like. Do not look at their code or copy their code. Please cite GitHub Copilot where appropriate.

## Setup

1. Create your own **private** repository from this repo by hitting the "Use this template" button at the top of the page
2. Add me (@davecom) as a collaborator on your **private** repository.
3. Make sure the assignment is trivial to run for me. I should be able to run `python ps8.py` and it should run your code and show your final image output.
4. Submit the link to your private repository on Canvas.

## Grading

You will receive full credit on this problem set if you successfully posterize the sunflowers image using k-means to select the colors while following the rules above. I will holistically provide partial credit if you do not succeed but wrote some working code. Submissions that do not run or crash with an exception will receive no credit. Plagiarism will result in a 0 for the assignment.

## Note on Repository Access

This repository should stay private. If you make it public, you are possibly providing your solution to other students taking the class. Generally the problem sets in this class are not great portfolio projects because they are too small, or contain a significant portion of code that is not your own and therefore do not demonstrate your skill. Please keep your repository private so other students can't use your solution.