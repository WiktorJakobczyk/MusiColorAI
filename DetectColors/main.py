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


def getAverageValues(coloursValues):
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
    for count, filename in enumerate(os.listdir(PATH_CHORDS)):
        dst = PATH_CHORDS+"chord" + str(count) + ".mid"
        os.remove(dst)


def renameFiles(path,name):
    for count, filename in enumerate(os.listdir(path)):
        dst = name + str(count) + ".mid"
        src = path + filename
        dst = path + dst
        os.rename(src, dst)


def addChords(averageHeat):
    if averageHeat <= 0.5:
        #for i in range(10):
            Chords('attention_improv').addChordsSad('melody' + str(0) + '.mid')
    else:
        #for i in range(10):
            Chords('attention_improv').addChordsHappy('melody' + str(0) + '.mid')
#if __name__ == '__main__':
def music():


    #  Open img, and get dominant colours from it
    #  Second parameter determines number of colors (default=8)
    colours = getColorsFromImage("F:/Python/NEW/MusiColorAI/MusiColorFlask/static/uploads/image.jpg")

    #  Create a CSV file
    #  It will be used later for drawing a pie plot in ColorChar class.
    writeToCSV("F:/Python/NEW/MusiColorAI/DetectColors/charts/dataToChartDominate.csv", colours)

    print(colours)  # DEBUG ONLY!!

    # Create a plot
    # It helps visualize how image dominant colours looks like
    #createPlot("F:/Python/NEW/MusiColorAI/DetectColors/charts/dataToChartDominate.csv", "color")

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
    averageActivity, averageWeight, averageHeat = getAverageValues(coloursValues)

    # Delete old midis
    deleteOldFiles()

    # HAPPY:
    # 1-0.9 C4
    # 0.9-0.8 D4
    # 0.8-0.7 F4
    # 0.7-0.6 A4
    # 0.6-0.5 C5
    # 0.5-0.4 D5
    # 0.4-0.3 E5
    # 0.3-0.2 C6
    # 0.2-0.1 D6
    # 0.1-0 to E6
    happyList = ['E6', 'D6', 'C6', 'E5', 'D5', 'C5', 'A4', 'F4', 'D4', 'C4']
    # SAD:
    # 1-0.9 C2
    # 0.9-0.8 D2
    # 0.8-0.7 F2
    # 0.7-0.6 G2
    # 0.6-0.5 A2
    # 0.5-0.4 C3
    # 0.4-0.3 E3
    # 0.3-0.2 F3
    # 0.2-0.1 B3
    # 0.1-0 to C4
    sadList = ['C4-', 'B3-', 'F3-', 'E3-', 'C3-', 'A2-', 'G2-', 'F2-', 'D2-', 'C2-']


    # Decide what model should be used based on averageHeat value.
    if averageHeat<=0.5:
        print(f'SAD Colors')
        Generate('F:/Python/NEW/MusiColorAI/DetectColors/models/modelSadLookback_rnn.mag','lookback_rnn').generate("[60]")

        # Tempo 78-144 BPM
        tempo = (((averageActivity - 0) * (1.2 - 0.65)) / (1 - 0)) + 0.65
        index=int(averageWeight*10)
        key =sadList[index]

    else:
        print(f'HAPPY Colors')
        Generate('F:/Python/NEW/MusiColorAI/DetectColors/models/modelHappyLookback_rnn.mag', 'lookback_rnn').generate("[60]")
        # Tempo 90-180 BPM
        tempo = (((averageActivity - 0) * (1.5 - 0.75)) / (1 - 0)) + 0.75
        index = int(averageWeight * 10)
        print(f'index: {index}')
        key = happyList[index]
        print(f'key: {key}')

    # TODO: folders
    # Change files names so they will be easier to operate on. e.g 2021-01-06_201919_01.mid to melody0.mid
    renameFiles(PATH_MELODY, 'melody')

    # Add chords to generated melodies.
    addChords(averageHeat)

    renameFiles(PATH_CHORDS, 'chord')

    # Create mp3/wav with new tempo/low-pass filter
    # TODO: temp and filter
    from DetectColors.EditMid import EditMid


    print(f'tempo {tempo} "  " {120* tempo}')  # DEBUG ONLY




    # retrieving all files in directory PATH_CHORDS
    import glob
    os.chdir(PATH_CHORDS)
    for file in glob.glob("*.mid"):
        print(f'file: {file}')
        midi = EditMid(file, PATH_MUSIC, file,PATH_MUSIC) # po przecinku dopisz folder dla plików flac i nazwy tych plików
        midi.change_tempo(fctr=tempo,weight=averageWeight,key=key)
    os.chdir(PATH_MUSIC)
    for file in glob.glob("*.mid"):
        midi = EditMid(file, PATH_MUSIC, file, PATH_MUSIC)
        midi.export('F:/Python/NEW/MusiColorAI/DetectColors/soundfonts/full_grand_piano.sf2')

    # Delete old midis
    # deleteOldFiles()
    return 0