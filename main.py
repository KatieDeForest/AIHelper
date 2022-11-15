import Redbubble
import Upscaler
from Upscaler import *
from Redbubble import *
import os

# assign directory

# iterate over files in
# that directory


def main():
    directory = 'resources'
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        # checking if it is a file
        if os.path.isfile(f):
            Upscaler.upScaleImage(f)
            Redbubble.uploadToRedbubble()



if __name__ == "__main__":
    main()
