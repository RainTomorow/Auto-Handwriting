# Auto-Handwriting
This program allows you to imitate your own handwriting with any possible text you want to input

_I do not endorse to use this code in order to cheat someone or any other harmful ways. Please use it only for fair reasons_

[Try on Google Colab](https://colab.research.google.com/drive/10SM8ma6M6hdBGbvzROk7FYdZee1qgy7m?usp=sharing)

To run the code you need three files

*First is input.txt which contains input text you want to generate
*Second is workbook.png which is a background where your handwritings will be pasted. Please make sure to set the image with a proper resolution, as the height of a one row is 100px.
*Third is a letters.zip which contains .png files of your letters. This archive should be prepaired considering the following convention:

1. Take a photo of your handwritings and remove the background with any photo editor you wish
2. Separe the letters and set their height 100px for uppercase and 150px for lowercase (this is made for letters like _y_ which usually take some place under the row
3. Naming convetion is (_l_ prefix in case of a lowercase letter)(letter)_(index).png . Index count starts at 1 and allows you to put a multiple versions of a letter so they are being picked randomly to make writings look more natural.
4. nextrow.png is a dash at the end of a line (150px height)

Here is a rough example of how it can work (I won`t post real example for privacy reasons)
![result_0](https://github.com/RainTomorow/Auto-Handwriting/assets/119802850/4cd4cdb5-715e-4d59-abef-c642e9ae49ff)
