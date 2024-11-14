import pandas
import matplotlib.pyplot as plt
data=pandas.read_csv(r"People.csv")
# print(data.tail(10))
# print(data["Phone"])
# print(data.info())
# print(data.describe())
data["Phone"].plot()
plt.show()
