import matplotlib
import matplotlib.pyplot as plt
import numpy as np
student_name=['sam','riddhonil','holly','gojo','goku','kakashi']
student_marks=[90,99,56,89,91,95]
plt.plot(student_name,student_marks,color='green',linewidth=2)
plt.title('marks of students')
plt.xlabel('student_name')
plt.ylabel('marks of students')
plt.show()


plt.bar(student_name,student_marks,color='green',linewidth=2)
plt.title('marks of students')
plt.xlabel('student_name')
plt.ylabel('marks of students')
plt.show()

