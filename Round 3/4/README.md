Place your Python code into a file named **digitmatch.py**.

The [scikit-learn library homepages](http://scikit-learn.org/) provide several tutorial style examples about different features of the library. One example concerns [recognizing hand-written digits](http://scikit-learn.org/stable/auto_examples/classification/plot_digits_classification.html) by using a support vector machine. The library also provides some data for testing purposes; in this particular example a collection of digitized images created from hand-written digits together with information about which digit (= numbers between 0-9) each image corresponds to. In the test data, each digitized digit is represented by a 8x8 grayscale image (simply an 8x8 integer array), where each pixel has a value between 0 and 16\. The process of recognizing (that is, classifying) digits consists of the following steps (also see the code provided in the scikit-learn example):

*   Initialize a support vector machice -based classifier: **classifier = svm.SVC(gamma=0.001)**.
    *   **gamma** is a parameter affecting how the support vector machine works. You may use the same value 0.001 as in the example.
*   Train the classifier with training data and the correct labels: **classifier.fit(traindata, labels)**.
    *   **traindata** is a list of training data items, where each data item should be represented as a one-dimensional array/list.
        *   In the example each 8x8 image is transformed into a one dimensional list of size 64.
    *   **labels** is a list whose length should be equal to the length of the **traindata** list and where the value **labels[i]** tells the correct class for the data item **traindata[i]**.
*   Predict (classify) one or more previously unknown data items: **classifier.predict(data)**.
    *   **data** is a list of items that we wish to classify.
        *   The items have to be in same form as in **traindata** (in this particular example each data item is a list of 64 values that represents a 8x8 image).
    *   The function returns a list with same length as **data** whose value at index **i** tells the class into which the classifier classified the data item **data[i]**.

The scikit-learn example code uses the first half of the provided test data set for training and the second half for testing the performance of the classifier: how correctly are the items in the second half classified when the classifier has been trained with the items in the first half.

In this question your task is to use the method tested in the above described scikit-learn example to recognize digits that have been written by hand by the course instructor. These hand-written digits were photographed with a smartphone and saved into individual images in PNG format. The images are available for download in the folder **digits/**. One example image is shown below:

As discussed above, the eventual classification is straightforward once the data has been preprocessed into a suitable form. The main part of this question thus concerns how to transform a fairly high-resolution image into a similar format as what the scikit-learn example uses. You may achieve this for example as follows:

1.  Load the PNG image by using the [Pillow (PIL) library](http://pillow.readthedocs.io/en/3.4.x/index.html).
2.  Isolate the digit from the image background (and transform the image to black and white).
    *   The original image uses RGB colors: each pixel is represented by a tuple **(r, g, b)**, where **r**, **g** and **b** are integers between 0..255\. The first corresponds to red, the second to green, and the third to blue.
    *   Since the digits are written in a blueish color and the background is somewhat gray, the following procedure works well: change each pixel to black (= a tuple **(0, 0, 0)**), if the condition **(r + 15 <= b) and (g + 15 <= b)** holds. Otherwise set the pixel to white, that is, to a tuple **(255, 255, 255)**.
        *   How can you modify the pixels? Get a handle to the pixel data e.g. by **pix = img.load()**, where **img** is the original image object. Then you can modify (both read and write) the pixels of **img** through **pix**: the notation **pix[i][j]** refers directly to the pixel of **img** whose coordinates are **i** and **j**. Modifications to **pix** will directly affect **img**.
3.  Remove extra white space from around the digit (crop the image) and ensure that the image dimensions correspond to a square (equal width and height).
    *   Cropping: When you turn pixels to black or white in step 2, record the smallest and largest **x**- and **y** -indices where a black pixel exists.
        *   If these indices are **minX**, **maxX**, **minY** and **maxY**, then the image can be cropped to have the upper left corner **(minX, minY)** and lower right corner **(maxX, maxY)**.
            *   Note that the **x**-indices grow from left to right and the **y**-indices from up to down.
            *   See [the Image library documentation](http://pillow.readthedocs.io/en/3.4.x/reference/Image.html) for the function **crop**.
    *   Making the image square-shaped: create a new square-shaped image where each pixel is white and whose width and height are equal to the maximum of the width and height of the cropped image. Then paste the cropped image into the new image in a centered manner (e.g. if the cropped image is tall and slim, paste the image into the square-shaped image in such manner that equal amount of white space is left to its left and right sides).
4.  Resize the image to 16x16 pixels, convert it to a grayscale image (use [the mode 'L'](http://pillow.readthedocs.io/en/3.4.x/handbook/concepts.html#concept-modes)), and filter it with a filter **ImageFilter.Kernel((3,3), [0.0625, 0.125, 0.0625, 0.125, 0.25, 0.125, 0.0625, 0.125, 0.0625])**.
    *   After converting to grayscale, each pixel is now represented by a single integer between 0..255.
    *   How to resize, convert and filter? See [the Image library documentation](http://pillow.readthedocs.io/en/3.4.x/reference/Image.html) for functions **resize**, **convert** and **filter**.
5.  Create a new 8x8 two-dimensional list where the value **[j,i]** is given the average value of the four pixels **[2*i,2*j]**, **[2*i+1, 2*j]**, **[2*i, 2*j+1]** and **[2*i+1, 2*j+1]** of the image created in step 4.
    *   <span style="text-decoration: underline;">Note the index ordering</span>: the indices **[j,i]** in the new image (now represented by a two-dimensinal list) are <span style="text-decoration: underline;">reversed</span>. This is because the scikit-learn data set uses a different pixel order than normal PNG images.
6.  Transform the pixel values in the image (two-dimensional list) from step 5 to be between 0..16, where 0 means white and 16 means black.
    *   Note: in the original image 0 means black and 255 means white.
    *   This transformation is achieved by setting new pixel value = (256 - old pixel value)/16\. Modify the pixels in similar manner as in step 2.
7.  As a last step, convert the 8x8 image from step 6 into a one dimensional list of 8*8 = 64 values: create an empty list and first add to it the 8 pixel values from the first row of the image, then the 8 values from the second row, and so on for all 8 rows.

The image resulting from step 6 should be in more or less same format as the original test data in the scikit-learn hand-written digit recognizing example, and the flattened list format from step 7 is similar to what the example eventually feeds to the classifier (in the scikit example, a **reshape** call flattens the images). After this you may train the classifier with the images provided in the scikit example as **digits.images**. Use the whole set and not only half as in the example. After training, try to classify the result from step 7 by feeding it to the **predict**-function. Repeat this process for each of the supplied high-resolution hand-written digit images. Your program should output the predictions for each of the 10 input images. It may happen that your program does not necessarily recognize all 10 digits correctly. But you should try to get at least 8 correct answers.