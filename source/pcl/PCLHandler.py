import numpy as np
import open3d as op3d

class PCLHandler:
    """ PCLHandler handles file i/o
    of .xyz files and stores them in numpy.
    Several other options to pcl..."""

def __init__(self, path):
    self.path = path
    self.xyz = readFiles(path)

def readFiles(path):
    try:
        xyz = op3d.read_point_cloud(path)
    except:
        print("Error File I/O!")
    return xyz
