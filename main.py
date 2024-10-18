# https://docs.roboflow.com/deploy/hosted-api/custom-models/object-detection

from tkinter import *
from tkinter import ttk
from roboflow import Roboflow

# Initialize Roboflow project
rf = Roboflow(api_key="xiu3cjOBKOMlP2zSBvTr")
project = rf.workspace("fx-coding-club-1armu").project("howoldismyplant")
model = project.version(1).model

# Initialize tkinter window for the user-interface
mainWindow = Tk()
mainWindow.title("How Old Is My Plant?")
mainWindow.geometry("300x300")
predictions_list = []

# Use inference to predict on a hosted image
# image_url = "https://cdn.vectorstock.com/i/1000v/81/68/parts-of-a-plant-vector-1858168.jpg"
image_url = "https://reefertilizer.com/wp-content/uploads/2018/12/IMG_20181219_185434-scaled-e1596134064368.jpg"
prediction_result = model.predict(image_url, hosted=True, confidence=1, overlap=30).json()

# Create and save a prediction image to visually see resulting predictions
model.predict(image_url, hosted=True, confidence=1, overlap=30).save("prediction.jpg")

# Extract values from the prediction result
key_list = []
value_list = []

# Assuming 'predictions' key contains the results
if 'predictions' in prediction_result:
    for prediction in prediction_result['predictions']:
        key_list.append(list(prediction.keys()))
        value_list.append(list(prediction.values()))

# Flatten the value list if there are nested dictionaries
flat_list = []
for item in value_list:
    if isinstance(item, list):
        flat_list.extend(item)
    else:
        flat_list.append(item)

# Print flattened list
print("Flattened Values:", flat_list)

# Function to create the data structure from the prediction results
def create_data_structure(prediction_result):
    data = []
    detections = []

    # Extract the detections from the prediction result
    if isinstance(prediction_result, dict) and 'predictions' in prediction_result:
        for prediction in prediction_result['predictions']:
            detection = {
                'x': prediction.get('x'),
                'y': prediction.get('y'),
                'width': prediction.get('width'),
                'height': prediction.get('height'),
                'confidence': prediction.get('confidence'),
                'class': prediction.get('class'),
                'class_id': prediction.get('class_id'),
                'detection_id': prediction.get('detection_id'),
                'image_path': prediction.get('image_path'),
                'prediction_type': prediction.get('prediction_type')
            }
            detections.append(detection)
            print(detections)
    return detections



# Create data from the prediction result
data = create_data_structure(prediction_result)

# Separate keys and values for further analysis
keys = []
values = []

for item in data:
    if isinstance(item, dict):
        keys.extend(item.keys())
        values.extend(item.values())

print("Keys:", keys)
print("Values:", values)

# Find the class key and print the plant's age
if 'class' in keys:
    class_index = keys.index('class')
    print("Your plant is", values[class_index], "old")

# if "class"in keys: 
#     for i in detections: 
#         width = keys.index("width")
#         height = keys.index("height")
#         boxarea = values[width]*values[height]
#         print(boxarea) 

# Start the Tkinter main loop
mainWindow.mainloop()
