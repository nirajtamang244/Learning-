import pandas as pd

container= pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/refs/heads/master/anagrams.csv")

filter= container[container["num1"]==6]
#print(container)
filter.to_csv("filtered_data.csv")
print(filter)