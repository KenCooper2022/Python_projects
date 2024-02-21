#this project incorporates Bayes theorem
#originally created to prove the existence of God 
#it's a theorem that is aimed at creating probabilities given the discovery of new data
#it has boundless applications such as for example:
#accounting for the frequency of false positive diagnoses within a study of cancer patients
import sys
import random
import itertools
import numpy as np
import cv2 as cv
MAP_FILE = 'cape_python.png'
SA1_CORNERS=(130,265,180,315)
SA2_CORNERS=(80,255,130,130,305)
SA3_CORNERS=(105,205,155,255)
class Search():
    """Bayesian Search and Rescue game """
    def _init_(self,name):
        self.name=name
        self.img = cv.imread(MAP_FILE,cv.IMREAD_COLOR)
        if self.img is None:
            print('Could not load map file {}'.format(MAP_FILE),
            file = sys.stderr)
            sys.exit(1)
        self.area_actual=0
        self.sailor_actual = [0,0] #as "local"coords within search are 
        self.sa1=self.img[SA1_CORNERS[1]:SA1_CORNERS[3],SA1_CORNERS[0]:SA1_CORNERS[2]]
        self.sa2=self.img[SA2_CORNERS[1]:SA2_CORNERS[3],SA2_CORNERS[0]:SA2_CORNERS[2]]
        self.sa3=self.img[SA3_CORNERS[1]:SA3_CORNERS[3],SA3_CORNERS[0]:SA2_CORNERS[2]]

        self.p1 = 0.2
        self.p2=0.5
        self.p3=0.3
        
        self.sep1=0
        self.sep2=0
        self.sep3=0

        
