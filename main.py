from PIL import Image

#ASCI IMAGES

ASCII_CHARACTER=["@","#","S","%","?","*","+",";",":",",","."]

#resize images height and width

def resize(image,new_width=25):
    height,width = image.size
    ratio = width / height
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width,new_height))
    return(resized_image)

#convert to grey colours
def grecolour(image):
    greyscale_image=image.convert("L")
    return(greyscale_image)

#convert pixels to ascii
def pixel_ascii(image):
    pixels=image.getdata()
    character=''
    for pixel in pixels:
        temp=pixel//25
        character+="".join(ASCII_CHARACTER[temp])
    return character


#open the image file

def main(new_width=25):
    path=input("Enter path to the image file:\n")
    try:
        image = Image.open(path)
        # print(image)
    except:
        print("Error opening the image file")

    new_image=pixel_ascii(grecolour(resize(image)))
    pixel_count=len(new_image)
    ascii_image="\n".join(new_image[i:(i+new_width)] for i in range(0,pixel_count,new_width))
    print(ascii_image)



#run the main program
if __name__ == "__main__":
    main()
