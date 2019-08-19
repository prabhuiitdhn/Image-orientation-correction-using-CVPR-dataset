
import os, sys
import Image
from PIL import Image
from resizeimage import resizeimage

def resizeImage(infile, output_dir=""):
     print (os.path.splitext(infile)[0])
     outfile = os.path.splitext(infile)[0]+"_resized"
     extension = os.path.splitext(infile)[1]

     if (cmp(extension, ".jpg")):
        return

     if infile != outfile:
        try :
            '''
            im = Image.open(infile)
            im.thumbnail(size, Image.ANTIALIAS)
            im.save(output_dir+outfile+extension,"JPEG")
            '''
            with open(infile, 'r+b') as f:
                with Image.open(f) as image:
                    cover = resizeimage.resize_cover(image, [64, 64])
                    cover.save(output_dir+outfile+extension, image.format)
        except IOError:
            print ("cannot reduce image for", infile)


if __name__=="__main__":
    output_dir ="resized"
    dir = os.getcwd()
    print (dir)
    '''
    if not os.path.exists(os.path.join(dir,output_dir)):
        os.mkdir(output_dir)
    '''
    #print (os.listdir(dir))
    for file in os.listdir(dir):
        resizeImage(file) 
        #resizeImage(file,output_dir)