score1=input('請輸入你的成績')
score2=int(score1)
if score2>=0 and score2<101 :
    if score2>=90:
        print("A 恭喜 突破自己")
    
    elif score2>=80:
        print("B 可以接受 有維持水準") 
    
    elif score2>=70:
        print("C 差強人意 再加油")  
    
    elif score2>=60:
        print("D 低空飛過 要認真念書") 
     
    else:
        print("F 該死 考一個不及格 以後只能唸佛光玄奘了 先取法號吧")
else :
    print("不要亂輸成績")