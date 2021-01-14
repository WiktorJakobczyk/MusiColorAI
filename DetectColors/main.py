import os
from config import *
from PIL import Image
from DetectColors.ColorChar import ColorChar
from DetectColors.Generate import Generate
from DetectColors.AddChords import Chords
from DetectColors.PiePalette import PiePalette

def getColorsFromImage(src):
    img = Image.open(src)
    return PiePalette.get_colors(img)


def writeToCSV(csvSrc, coloursToGetData):
    f = open(csvSrc, "w+")
    f.write("color\n")
    for p in coloursToGetData:
        f.write(f'{PiePalette.RGB2HEX(p)}\n')
    f.close()


def createPlot(src, rowTitle):
    char = ColorChar(src, rowTitle)
    char.createChart()

def getImageEmotions(colours):
    coloursValues = []
    for i in range(len(colours)):
        T1, T2, T3 = PiePalette.happiness(PiePalette.rgb2lab(colours[i]))
        coloursValues.append([T1, T2, T3])
        print(f'Acitvity: -> {T1} \n Weight: -> {T2} \n Heat: -> {T3} \n')  # DEBUG ONLY!!
    return  coloursValues


def getAverageValues():
    averageActivity_ = 0.0
    averageWeight_ = 0.0
    averageHeat_ = 0.0
    for i in coloursValues:
        averageActivity_ += i[0]
        averageWeight_ += i[1]
        averageHeat_ += i[2]

    averageActivity_ /= len(coloursValues)
    averageWeight_ /= len(coloursValues)
    averageHeat_ /= len(coloursValues)

    print(f'==========================')  # DEBUG ONLY!!
    print(f'avActivity: {averageActivity_}')  # DEBUG ONLY!!
    print(f'avWeight: {averageWeight_}')  # DEBUG ONLY!!
    print(f'avHeat: {averageHeat_}')  # DEBUG ONLY!!
    return averageActivity_, averageWeight_, averageHeat_


def deleteOldFiles():
    for count, filename in enumerate(os.listdir(PATH_MELODY)):
        dst = PATH_MELODY+"melody" + str(count) + ".mid"
        os.remove(dst)


def renameFiles():
    for count, filename in enumerate(os.listdir(PATH_MELODY)):
        dst = "melody" + str(count) + ".mid"
        src = PATH_MELODY + filename
        dst = PATH_MELODY + dst
        os.rename(src, dst)


def addChords():
    if averageHeat <= 0.5:
        for i in range(10):
            Chords('attention_improv').addChordsSad('melody' + str(i) + '.mid')
    else:
        for i in range(10):
            Chords('attention_improv').addChordsHappy('melody' + str(i) + '.mid')
if __name__ == '__main__':

    #  Open img, and get dominant colours from it
    #  Second parameter determines number of colors (default=8)
    colours = getColorsFromImage("images/image4.jpg")

    #  Create a CSV file
    #  It will be used later for drawing a pie plot in ColorChar class.
    writeToCSV("charts/dataToChartDominate.csv", colours)

    print(colours)  # DEBUG ONLY!!

    # Create a plot
    # It helps visualize how image dominant colours looks like
    createPlot("charts/dataToChartDominate.csv", "color")

    # Contains 3 values (activity, weight and heat) for all colours from palette.
    coloursValues = getImageEmotions(colours)

    # === DO USUNIECIA
    # Zakładamy, że activity określa 'tempo' to jak energiczny jest utwór
    # Weight ?
    # Heat określa czy utwór będzie wesoły/smutny i jak bardzo.
    # colorsValues przechowuje wartości kolorów z naszej palety.
    # Teraz średnia? inny sposób?
    # ==============

    # Get average values from entire palette
    averageActivity, averageWeight, averageHeat = getAverageValues()

    # Delete old midis
    deleteOldFiles()

    # Decide what model should be used based on averageHeat value.
    if averageHeat<=0.5:
        print(f'SAD Colors')
        Generate('./models/modelSadLookback_rnn.mag','lookback_rnn').generate("[55]")
        # Tempo 90-180 BPM
        tempo = (((averageActivity - 0) * (1.5 - 0.75)) / (1 - 0)) + 0.75
    else:
        print(f'HAPPY Colors')
        Generate('./models/modelHappyLookback_rnn.mag', 'lookback_rnn').generate("[65]")
        # Tempo 78-144 BPM
        tempo = (((averageActivity - 0) * (1.2 - 0.65)) / (1 - 0)) + 0.65
    # TODO: folders
    # Change files names so they will be easier to operate on. e.g 2021-01-06_201919_01.mid to melody0.mid
    renameFiles()

    # Add chords to generated melodies.
    addChords()

    # Create mp3/wav with new tempo/low-pass filter
    # TODO: temp and filter
    from DetectColors.EditMid import EditMid


    print(f'tempo {120/tempo}')   #DEBUG ONLY
    print(f'{120/2}--{120/0.8}')

    print(f'tempo {120 / tempo}')  # DEBUG ONLY

    # retrieving all files in directory PATH_CHORDS
    import glob
    os.chdir(PATH_CHORDS)
    for file in glob.glob("*.mid"):
        midi = EditMid(file, PATH_MUSIC, file)# po przecinku dopisz folder dla plików flac i nazwy tych plików
        midi.change_tempo(tempo,averageWeight)
