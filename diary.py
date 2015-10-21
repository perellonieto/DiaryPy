"""
This class can be used to save the intermediate results of any experiment
run in python. It will create a folder for the specific experiment and
save all the information and images in a structured and sorted manner.
"""
__docformat__ = 'restructedtext en'

import os
import sys
import datetime

import csv

try:
    import PIL.Image as Image
except ImportError:
    import Image

RESULTS_FILENAME='results.csv'
DESCRIPTION_FILENAME='description.txt'

class Diary(object):
    def __init__(self, name, path='diary', overwrite=False, image_format='png'):
        self.creation_date = datetime.datetime.now()
        self.name = name
        self.path = os.path.join(path,name)
        self.overwrite = overwrite

        self.image_format = image_format
        self.iteration = 0

        self.all_paths = self._create_all_paths()
        self._save_description()

    def _create_all_paths(self):
        path = self.path
        i = 0
        while self.overwrite == False and os.path.exists(self.path):
            self.path = "{}_{}".format(path,i)
            i +=1

        self.path_images = os.path.join(self.path, 'images')
        all_paths = [self.path, self.path_images]
        for path in all_paths:
            if not os.path.exists(path):
                os.makedirs(path)
        return all_paths

    def _save_description(self):
        with open(os.path.join(self.path, DESCRIPTION_FILENAME), 'w') as f:
            print("Writting :\n{}".format(self))
            f.write(self.__str__())

    def next_iteration(self):
        self.iteration +=1

    def save_iteration_results(self, row, inc=False):
        with open(os.path.join(self.path, RESULTS_FILENAME), 'a') as csvfile:
            writer = csv.writer(csvfile, delimiter=',', quotechar='|',
                    quoting=csv.QUOTE_NONNUMERIC)
            now = datetime.datetime.now()
            writer.writerow([self.iteration,  now.date(), now.time()] + row)
        if inc:
            self.iteration += 1

    def save_image(self, image, filename='', extension=None, inc=False):
        if extension == None:
            extension = self.image_format
        image.save(os.path.join(self.path_images,
                                "{}_{}.{}".format(filename, self.iteration,
                                                  extension)))
        if inc:
            self.iteration += 1

    def __str__(self):
        return ("Date: {}\nName : {}\nPath : {}\n"
                "Overwrite : {}\nImage_format : {}\n"
                "").format(self.creation_date, self.name, self.path,
                        self.overwrite, self.image_format)

if __name__ == "__main__":
    diary = Diary(name='world', path='hello', overwrite=False)
    diary.save_iteration_results(['hi!', 0.3, 25, 'yes', 0, 'no'])
    image = Image.new(mode="1", size=(16,16), color=0)
    diary.save_image(image, filename='test', inc=True)
    diary.save_iteration_results(['bye', 0.5, 32, 'no', 0, 'yes'])
    image = Image.new(mode="1", size=(16,16), color=1)
    diary.save_image(image, filename='test')
