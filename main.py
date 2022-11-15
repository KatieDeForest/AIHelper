import Redbubble
import Upscaler
import shutil
from Upscaler import *
from Redbubble import *
import os


# assign directory

# iterate over files in
# that directory


def main():
    # os.remove('resources/Black Hole, space, ai, blackhole.png')

    shutil.copyfile('Black Hole, space, ai, blackhole.png', 'resources/Black Hole, space, ai, blackhole.png')
    # os.popen("copy 'Black Hole, space, ai, blackhole.png' './resources/Black Hole, space, ai, blackhole.png'")
    directory = './resources'
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        # checking if it is a file
        if os.path.isfile(f):
            Upscaler.upScaleImage('resources\Black Hole, space, ai, blackhole.png')
            Redbubble.uploadToRedbubble()


if __name__ == "__main__":
    main()
