import math
#Polygon points
pp = int (input ("Enter the number of polygon points :"))

#Polygon coordinates
coordinatesList = []
for i in range (1, pp+1) :
    print ("Enter the x and y coordinates of the polygon point", i)
    item = int(input('X:')), int(input('Y:'))
    coordinatesList.append(item)

print ("Polygon Coordinates: ")
print (f"{'Point':>3}{'x':>7}{'y':>3} ")
print ("-" * 17)

for cl in range (1, pp+1) :  
    print ('Point', cl, ':', coordinatesList[cl-1])

#Unpacking tuple
for cc in range (1, pp+1):
    a = coordinatesList [cc-1]
    (x, y) = a
    
#Polygon Formulas  
print ("Geometric characteristics:")

#Ax
def PolygonArea(vertices):
    n = len(vertices)
    area = 0.00
    for x in range(n):
        y = (x + 1) % n
        area += vertices[x][0] * vertices[y][1]
        area -= vertices[y][0] * vertices[x][1]
    area = abs(area) / 2.0
    return area

print ("Ax:", f"{PolygonArea(coordinatesList):11.2f}")

#Sx
def PolygonStaticX(vertices):
    n = len(vertices)
    static = 0.00
    for i in range(n):
        if i != n-1:
            static += (vertices[i+1][0] - vertices[i][0]) * ((vertices[i+1][1])**2 + vertices[i][1] * vertices[i+1][1] + (vertices[i][1])**2) 
        else:
            static += (vertices[0][0] - vertices[i][0]) * ((vertices[0][1])**2 + vertices[0][1] * vertices[0][1] + (vertices[0][1])**2) 
    static = (static) / -6.0
    return static

print ("Sx:", f"{PolygonStaticX(coordinatesList):11.2f}") 

#Sy
def PolygonStaticY(vertices):
    n = len(vertices)
    static = 0.00
    for i in range(n):
        if i != n-1:
            static += (vertices[i+1][1] - vertices[i][1]) * ((vertices[i+1][0])**2 + vertices[i][0] * vertices[i+1][0] + (vertices[i][0])**2) 
        else:
            static += (vertices[0][1] - vertices[i][1]) * ((vertices[0][0])**2 + vertices[i][0] * vertices[0][0] + (vertices[i][0])**2)
    static = (static) / 6.0
    return static

print ("Sy:", f"{PolygonStaticY(coordinatesList):11.2f}") 

#Ix
def PolygonDinamicX(vertices):
    n = len(vertices)
    dinamic = 0.00
    for i in range(n):
        if i != n-1:
            dinamic += (vertices[i+1][0] - vertices[i][0]) * ((vertices[i+1][1])**3 + (vertices[i+1][1])**2 * vertices[i][1] + vertices[i+1][1] * (vertices[i][1])**2 + (vertices[i][1])**3)
        else:
            dinamic += (vertices[0][0] - vertices[i][0]) * ((vertices[0][1])**3 + (vertices[0][1])**2 * vertices[i][1] + vertices[0][1] * (vertices[i][1])**2 + (vertices[i][1])**3)
    dinamic = (dinamic) / -12.0
    return dinamic

print ("Ix:", f"{PolygonDinamicX(coordinatesList):11.2f}") 

#Iy
def PolygonDinamicY(vertices):
    n = len(vertices)
    dinamic = 0.00
    for i in range(n):
        if i != n-1:
            dinamic += (vertices[i+1][1] - vertices[i][1]) * ((vertices[i+1][0])**3 + (vertices[i+1][0])**2 * vertices[i][0] + vertices[i+1][0] * (vertices[i][0])**2 + (vertices[i][0])**3)
        else:
            dinamic += (vertices[0][1] - vertices[i][1]) * ((vertices[0][0])**3 + (vertices[0][0])**2 * vertices[i][0] + vertices[0][0] * (vertices[i][0])**2 + (vertices[i][0])**3)
    dinamic = (dinamic) / 12.0
    return dinamic
 
print ("Iy:", f"{PolygonDinamicY(coordinatesList):11.2f}") 

#Ixy
def PolygonDinamicXY(vertices):
    n = len(vertices)
    dinamic = 0.00
    for i in range(n):
        if i != n-1:
            dinamic += (vertices[i+1][1] - vertices[i][1]) * ((vertices[i+1][1] * (3*vertices[i+1][0]**2 + 2*vertices[i+1][0] * vertices[i][0] + vertices[i][0]**2)) + (vertices[i][1] * (3*vertices[i][0]**2 + 2*vertices[i+1][0] * vertices[i][0] + vertices[i+1][0]**2)))
        else:
            dinamic += (vertices[0][1] - vertices[i][1]) * ((vertices[0][1] * (3*vertices[0][0]**2 + 2*vertices[0][0] * vertices[i][0] + vertices[i][0]**2)) + (vertices[i][1] * 3*vertices[i][0]**2 + 2*vertices[0][0] * vertices[i][0]+ vertices[0][0]**2))
    dinamic = (dinamic) / -24.0
    return dinamic

print ("Ixy:", f"{PolygonDinamicXY(coordinatesList):10.2f}")   

#xt
totalX = PolygonStaticY(coordinatesList) / PolygonArea(coordinatesList)
print ("xt:", f"{totalX:11.2f}")

#yt
totaly = PolygonStaticX(coordinatesList) / PolygonArea(coordinatesList)
print ("yt:", f"{totaly:11.2f}")

#Ixt
totalIx = PolygonDinamicX(coordinatesList) - ((totalX**2) * PolygonArea(coordinatesList))
print ("Ixt:", f"{totalIx:10.2f}")

#Iyt
totalIy = PolygonDinamicY(coordinatesList) - ((totaly**2) * PolygonArea(coordinatesList))
print ("Ixt:", f"{totalIy:10.2f}")

#Ixyt
totalIxy = PolygonDinamicXY(coordinatesList) + (totalX * totaly * PolygonArea(coordinatesList))
print ("Ixyt:", f"{totalIy:9.2f}")