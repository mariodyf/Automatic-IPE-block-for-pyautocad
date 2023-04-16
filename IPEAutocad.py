from pyautocad import Autocad, APoint, aDouble
from math import pi
acad = Autocad()

print("Elige el perfil IPE")

#Loop that verifies numeric input
while True:
    iHeight = input("Canto de perfil en mm:")
    try:
        int_Height = int(iHeight)
        break
    except:
        print("Error, introduce un número válido")
        continue
str_Height = str(int_Height)

print("Perfil seleccionado: IPE " + str_Height)

#IPE dimensions
variables_IPE = {
    "IPE_80": [0.08,0.046,0.0038,0.0052,0.005],
    "IPE_100": [0.10,0.055,0.0041,0.0057,0.007],
    "IPE_120": [0.12,0.064,0.0044,0.0063,0.007],
    "IPE_140": [0.14,0.073,0.0047,0.0069,0.007],
    "IPE_160": [0.16,0.082,0.005,0.0074,0.009],
    "IPE_180": [0.18,0.091,0.0053,0.008,0.009],
    "IPE_200": [0.20,0.100,0.0056,0.0085,0.012],
    "IPE_220": [0.22,0.11,0.0059,0.0092,0.012],
    "IPE_240": [0.24,0.12,0.0062,0.0098,0.015],
    "IPE_270": [0.27,0.135,0.0066,0.0102,0.015],
    "IPE_300": [0.30,0.15,0.0071,0.0107,0.015],
    "IPE_330": [0.33,0.16,0.0075,0.0115,0.018],
    "IPE_360": [0.36,0.17,0.008,0.0127,0.018],
    "IPE_400": [0.40,0.18,0.0086,0.0135,0.021],
    "IPE_450": [0.45,0.19,0.0094,0.0146,0.021],
    "IPE_500": [0.50,0.20,0.0102,0.016,0.021],
    "IPE_550": [0.55,0.21,0.0111,0.0172,0.024],
    "IPE_600": [0.60,0.22,0.012,0.019,0.024]
}

#variables IPE seleccionado
h = variables_IPE["IPE_"+str_Height][0]
b = variables_IPE["IPE_"+str_Height][1]
e1 = variables_IPE["IPE_"+str_Height][2]
e2 = variables_IPE["IPE_"+str_Height][3]
r = variables_IPE["IPE_"+str_Height][4]

#puntos del perfil
p0 = APoint(0, 0)
p1 = APoint(0, e2)
p2 = APoint(((b/2)-(e1/2)-r), e2)
p3 =APoint(((b/2)-(e1/2)), e2+r)
p4 = APoint(((b/2)-(e1/2)), (h-e2)-r)
p5 = APoint(((b/2)-(e1/2)-r), (h-e2))
p6 = APoint(0, (h-e2))
p7 = APoint(0, h)
p8 = APoint(b, h)
p9 = APoint(b, (h-e2))
p10 = APoint(((b/2)+(e1/2)+r), (h-e2))
p11 = APoint(((b/2)+(e1/2)), (h-e2-r))
p12 = APoint(((b/2)+(e1/2)), e2+r)
p13 = APoint(((b/2)+(e1/2)+r), e2)
p14 = APoint(b, e2)
p15 = APoint(b, 0)
p16 = p0

#Group points in dictionary
pointsList = [p0,p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14,p15,p16]
pointsDict = {}
for i in range(0,17):
    pointsDict["p{0}".format(i)] = pointsList[i]

#Block name
blockName = "IPE_"+str_Height

#Define block
acad.doc.Blocks.Add(p0,blockName)
blockIPE = acad.doc.Blocks.Item(blockName)

#Draw lines
count = 0
lines = {}
for i in range(0,16):
    lines["line{0}".format(i)] = blockIPE.AddLine(pointsDict["p"+str(count)],pointsDict["p"+str(count+1)])
    count = count + 1

#Delete extra lines
lines["line2"].delete()
lines["line4"].delete()
lines["line10"].delete()
lines["line12"].delete()

#Draw arcs

p2_3center = APoint(p2.x, p3.y, 0)
p4_5center = APoint(p5.x, p4.y, 0)
p10_11center = APoint(p10.x, p11.y, 0)
p12_13center = APoint(p13.x, p12.y, 0)

p2_3arc = blockIPE.AddArc(p2_3center, r, -pi/2, 0)
p4_5arc = blockIPE.AddArc(p4_5center, r, 0, pi/2)
p10_11arc = blockIPE.AddArc(p10_11center, r, pi/2, -pi)
p12_13arc = blockIPE.AddArc(p12_13center, r, pi, -pi/2)

acad.model.InsertBlock(p0,blockName,1,1,1,0)
acad.app.ZoomWindow(p0,p8)
print("Programa finalizado con éxito")
