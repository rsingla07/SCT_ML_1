import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
data=pd.read_csv("house_prediction.csv")
print(data.head())
x=data[["SquareFeet","Bedrooms","Bathrooms"]]
y=data["Price"]
x_train,x_test,y_train,y_test=train_test_split(x,y)
model=LinearRegression()
model.fit(x_train,y_train)
area=float(input("enter required area:"))
bedrooms=int(input("enter number of bedrooms:"))
bathrooms=int(input("enter number of bathrooms:"))
data_final=[[area,bedrooms,bathrooms]]
result=model.predict(data_final)
print(f"expected price of house:{result[0]:,.2f}")