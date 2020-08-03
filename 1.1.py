height=float(input('請輸入你的身高'))
weight=float(input('請輸入你的體重'))
bmi=float(weight/((height/100)**2))
print(bmi)
if bmi<=18.5 :
   print("體重不足 紙片人")
    
elif bmi<=24 :
   print("正常")
        
elif bmi<=27 :
   print("過重 少吃點胖老爹")
    
elif bmi<=30 :
   print("輕度肥胖 a little obese")

elif bmi<=35 :
   print("中度肥胖 obese")
        
else:
   print("重度肥胖 extremely obese")