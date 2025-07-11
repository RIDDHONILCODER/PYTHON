import matplotlib.pyplot as plt
year=[2020,2021,2022,2023,2024,2025]
m_goals=[20,30,25,23,12,27]
r_goals=[23,30,45,68,46,98]
plt.plot(year,m_goals,linestyle='dashed',marker='D')
plt.plot(year,r_goals,linestyle='dashed',marker='D')
plt.title('messi and ronaldo goals')
plt.xlabel('year')
plt.ylabel('number of goals')
plt.grid(True)
plt.show()