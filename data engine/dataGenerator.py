#!/usr/bin/env python
import math
import numpy as np
import re
import string

from collections import Counter
from matplotlib import pyplot as plt
from PIL import Image
# You will need to update this path to match the folder in your Google Drive
PATH = "../pictures"
labels =  "{PATH}"
label = list(string.ascii_uppercase)
labels = labels[0].split()
print(labels)
