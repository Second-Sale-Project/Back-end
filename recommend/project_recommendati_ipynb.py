# -*- coding: utf-8 -*-
"""Project_Recommendati.ipynb.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1GaS9fK1VLjjrH8OOALq5NZ8otU-hJCkr
"""

import pandas as pd
import numpy as np 
from scipy.sparse import csr_matrix
from sklearn.neighbors import NearestNeighbors

#指定csv位置
df = pd.read_csv("/content/drive/MyDrive/Colab Notebooks/專案/Recommendation_AI0.1/_Organized  Example data.xlsx - シート1.csv", sep=",")

#利用0~2資料（BrandID、BrandID、rating）
df = df.iloc[:,0:3]

#疎行列#重新排列
df_piv = df.pivot(index= "UserID",columns="BrandID",values="rating").fillna(0)

#使用scikit-learnde時候，讓它速度變快的指定
df_sp = csr_matrix(df_piv.values)

#使用KNN。brute方式。
rec = NearestNeighbors(n_neighbors=10,algorithm= "brute", metric= "cosine")

# 練習KNN
rec_model = rec.fit(df_sp)

User = 1#指定User
distance, indice = rec_model.kneighbors(df_piv.iloc[df_piv.index== User].values.reshape(1,-1),n_neighbors=5)
for i in range(5):#掛號裡面是指定列出數量,包含指定User
    if  i == 0:#指定的User是i==0。
        print("類似UserID:{0}的User是以下,(推薦電影ID,評価)。".format(User))
    else:
        print('UserID:{0} '.format(df_piv.index[indice.flatten() [i]]))
        rec_movie = df_piv[df_piv.index[indice.flatten() [i]]]
        rec_movie_sort = sorted(rec_movie.items(), reverse=True, key=lambda x:x[1])#reverse→降順、辞書のvalueをkeyにソート
        rec_movie_3 = rec_movie_sort[0:3]#評価の高い映画を3つ抽出
        print(rec_movie_3)
print("\n")

# 距離近的優先列出
# n_neighbors=11是包含指定這，列出的數量
Brand = 25          #指定brandID
distance, indice = rec_model.kneighbors(df_piv.iloc[df_piv.index== Brand].values.reshape(1,-1),n_neighbors=11)
for i in range(11):
    if  i == 0:  #i=0是指選的brand。
        print("選BrandID{}的人，推薦一下品牌。".format(Brand))
    else:
        print("{0}: {1}".format(i,df_piv.index[indice.flatten()[i]]))#從喜好排列