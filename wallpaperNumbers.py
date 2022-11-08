# Import the required modules
import os
import random
# Assign the target directory
directory = '/home/leo/Pictures/Wallpapers/'
# Iterate over the files in that directory
for filename in os.scandir(directory):
    # Creates a random number
    randomNumber = random.randrange(1000000000, 9999999999)
    # Transform the filename in a string
    file = str(filename)
    # Check the type of the extensions
    if file.endswith(".jpg'>"):
        os.rename(filename, directory + str(randomNumber) + ".jpg")
    elif file.endswith(".png'>"):
        os.rename(filename, directory + str(randomNumber) + ".png")
    elif file.endswith(".jpeg'>"):
        os.rename(filename, directory + str(randomNumber) + ".jpeg")
    elif file.endswith(".tif'>"):
        os.rename(filename, directory + str(randomNumber) + ".tif")
    elif file.endswith(".jfif'>"):
        os.rename(filename, directory + str(randomNumber) + ".jfif")
print("All files have been renamed!")
