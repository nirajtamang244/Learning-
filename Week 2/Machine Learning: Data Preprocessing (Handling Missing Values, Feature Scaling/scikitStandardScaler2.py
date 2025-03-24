import pandas as pd
from sklearn.preprocessing import StandardScaler

df = pd.DataFrame({'Height': [150, 160, 170, 180, 190],
                   'Weight': [55, 65, 75, 85, 95]})

variable= pd.DataFrame(StandardScaler().fit_transform(df),columns=df.columns)

print(variable)