import math
from collections import Counter
from operator import itemgetter

from PIL import Image, ImageCms


class PiePalette:

    def RGB2HEX(color):
        return "#{:02x}{:02x}{:02x}".format(int(color[0]), int(color[1]), int(color[2]))

    def get_colors(img, numcolors = 9, resize = 150):
        # Resize image to speed up processing
        # imgSrc.thumbnail((resize, resize))

        from .colorthiefTest import ColorThief2
        color_thief = ColorThief2(img)
        palette = color_thief.get_palette(color_count=numcolors, quality=1)

        print(f'Thief : {palette}')
        print(f'Color :{color_thief.get_color(quality=1)}')

        palette2 = []
        paletteValues = []
        for color in palette:
            palette2.append(color[:3])
            paletteValues.append(color[3:])

        print(palette2)
        print(paletteValues)
        return palette2, paletteValues

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

