import random
import datetime
import pandas as pd
import matplotlib.pyplot as plt
import statistics
import numpy as np
import scipy
from scipy import stats
import seaborn

print("successs")

data = pd.read_csv('./example/trip.csv')

print(len(data))
data.head()