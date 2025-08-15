import numpy as np
import pandas as pd
import streamlit as st 

st.title("ORDERING SYSTEM")
st.write("## MENU")
st.write("~","我們用心製作每一道餐點","~")

st.write("## 外帶內用")
r1 = st.checkbox("外帶")
if r1:
    st.info("外帶")
else:
    st.info("內用")

checks = st.columns(2)
txt = ''
with checks[0]:
    r11 = st.checkbox(' 大人 ')
    if r11:
        txt += ' 大人 '
with checks[1]:
    r12 = st.checkbox(' 小孩 ')
    if r12:
        txt += ' + 小孩 '
st.info(txt)

st.write("## 嬰兒人數")
num = st.slider("嬰兒人數", 0, 10, 0)
st.info(f"人數: {num} 位")
st.write("## 套餐")

# 定義各項餐點的價格字典
appetizer_prices = {
    '凱薩沙拉': 100,
    '羅勒沙拉': 120,
    '田園沙拉': 130
}

main_prices = {
    '瑪格麗特義大利麵': 280,
    '培根義大利麵': 300,
    '海鮮義大利麵': 350,
    '田園義大利麵': 250
}

dessert_prices = {
    '起司蛋糕': 150,
    '巧克力蛋糕': 170,
    '草莓蛋糕': 160
}

drink_prices = {
    '珍珠奶茶': 80,
    '綠茶': 60,
    '咖啡': 100,
    '檸檬水': 50
}

# 選擇餐點並顯示價格
b1 = st.radio("開胃菜:", tuple(appetizer_prices.keys()), key="b1")
b1price = appetizer_prices[b1]
st.info(f"{b1}  ${b1price}")

b2 = st.radio("主餐:", tuple(main_prices.keys()), key="b2")
b2price = main_prices[b2]
st.info(f"{b2}  ${b2price}")

b3 = st.radio("甜點:", tuple(dessert_prices.keys()), key="b3")
b3price = dessert_prices[b3]
st.info(f"{b3}  ${b3price}")

b4 = st.radio("飲料:", tuple(drink_prices.keys()), key="b4")
b4price = drink_prices[b4]
st.info(f"{b4}  ${b4price}")

st.write("## 總計")
total = b1price + b2price + b3price + b4price
st.info(f"總金額: ${total} 元")

st.sidebar.write("## 甜點上餐方式")
dessert = st.sidebar.selectbox( "甜點:", ("隨餐上", "後上", "其他"))
if dessert == "隨餐上":
    st.sidebar.info(" A ")
elif dessert == "後上":
    st.sidebar.info(" B ")
else:
    st.sidebar.info(" OTHERS ")

st.sidebar.write("## 飲料上餐方式")
drink = st.sidebar.selectbox( "飲料:", ("隨餐上", "後上", "其他"))
if drink == "隨餐上":
    st.sidebar.info(" A ")
elif drink == "後上":
    st.sidebar.info(" B ")
else:
    st.sidebar.info(" OTHERS ")

st.write("## 按鈕")
a = st.number_input("num...", key="a")
b = st.number_input("num...", key="b")
if st.button("相加"):
    st.write("###", a + b)

#-------------------------------------------------#
arr1 = np.array([1, 2, 3, 4, 5, 6])
st.write(arr1)

df1 = pd.DataFrame([[11,22,33,44],[50,60,70,80]])
st.write(df1)
st.table(df1)
