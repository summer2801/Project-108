import random
import plotly.express as px
count=[]
dice_result=[]
for i in range(0,100):
    dice_1=random.randint(1,6)
    dice_2=random.randint(1,6)
    dice_result.append(dice_1+dice_2)
    count.append(i)

print(count,dice_result)
fig=px.bar(x=dice_result,y=count)
fig.show()
