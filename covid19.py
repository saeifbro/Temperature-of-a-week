


import numpy as np
import matplotlib.pyplot as plt
day=np.array(["March1","March2","March3","March4","March5","March6","March7","March8","March9","March10"])

case=np.array([50,65,80,110,150,130,90,70,40,55])
plt.figure(figsize=(10,6))


plt.fill_between(day,case,where=(case >=110) & (case<=150),color="red")
plt.fill_between(day,case,where=(case>=40) & (case<=55),color="green")
plt.plot(day,case,color="blue",marker="o",label="daily_cases")
plt.legend()
plt.title("The Covid-19 case ",color="blue")
plt.grid(True,color="gray",alpha=0.5)
plt.ylabel("case",color="blue",fontsize=15)
plt.xlabel("day",color="red")
plt.show()







