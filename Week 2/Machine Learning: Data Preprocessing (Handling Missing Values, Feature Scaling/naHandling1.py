#importing pandas and numpy

import pandas as pd
import numpy as np


# inputting the data in the program
data = {'Name': ['Alice', 'Bob', 'Charlie', np.nan, 'Eve'],
        'Age': [25, np.nan, 30, 22, np.nan],
        'Salary': [50000, 60000, np.nan, 52000, 58000]}


# using dataframe to load the data into the variable source
source= pd.DataFrame(data)
print(source.isnull().sum())


# deleting the row with "na"
cleansource= source.dropna()
print(cleansource)


#filling the numeric value with mean of the column.
meanFill= source.fillna(source.mean(numeric_only=True))
print(meanFill)