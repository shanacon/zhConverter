
import os
from zhconv import convert
def Convert(InputData):
    ConvertData = convert(InputData,'zh-tw')
    return ConvertData

def ConvertAss(InputList):
    ConvertData = ""
    for line in InputList:
        former = line.split(':')[0]
        if former == "Style" :
            style = line.split(':')[1].split(',')[0]
            ConvertData += line.replace(style, convert(style ,'zh-tw')) 
        elif former == "Dialogue" :
            ConvertData += convert(line,'zh-tw')
        else :
            ConvertData += line
    return ConvertData

def Output_Cover(ConvertData, FilePath) :
    with open(FilePath, "w", encoding='utf-8') as WriteF:
        WriteF.write(ConvertData)

def Output_NoCover(ConvertData, path, OutputPath):
    FileName = os.path.basename(path)
    with open(OutputPath + '/' + FileName, "w", encoding='utf-8') as WriteF:
        WriteF.write(ConvertData)