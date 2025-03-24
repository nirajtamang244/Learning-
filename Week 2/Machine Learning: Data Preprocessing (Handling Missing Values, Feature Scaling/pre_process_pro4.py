import pandas as pd
from sklearn.preprocessing import MinMaxScaler,StandardScaler,OneHotEncoder,LabelEncoder

df = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")

#fillna
df["Survived"]= df["Survived"].fillna(df["Survived"].median())
print(df)

#delna for those which are not numerical value and cannot be filled
df_dropped= df.dropna()
print(df_dropped)

#Min_max_scaler
df_dropped["Survived"]= MinMaxScaler().fit_transform(df_dropped[["Survived"]])



#Standard Scaler
df_dropped[["Fare","Age"]]= StandardScaler().fit_transform(df_dropped[["Fare","Age"]])


#Label encoder
df_dropped["PassengerId"]= LabelEncoder().fit_transform(df_dropped["PassengerId"])
final_df= df_dropped[["Survived","Fare","Age","PassengerId"]].head()
print(final_df)


#oneHotEncodere
variable= pd.get_dummies(final_df,columns=["Survived"],dtype=int)
print(variable.head())
