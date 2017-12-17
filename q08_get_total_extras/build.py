# Default Imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
import numpy as np

path = 'data/ipl_matches_small.csv'

# Enter Code Here
def get_total_extras():
    data = read_ipl_data_csv(path,dtype='|S50')

    extra = 0
    for i in data:
        extra = extra + int(i[17])

    return extra
