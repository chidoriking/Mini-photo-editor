from urllib import request
from urllib import error
import urllib
from PIL import Image
try:
    # IMAGE DOWNLOAD FUNCTION
    def image(url, type, imagename):

        fullname = imagename+type

        urllib.request.urlretrieve(url, fullname)

        print("Image will be found after exiting the program :)".center(150, '='))

    # FILE DOWNLOAD FUNCTION
    def file(url, type, filename):

        receiver = request.urlopen(url)

        content = receiver.readlines()

        fullname = filename+type

        with open(fullname, 'wb') as f:

            f.writelines(content)

        print("File will be found after exiting the program :)".center(150, '='))

    # DOWNLOAD SECTION2
    def fn(n):
        if n == 1:

            imagename = input("\nEnter name of image:\n")

            url = input("\nPaste the url of the image from website which allows access:\n")

            type = input("\nEnter .jpg or .png or .jpeg or .gif:\n")

            if type == '.jpg':

                image(url, type, imagename)

            elif type == '.png':

                image(url, type, imagename)

            elif type == '.jpeg':

                image(url, type, imagename)

            elif type == '.gif':

                image(url, type, imagename)

            else:

                raise TypeError

        elif n == 2:

            filename = input("Enter file's name:\n")

            type = input("\nEnter type of file:\n")

            url = input("\nPaste the url of the file which allows access:\n")

            file(url, type, filename)

        else:

            raise ValueError

    # IMAGE SAVE FUNCTION
    def image_save(mode, imname):

        print("\nEnter:")

        save_option = int(input("1 : save the image\n2 : Do more editing\n0 : Don't save\n"))

        if save_option == 1:

            print("\nSelect:")

            edit_option = int(input("1 : Save as original\n2 : Save as new image\n"))

            if edit_option == 1:

                oldip = mode.save(imname)

            elif edit_option == 2:

                newimagename = input("Enter new name of modified image [with extension]:\n")

                newip = mode.save(newimagename)

            else:

                raise ValueError

        elif save_option == 0:

            print(" Image not saved ".center(150, '='))

        if save_option != 1 and save_option != 2 and save_option != 0:

            raise ValueError

    # IMAGE EDIT SECTION
    def image_edit():

        imname = input("\nEnter the name of image to be edited: [With extension]\n")

        i = Image.open(imname)

        s = " Dimensions of " + imname + " are " + str(i.size)

        print(s.center(150, '='))

        print("\nSelect:")

        option = int(input("1 : open the image\n2 : crop the image\n3 : resize image\n4 : rotate the image\n0 : Close the editor\n"))

        if option == 0:

            print(" Editor closed ".center(150, '='))

        options = [1,2,3,4,0]

        if option not in options:

            raise ValueError

        while option != 0:

            if option == 1:

                i.show()

            elif option == 2:

                t1 = tuple(map(int,input("\nEnter starting coordinates of the cropping area [Space seperated numbers] :").split()))

                t2 = tuple(map(int,input("\nEnter ending coordinates of the cropping area [Space seperated numbers] :").split()))

                t = t1+t2

                cropped = i.crop(t)

                cropped.show()

                image_save(cropped, imname)

            elif option == 3:

                resize_tuple = tuple(map(int,input("Enter the new dimensions of the image [Space seperated numbers] : \n").split()))

                resized = i.resize(resize_tuple)

                resized.show()

                image_save(resized, imname)


            elif option == 4:

                angle = float(input("Enter the degrees to be rotated in anti clockwise direction:\n"))

                rotated = i.rotate(angle)

                rotated.show()

                image_save(rotated, imname)


            print("\nWhat next?\n")

            option = int(input("1 : open the image\n2 : crop the image\n3 : resize image\n4 : rotate the image\n0 : Close the editor\n"))

            if option == 0:

                print(" Editor closed ".center(150, '='))
    # MAIN MENU
    k=int(input("Enter 1 for downloading , 2 for image editor, 0 for exiting:\n"))

    if k == 0:

        print("Thanks for using me,Revisit soon :)".center(150, '='))

    if k != 0 and k != 1 and k != 2:

        raise ValueError

    while k != 0:

        if k == 1:

            n = int(input("\nEnter 1 for image and 2 for file:\n"))

            fn(n)

        elif k == 2:

            image_edit()

        k = int(input("\nThis time?\n1 : download\n2 : edit\n0 : exit\n"))

        if k == 0:

            print("Thanks for using me,Revisit soon :)".center(150, '='))

        if k != 0 and k != 1 and k != 2:

            raise ValueError

# EXCEPTION HANDLERS
except TypeError:

    print(" Not valid ".center(150, '='))

except ValueError:

    print(" Not in options ".center(150, '='))

except urllib.error.HTTPError:

    print(" Forbidden by website ".center(150, '='))

except FileNotFoundError:

    print(" Enter item which is found in the directory ".center(150, '='))
