import pandas as pd
import numpy as np

result = pd.read_table('C:/Users/student/Desktop/ex3.txt', sep='\s+')
print(type(result))
print(result)
print(result.info())

result = pd.read_table('C:/Users/student/Desktop/ex3.txt', sep='\s+', skiprows=[2, 3])
print(type(result))
print(result)
print(result.info())

result = pd.read_table('C:/Users/student/Desktop/ex3.txt', sep='\s+', na_values = {'B':0, 'C':-999})
print(type(result))
print(result)
print(result.info())
