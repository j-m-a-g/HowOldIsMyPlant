from roboflow import Roboflow

# Initialize Roboflow project
rf = Roboflow(api_key="xiu3cjOBKOMlP2zSBvTr")
project = rf.workspace("fx-coding-club-1armu").project("howoldismyplant")
model = project.version(1).model
    
# Display content to enter either a local image path or an online image URL
print("\nHow Old Is My Plant?")

isHostedOption = input("\nLocal [l/local] or Hosted [h/hosted]?: ")
if isHostedOption == "l":
    imagePathInput = input("\nLocal Image Path: ")
    isHostedBoolean = False
elif isHostedOption == "local":
    imagePathInput = input("\nLocal Image Path: ")
    isHostedBoolean = False
elif isHostedOption == "h":
    imagePathInput = input("\nOnline Image URL: ")
    isHostedBoolean = True
elif isHostedOption == "hosted":
    imagePathInput = input("\nOnline Image URL: ")
    isHostedBoolean = True
else:
    print("\nOops! Try Again :(")

# Use inference to predict on a hosted image
prediction_result = model.predict(imagePathInput, hosted = isHostedBoolean, confidence = 1, overlap = 30).json()

# Option of whether to save an individual image that visually displays the predictions derived from the model
savePredictionsResultImage = input("Save the model's predictions as a separate image? [y/yes] [n/no]: ")
if savePredictionsResultImage == "y" or "yes":
    # Create and save a prediction image to visually see resulting predictions
    model.predict(imagePathInput, hosted = isHostedBoolean, confidence = 1, overlap = 30).save("predictions.jpg")

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
print("\nFlattened Values:", flat_list)

# Function to create the data structure from the prediction results
def create_data_structure(prediction_result_param):
    data = []
    detections = []

    # Extract the detections from the prediction result
    if isinstance(prediction_result_param, dict) and 'predictions' in prediction_result_param:
        for prediction in prediction_result_param['predictions']:
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
            print()
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

print("\nKeys:", keys)
print("\nValues:", values)

# Find the class key and print the plant's age
if 'class' in keys:
    class_index = keys.index('class')
    print("\nYour plant is", values[class_index], "old")

# if "class"in keys: 
#     for i in detections: 
#         width = keys.index("width")
#         height = keys.index("height")
#         boxarea = values[width]*values[height]
#         print(boxarea)
