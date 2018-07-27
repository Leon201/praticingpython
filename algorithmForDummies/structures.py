import pandas as pd
import numpy as np

df = pd.DataFrame({'A': [0, 0, 1, None]
                      , 'B': [1, 2, 3, 4]
                      , 'C': [np.NAN, 3, 4, 1]}
                  , dtype=int)

print(df, "\n")

values = pd.Series(df.mean(), dtype=int)
print(values, "\n")

df = df.fillna(values)
print(df)
