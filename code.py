from turtle import position
import plotly.express as px
import csv
import numpy as np

def plotFigure(data_path):
    with open(data_path) as csv_file:
        df = csv.DictReader(csv_file)
        fig = px.scatter(df,x="Position In Class", y="Marks In Percentage")
        fig.show()

def getDataSource(data_path):
    marks_in_percentage = []
    position_in_class = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            marks_in_percentage.append(float(row["Marks In Percentage"]))
            position_in_class.append(float(row["Position In Class"]))

    return {"x" : marks_in_percentage, "y": position_in_class}

def setup():
    data_path  = "./Student Marks vs Position In Class.csv"

    datasource = getDataSource(data_path)
    plotFigure(data_path)

setup()