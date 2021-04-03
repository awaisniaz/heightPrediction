from django.shortcuts import render
from height.ExtraFile.Model import readFile
def showResult(request):
    data = readFile()
    return data
