#You are developing a program that analyzes weather data. Write a Python function
#that takes a list of temperature readings for a specific location and determines the
#average temperature, highest temperature, and lowest temperature.
#Input
#temperature_readings = [25, 28, 21, 24, 27]
#Output:
#Average Temperature: 25.0
#Highest Temperature: 28
#Lowest Temperature: 21
l1 = [25, 28, 21, 24, 27]
avg = 0
sum =0
for i in range(len(l1)):
    sum = sum + l1[i]

avg = sum/5

l1.sort()

print(avg)
print(l1[0])
print(l1[len(l1)-1])