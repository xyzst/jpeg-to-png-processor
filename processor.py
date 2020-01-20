"""
JPEG Image Processor

A simple command line interface JPEG to PNG converter

__author__ = "Darren Rambaud"
__email__ = "xyzst@users.noreply.github.com"
"""
import glob
import os
import sys

from PIL import Image


def jpeg_to_png(directories):
    """
    Walks through the root directory defined by directories[0], finds .jpeg or .jpg files, and converts them to .png files

    :param directories: A tuple of strings, the 0th index contains the path to the directory of jpeg files and the 1st
    index contains the path to store the pngs
    :return: None
    """
    for subdir, dirs, files in os.walk(directories[0]):
        for jpeg in glob.glob(os.path.join(subdir, '*.jpg')) + glob.glob(os.path.join(subdir, '*.jpeg')):
            if not os.path.exists(directories[1] + '/' + subdir):
                print('[WARN] Creating new subdirectory under \'%s\' - %s' % (directories[1], subdir))
                os.mkdir(directories[1] + '/' + subdir)
            with Image.open(jpeg) as jpg:
                print('Processing %s...' % jpeg)
                jpg.save(directories[1] + '/' + jpeg + '.png', 'png')


def verify_arguments(jpeg, png):
    """
    Verify existence of paths provided by the two arguments

    :param jpeg: A string which contains the path to the .jpeg|.jpg files
    :param png: A string which contains the path to store the generated png files
    :return: A tuple (jpeg, png) if the paths exists on the current file system
    """
    if len(sys.argv) != 3:
        print('[ERR] Not enough arguments, usage: python processor.py /path/dir/with/jpeg/files /path/to/new/dir/png',
              file=sys.stderr)
        sys.exit(-1)

    if not os.path.exists(jpeg):
        print('[ERR] The %s does not exist' % jpeg, file=sys.stderr)
        sys.exit(-1)

    if not os.path.isdir(jpeg):
        print('[ERR] The %s is not a directory' % jpeg, file=sys.stderr)
        sys.exit(-1)

    if not os.path.exists(png):
        print('[WARN] The \'%s\' directory does not exist, will create this directory' % png)
        os.mkdir(png)

    return jpeg, png


if __name__ == '__main__':
    jpeg_to_png(verify_arguments(sys.argv[1], sys.argv[2]))
