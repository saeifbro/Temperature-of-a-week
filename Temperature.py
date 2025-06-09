


import matplotlib.pyplot as plt
import numpy as np


#the maximum temperature of 7 days
day=["Saturday","Sunday","Monday","Tuesday","Wednesday","Thursday","Friday"]
max_temperature=[23,50,70,60,80,90,70]
#the minimum temperature of 7 days
plt.figure(figsize=(10,6))  #creating campus
min_temperature=[16,15,13,8,22,25,31]

plt.stem(day,max_temperature,markerfmt="go",label="maximum_temperatute",linefmt=":")
plt.xlabel("Day",color="red")
plt.legend()
plt.ylabel("Temperatue(Celcuis)",color="blue")

plt.xticks(rotation=45,color="blue")
plt.yticks(color="green")


plt.stem(day,min_temperature,markerfmt="ro",label="minimum_temperature",linefmt=":")
plt.title("Temperature of Seven days ",color="blue")
plt.legend()
plt.tight_layout()
plt.show()