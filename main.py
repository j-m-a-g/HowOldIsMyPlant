# https://docs.roboflow.com/deploy/hosted-api/custom-models/object-detection

from tkinter import *
from tkinter import ttk

from roboflow import Roboflow

roboflowObject = Roboflow(api_key = "xiu3cjOBKOMlP2zSBvTr")
project = roboflowObject.workspace().project("howoldismyplant")
model = project.version(1).model

# Initialize and create a tkinter window for the user-interface
mainWindow = Tk()
mainWindow.title("How Old Is My Plant?")
mainWindow.geometry("300x300")

# Use inference to print out all_properties from a local image
print(model.predict("https://dam.thdstatic.com/content/production/lh2loaHOQFynCwhJ2EIOUg/Y6kklzWdiWY43H2fqRQKQg/Original%20file/2023_1v2_Low_Maintenance_Indoor.jpg", hosted = True, confidence = 1, overlap = 30).json())

# Create a .jpg image to visually see resulting predictions
model.predict("https://dam.thdstatic.com/content/production/lh2loaHOQFynCwhJ2EIOUg/Y6kklzWdiWY43H2fqRQKQg/Original%20file/2023_1v2_Low_Maintenance_Indoor.jpg", hosted = True, confidence = 1, overlap = 30).save("prediction.jpg")

print()
print()
print(model.predict.__class__)

# Infer on a hosted image
# print(model.predict("URL_OF_YOUR_IMAGE", hosted=True, confidence=40, overlap=30).json())
