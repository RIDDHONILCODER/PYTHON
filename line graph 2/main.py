import matplotlib.pyplot as plt

x=[0,5,10,15,20,25,30,35,40,45,50,55,60]
y=[10,20,30,40,50,60,70,80,90,100,110,120,130]
y1=[10,27,35,44,33,67,30,25,92,24,10,22,35]
plt.plot(x,y,linestyle='dashed',marker='D')
plt.plot(x,y1,linestyle='dashed',marker='D')
plt.title('time velosity graph')
plt.xlabel('velosity')
plt.ylabel('time')
plt.xlim(5,40)
plt.ylim(10,60)
plt.legend()
plt.show()