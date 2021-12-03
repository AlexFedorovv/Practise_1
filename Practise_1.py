import numpy
import math
import matplotlib.pyplot as plt
import os

def mathFunction (x, A):
    result = 100*math.sqrt(math.fabs(A-0.01*math.pow(x,2))) + 0.01*math.fabs(x+10)
    return result

x1   = -5
x2   = 15
step = 0.5

A = 1

x = list(numpy.arange(x1, x2 + step, step))
y = list(numpy.arange(x1, x2 + step, step))

for index, value in enumerate(x):
    print("[",value,"]: ", mathFunction(value, A))
    y[index] = mathFunction(value, A)
    
plt.plot(x,y,'r-')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.show()

if os.path.exists("results"):
    print("Указанный файл существует")
else:
    print("Файл не существует")
    os.mkdir("results")

file = open("results/result.xml", "w")
file.write("<?xml version=\"1.1\" encoding=\"UTF-8\" ?>\n")
file.write("<data>\n")

file.write("    <xdata>\n")

for index, value in enumerate(x):
    file.write("        <x>")
    file.write(str(value))
    file.write("</x>\n")
file.write("    </xdata>\n")

file.write("    <ydata>\n")
for index, value in enumerate(x):
    file.write("        <y>")
    file.write(str(mathFunction(value, A)))
    file.write("</y>\n")
file.write("    </ydata>\n")

file.write("</data>\n")

file.close()
