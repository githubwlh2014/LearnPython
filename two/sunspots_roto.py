from reportlab.lib import colors
from reportlab.graphics.shapes import *
from reportlab.graphics import renderPDF
from reportlab.graphics.charts.lineplots import LinePlot
from reportlab.graphics.charts.textlabels import Label

data = [  
#    Year  Month  Predicted  High  Low  
    (2007,  8,    113.2,     114.2, 112.2),  
    (2007,  9,    112.8,     115.8, 109.8),  
    (2007, 10,    111.0,     116.0, 106.0),  
    (2007, 11,    109.8,     116.8, 102.8),  
    (2007, 12,    107.3,     115.3,  99.3),  
    (2008,  1,    105.2,     114.2,  96.2),  
    (2008,  2,    104.1,     114.1,  94.1),  
    (2008,  3,     99.9,     110.9,  88.9),  
    (2008,  4,     94.8,     106.8,  82.8),  
    (2008,  5,     91.2,     104.2,  78.2),  
    ]

drawing=Drawing(400,200)

pred=[row[2]-40 for row in data]
high=[row[3]-40 for row in data]
low=[row[4]-40 for row in data]
times=[(row[0]+row[1]/12.0) for row in data]

lp=LinePlot()
lp.x=50
lp.y=50
lp.height=125
lp.width=300
lp.data=[zip(times,pred),zip(times,high),zip(times,low)]

drawing.add(lp)
drawing.add(String(250,150,'Sunspots',fontSize=14,fillColor=colors.red))

renderPDF.drawToFile(drawing,'report.pdf','sunspots')



#drawing.add(PolyLine(zip(times,pred),strokeColor=colors.blue))
#drawing.add(PolyLine(zip(times,high),strokeColor=colors.red))
#drawing.add(PolyLine(zip(times,low),strokeColor=colors.green))
#drawing.add(String(65,115,'Sunspots',fontSize=18,fillColor=colors.red))

#renderPDF.drawToFile(drawing,'report1.pdf','Sunspots')
