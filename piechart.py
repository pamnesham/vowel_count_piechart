import turtle
import math

#This function finds the frequency of vowels in a string
def vowelCount(astring):
    a = 0
    e = 0
    i = 0
    o = 0
    u = 0
    freqList = []
    r = 150
    for x in astring:
        if x == 'A' or x == 'a':
            a += 1
        elif x == 'E' or x == 'e':
            e += 1
        elif x == 'I' or x == 'i':
            i += 1
        elif x == 'O' or x == 'o':
            o += 1
        elif x == 'U' or x == 'u':
            u += 1
        freqList = [a, e, i, o, u]
        total = sum(freqList)
    if a ==0 and e == 0 and i == 0 and o == 0 and u == 0:
        deg = 0
        turtle.pu()
        xcor = r*math.cos(deg)
        ycor = r*math.sin(deg)
        turtle.goto(xcor, ycor)
        turtle.pd()
        while deg <= math.radians(360):
            xcor = r*math.cos(deg)
            ycor = r*math.sin(deg)
            turtle.goto(xcor, ycor)
            deg += math.radians(1)
        turtle.pu()
        turtle.goto(-100,175)
        turtle.write("There are no vowels.", font = ("Papyrus", 15, "bold"))
        turtle.exitonclick()
    else:
        for each in range(len(freqList)):
            freqList[each] = freqList[each]/total*360
    return freqList

#This function creates a piechart based on vowel frequencies
def pieChart(flist):
    turtle.pensize(width = 2.4)
    r = 150
    colors = ['#48C48E', '#E0EF69', '#F6943D', '#13799F', '#C95264']
    colorIndex = 0
    angleEndpoint = 0
    labels = ["A", "E", "I", "O", "U"]
    #if there are no vowels:
    if sum(flist) == 0:
        turtle.exitonclick()
    #if there are vowels:
    else:
        turtle.pu()
        turtle.goto(-85,175)
        turtle.write("Vowel Frequencies", font = ("Arial", 15, "normal"))
        turtle.goto(0, 0)
    for index, vowFreq in enumerate(flist):
        vowFreq = math.radians(vowFreq)
        angleEndpoint += vowFreq
        pieSliceWidth = angleEndpoint - vowFreq
        xcor = r*math.cos(pieSliceWidth)
        ycor = r*math.sin(pieSliceWidth)
        turtle.fillcolor(colors[colorIndex])
        turtle.begin_fill()
        turtle.goto(xcor, ycor)
        turtle.pd()
        #create the arc for each pie slice:
        while pieSliceWidth < angleEndpoint:
            xcor = r*math.cos(pieSliceWidth)
            ycor = r*math.sin(pieSliceWidth)
            turtle.goto(xcor, ycor)
            pieSliceWidth += math.radians(1)
        turtle.goto(0,0)
        turtle.end_fill()
        colorIndex += 1
        #label each pie slice:
        if flist[index] > 0:
            xcor = 120*math.cos(angleEndpoint - (vowFreq/2))
            ycor = 120*math.sin(angleEndpoint - (vowFreq/2))
            turtle.pu()
            turtle.goto(xcor, ycor)
            turtle.write(labels[index], font = ("Arial", 9, "normal"))
            turtle.goto(0,0)

#Function that calls pieChart function on vowelCount function
def main():
    turtle.delay(0)
    turtle.hideturtle()
    stringInput = turtle.textinput("Vowel Frequency","Enter a string.")
    pieChart(vowelCount(stringInput))
    turtle.hideturtle()


if __name__ == '__main__':
    main()
