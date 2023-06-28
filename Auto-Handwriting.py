from PIL import Image, ImageOps
from random import randint
import zipfile
import io

def paste_images(input_txt, letters_zip, workbook_png):
    with open(input_txt, 'r', encoding='utf-8') as f:
        text = f.read()
    #in px
    #number of rows on a sheet
    nrows=20
    #row start offset between
    rowoff1=10
    rowoff2=20
    #intend offset between
    intoff1=100
    intoff2=150 
    #space between
    spc1=40
    spc2=50
    #max space to the end of the row for intend
    spsleft=125
    #uppercase letter height
    upper=100
    #lowercase letter height
    lower=150
    
    with zipfile.ZipFile(letters_zip, 'r') as zip:
        zip_files = zip.namelist()

    bg = Image.open(workbook_png)
    bg_width, bg_height = bg.size


    x_offset = randint(intoff1, intoff2)
    y_offset = 0
    row_height = 100
    row_number = 0
    space_width = randint(spc1, spc2)
    result_index = 0


    for char in text:
        if char == '\n':
            x_offset = randint(intoff1, intoff1)
            y_offset += row_height
            row_number += 1
        elif char == ' ':
            x_offset += space_width
            if bg_width - x_offset < spsleft:
                x_offset = randint(rowoff1, rowoff2)
                y_offset += row_height
                row_number += 1
        else:
            if char.islower():
                images = [f for f in zip_files if f.startswith('l' + char + '_') and f.endswith('.png')]
            else:
                images = [f for f in zip_files if f.startswith(char + '_') and f.endswith('.png')]
            if images:
                image_name = images[randint(0, len(images) - 1)]
                with zipfile.ZipFile(letters_zip, 'r') as zip:
                    with zip.open(image_name) as f:
                        letter_img = Image.open(io.BytesIO(f.read()))
                letter_width, letter_height = letter_img.size

                if letter_width > bg_width - x_offset:
                    with zipfile.ZipFile(letters_zip, 'r') as zip:
                        with zip.open('nextrow.png') as f:
                            nextrow_img = Image.open(io.BytesIO(f.read()))
                    bg.paste(nextrow_img, (x_offset, y_offset), nextrow_img)
                    x_offset = randint(rowoff1, rowoff2)
                    y_offset += row_height
                    row_number += 1

                if row_number >= nrows:
                    result_name = f'result_{result_index}.png'
                    bg.save(result_name)
                    result_index += 1
                    workbook_name = f'workbook{result_index}.png'
                    bg = Image.open(workbook_name)
                    x_offset = randint(intoff1, intoff2)
                    y_offset = 0
                    row_number = 0

                if char.isupper():
                    letter_img = letter_img.resize((letter_width, upper), resample=Image.Resampling.LANCZOS)
                    bg.paste(letter_img, (x_offset, y_offset + (row_height - upper) // 2), letter_img)
                else:
                    letter_img = letter_img.resize((letter_width, lower), resample=Image.Resampling.LANCZOS)
                    bg.paste(letter_img, (x_offset, y_offset + row_height - lower + int(lower/3)), letter_img)
                x_offset += letter_width

    result_name = f'result_{result_index}.png'
    bg.save(result_name)

paste_images('input.txt', 'letters.zip', 'workbook.png')
