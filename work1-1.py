import pandas as pd
import matplotlib.pyplot as plt

#圖1: x,y 軸為 花萼(sepal) 之寬度與高度

df = pd.read_csv("iris.csv",index_col="class",encoding = "utf8")#讀取iris資料，並將類別設為索引值

x_setosa = df.loc["Iris-setosa","sepal length"]#取出setosa這個品種的sepal所有x值
y_setosa = df.loc["Iris-setosa","sepal width"]#取出setosa這個品種的sepal所有y值

x_versicolor = df.loc["Iris-versicolor","sepal length"]#取出versicolor這個品種的sepal所有x值
y_versicolor = df.loc["Iris-versicolor","sepal width"]#取出versicolor這個品種的sepal所有y值

x_virginica = df.loc["Iris-virginica","sepal length"]#取出virginica這個品種的sepal所有x值
y_virginica = df.loc["Iris-virginica","sepal width"]#取出virginica這個品種的sepal所有y值
      
plt.xlabel("Sepal length")#顯示x座標代表的文字
plt.ylabel("Speal width")#顯示y座標代表的文字


plot_setosa = plt.scatter(x_setosa, y_setosa, 25, "r")#將setosa描繪在座標軸上，且設為紅色
plot_versicolor =plt.scatter(x_versicolor, y_versicolor, 25, "tab:orange")#將versicolor描繪在座標軸上，且設為橘色
plot_virginica =plt.scatter(x_virginica, y_virginica, 25, "tab:purple" )#將virginica描繪在座標軸上，且設為紫色

plt.legend([plot_setosa,plot_versicolor,plot_virginica], labels =["setosa","versicolor","virginica"])#增加圖例






