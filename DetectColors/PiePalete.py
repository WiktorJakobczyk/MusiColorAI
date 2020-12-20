import math
import os

from PIL import Image, ImageCms
from DetectColors.testChar import TestChar
from skimage import io, color
from DetectColors.Generate import Generate
from DetectColors.AddChords import Chords


def RGB2HEX(color):
    return "#{:02x}{:02x}{:02x}".format(int(color[0]), int(color[1]), int(color[2]))

def get_colors(img, numcolors=8, resize=150):
    # Resize image to speed up processing
    #img = Image.open(image_file)
    img2 = img.copy()
    img2.thumbnail((resize, resize))
    palette = img2.convert('P', palette=Image.ADAPTIVE, colors=numcolors).getpalette()
    temp= []


    z = 0
    for i in range(numcolors):
        dominant_color = palette[z*3:z*3+3]
        #temp.append(RGB2HEX(dominant_color))
        temp.append(dominant_color)
        z += 1

    return temp

#https://gist.github.com/manojpandey/f5ece715132c572c80421febebaf66ae
def rgb2lab(inputColor):

    num = 0
    RGB = [0, 0, 0]

    for value in inputColor:
        value = float(value) / 255

        if value > 0.04045:
            value = ((value + 0.055) / 1.055) ** 2.4
        else:
            value = value / 12.92

        RGB[num] = value * 100
        num = num + 1

    XYZ = [0, 0, 0, ]

    X = RGB[0] * 0.4124 + RGB[1] * 0.3576 + RGB[2] * 0.1805
    Y = RGB[0] * 0.2126 + RGB[1] * 0.7152 + RGB[2] * 0.0722
    Z = RGB[0] * 0.0193 + RGB[1] * 0.1192 + RGB[2] * 0.9505
    XYZ[0] = round(X, 4)
    XYZ[1] = round(Y, 4)
    XYZ[2] = round(Z, 4)

    # Observer= 2°, Illuminant= D65
    XYZ[0] = float(XYZ[0]) / 95.047         # ref_X =  95.047
    XYZ[1] = float(XYZ[1]) / 100.0          # ref_Y = 100.000
    XYZ[2] = float(XYZ[2]) / 108.883        # ref_Z = 108.883

    num = 0
    for value in XYZ:

        if value > 0.008856:
            value = value ** (0.3333333333333333)
        else:
            value = (7.787 * value) + (16 / 116)

        XYZ[num] = value
        num = num + 1

    Lab = [0, 0, 0]

    L = (116 * XYZ[1]) - 16
    a = 500 * (XYZ[0] - XYZ[1])
    b = 200 * (XYZ[1] - XYZ[2])

    Lab[0] = round(L, 4)
    Lab[1] = round(a, 4)
    Lab[2] = round(b, 4)

    return Lab


def happiness(labCol):
    L = labCol[0]
    a = labCol[1]
    b = labCol[2]

    if(a==0):
        h = math.atan(0)
    else:
        h = math.atan(b/a)

    C = math.sqrt(pow(a,2)+pow(b,2))

    #print(f':{h}     {100*math.pi/180}')
    activity = -2.1+0.06*pow(pow((L-50),2)+pow((a-3),2)+pow(((b-17)/1.4),2),0.5)

    weight = -1.8+0.04*(100-L)+0.45*math.cos(h-100*math.pi/180)   #radiany!!

    heat = -0.5+0.02*pow(C,1.07)*math.cos(h-50*math.pi/180)       #radiany!!

    # MAXACTIVITY 5.017957093644959 :--: -2.0878870802859097
    MAXACTIVITY = 5.02
    MINACTIVITY = -2.09

    # MAXWEIGHT 2.615768733298268 :--: -2.2421824049799692
    MAXWEIGHT = 2.616
    MINWEIGHT = -2.243


    # Heat: 2.352146795189135 :--: -2.3062644060080473
    MAXHEAT = 2.353
    MINHEAT = - 2.307

    activityNorm = (activity+math.fabs(MINACTIVITY))/(MAXACTIVITY+math.fabs(MINACTIVITY))
    weightNorm = (weight+math.fabs(MINWEIGHT))/(MAXWEIGHT+math.fabs(MINWEIGHT))
    heatNorm = (heat+math.fabs(MINHEAT))/(MAXHEAT+math.fabs(MINHEAT))


    return activityNorm, weightNorm, heatNorm

if __name__ == '__main__':
    img = Image.open("images/image8.jpg")
    #input_file = 'images/image3.jpg'
    colors = get_colors(img)

    f = open("charts/dataToChartDominate.csv", "w+")
    f.write("color\n")
    for p in colors:
         f.write(f'{RGB2HEX(p)}\n')

    f.close()
    print(colors)

    char = TestChar("charts/dataToChartDominate.csv", "color")
    char.createChart()

    width, height = img.size
    colorsValues = []

    for i in range(len(colors)):
        T1,T2,T3=happiness(rgb2lab(colors[i]))
        colorsValues.append([T1,T2,T3])
        print(f'Acitvity: -> {T1} \n Weight: -> {T2} \n Heat: -> {T3} \n')


    # Zakładamy, że activity określa 'tempo' to jak energiczny jest utwór
    # Weight ?
    # Heat określa czy utwór będzie wesoły/smutny i jak bardzo.
    # colorsValues przechowuje wartości kolorów z naszej palety.

    # Teraz średnia? inny sposób?
    averageActivity = 0.0
    averageWeight = 0.0
    averageHeat = 0.0
    for i in colorsValues:
        averageActivity += i[0]
        averageWeight += i[1]
        averageHeat += i[2]

    averageActivity /= len(colorsValues)
    averageWeight /= len(colorsValues)
    averageHeat /= len(colorsValues)

    print(f'==========================')
    print(f'avActivity: {averageActivity}')
    print(f'avWeight: {averageWeight}')
    print(f'avHeat: {averageHeat}')

    if averageHeat<=0.5:
        Generate('./models/modelSadLookback_rnn.mag','lookback_rnn').generate()
    else:
        Generate('./models/modelHappyLookback_rnn.mag', 'lookback_rnn').generate()

    # Zmiana nazwy plikow

    for count, filename in enumerate(os.listdir("F:/tmp/melody_rnn/generatedFromColor/")):
        dst = "melody" + str(count) + ".mid"
        src = 'F:/tmp/melody_rnn/generatedFromColor/' + filename
        dst = 'F:/tmp/melody_rnn/generatedFromColor/' + dst

        # rename() function will
        # rename all the files
        os.rename(src, dst)

    # Dodanie akordów
    for i in range(10):
        Chords('attention_improv').addChordsHappy('melody'+str(i)+'.mid')
        # melody5.mid

        # FIND MAX

    # maxAcitivty = 0.0
    # minAcitivty = 1000000.0
    # maxWeight = 0.0
    # minWeight = 1000000.0
    # maxHeat = 0.0
    # minHeat = 1000000.0

    # test = False
    # for r in range(256):
    #     for g in range(256):
    #         for b in range(256):
    #             c = (r, g, b)
    #             T1, T2, T3 = happiness(rgb2lab(c))
    #             maxAcitivty = max(T1, maxAcitivty)
    #             minAcitivty = min(T1, minAcitivty)
    #             maxWeight = max(T2, maxWeight)
    #             minWeight = min(T2, minWeight)
    #             maxHeat = max(T3, maxHeat)
    #             minHeat = min(T3, minHeat)
    #     #         if(T3<= 0.3):
    #     #             test= True
    #     #             print(f'TOTO: {c}')
    #     #             break
    #     #     if(test):
    #     #         break
    #     # if(test):
    #     #     break
    #
    # # print(f'maxAc: {maxAcitivty} \n maxWe: {maxWeight}\n maxHeat: {maxHeat}')
    # print(f'Activity: {maxAcitivty} :--: {minAcitivty} \n')
    # print(f'Weight: {maxWeight} :--: {minWeight} \n')
    # print(f'Heat: {maxHeat} :--: {minHeat} \n')
    #
    # # Convert to Lab colourspace
    #
    # print(rgb2lab([0,255,0]))

