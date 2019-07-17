import matplotlib.pyplot as plt
from numpy import polyfit, polyval

x = range(10)
y = [0.1,1.2,2.4,3.3,3.8,5.0,5.7,7.1,8.3,9.0]

z = polyfit(x,y,1)

plt.plot(x,y, linestyle ='None', marker ='o')
plt.plot(x,polyval(z,x),'r')
plt.show()