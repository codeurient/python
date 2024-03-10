import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = pd.read_excel('Datasets-main/ESD.xlsx')
df = pd.DataFrame(data)

plt.scatter(  df['Annual Salary'],   df['EEID'] )
plt.show()