import matplotlib.pyplot as plt
import numpy as np

blood_sugar_men = [113, 85, 90, 150, 149, 88, 93, 115, 135, 80, 77, 82, 129]
blood_sugar_women = [67, 98, 89, 120, 133, 150, 84, 69, 89, 79, 120, 112, 100]

blood=[blood_sugar_men,blood_sugar_women]
color=['g','r']

bins=[80,100,125,150]
plt.xlabel("blood sugar range")
plt.ylabel("total number of patiant")

plt.hist(blood,bins=bins,color=color,)
plt.show()