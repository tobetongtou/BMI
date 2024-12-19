import streamlit as st
st.title("BMI计算器")

weight = st.text_input("Your weight(kg)")
height = st.text_input("Your height(m)")
if weight:
    weight = float(weight)
    if height:
        height = float(height)
        if st.button("calculate"):
            BMI = weight / (height) ** 2
            st.text("Your BMI is " + str(BMI))
    else:
        st.text("请填写身高体重~填写完记得敲回车~")
else:
    st.text("请填写身高体重~填写完记得敲回车~")

# #BMI=体重/（身高**2）
# user_weight=float(input("请输入您的体重kg"))
# user_height=float(input("请输入您的身高m"))
# #要将字符串改成数字
# user_BMI=user_weight/(user_height)**2
# user_sex=input("您的性别是（M/F）：")
# print("您的BMI值为："+str(user_BMI))
# #要将数字用str转化成字符串
#
# #偏瘦：user_BMI<=18.5
# #正常：18.5<user_BMI<=25
# #偏胖：25<user_BMI<=30
# #肥胖：user_BMI>30
#
# if user_BMI<=18.5:
#     if user_sex=="M":
#         #这里不能用=，必须用==否则会变成赋值；后面的字符串需要加""
#         print("先生您好，您的BMI范围属于偏瘦")
#     else:
#         print("女士您好，您的BMI范围属于偏瘦")
# elif 18.5<user_BMI<=25:
#     if user_sex == "M":
#         print("先生您好，您的BMI范围属于正常")
#     else:
#         print("女士您好，您的BMI范围属于正常")
# elif 25<user_BMI<=30:
#     if user_sex == "M":
#         print("先生您好，您的BMI范围属于偏胖")
#     else:
#         print("女士您好，您的BMI范围属于偏胖")
# else:
#     if user_sex == "M":
#         print("先生您好，您的BMI范围属于肥胖")
#     else:
#         print("女士您好，您的BMI范围属于肥胖")