from roboflow import Roboflow
import os
import time

def Main():
    os.system("cls")
    
    # Initialize Roboflow project
    roboflowObject = Roboflow(api_key="xiu3cjOBKOMlP2zSBvTr")
    project = roboflowObject.workspace("fx-coding-club-1armu").project("howoldismyplant")
    model = project.version(1).model

    os.system("cls")
    
    agreeingResponsesDictionary = ["y", "Y", "yes", "Yes", "YES"]
    visualizationImageFileName = "HowOldIsMyPlant_box_annotation_visual.png"
    
    # Display content to enter either a local image path or an online image URL for the model to analyze
    print("=== 🪴  How Old Is My Plant? ===")
    
    isHostedOption = input("\nLocal [l/local] or Hosted [h/hosted]?: ")
    if isHostedOption in ["l", "L", "local", "Local", "LOCAL"]:
        imagePathInput = input("\nLocal Image Path: ")
        isHostedBoolean = False
    elif isHostedOption in ["h", "H", "hosted", "Hosted", "HOSTED"]:
        imagePathInput = input("\nOnline Image URL: ")
        isHostedBoolean = True
    else:
        print("\n😵  Oops! Try Again :(\n")
        time.sleep(2)
        Main()


    # Present user with feedback that the model is currently in the process of making a prediction
    print("\nWorking...")
    time.sleep(1)
    
    # Use inference to predict on a hosted image
    prediction_result = model.predict(imagePathInput.strip("\'\""), hosted = isHostedBoolean, confidence = 1, overlap = 30).json()


    # Option of whether to save an individual image that visually displays the predictions derived from the model
    def Save_Predictions_As_Output_Image():
        print("\nWorking...")
        # Create and save a prediction image to visually see resulting predictions
        try:
            model.predict(imagePathInput.strip("\'\""), hosted = isHostedBoolean, confidence = 1, overlap = 30).save(visualizationImageFileName, 8)
            print("Output File: \"/" + visualizationImageFileName + "\"")
            time.sleep(2)
        except:
            print("\nHTTP Error 403: Forbidden")
            time.sleep(2)


    savePredictionsResultImage = input("\nSave the model's predictions as a separate image? (y/yes) [n/no]: ")
    if savePredictionsResultImage in agreeingResponsesDictionary:
        Save_Predictions_As_Output_Image()
    
    
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

    # Create the data structure from the prediction results
    def Create_Data_Structure(prediction_result_param):
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
    data = Create_Data_Structure(prediction_result)

    # Separate keys and values for further analysis
    keys = []
    values = []

    for item in data:
        if isinstance(item, dict):
            keys.extend(item.keys())
            values.extend(item.values())


    print("\nValue Key:", keys)
    print("\nValues:", values)

    # Find the class key and print the plant's age
    if 'class' in keys:
        class_index = keys.index('class')
        if values[class_index] == "soil":
            print("\n\n=== That is just soil! ===\n")
        elif values[class_index] == "harvest":
            print("\n\n=== Your plant is ready to be harvested. ===\n")
        else:
            print("\n\n=== Your plant is about", values[class_index], "old ===\n")


    # Enables the user to restart the program to run the model on another image of their choice
    runOnAnotherImage = input("\nRun model on another image? (y/yes) [n/no]: ")
    if runOnAnotherImage in agreeingResponsesDictionary:
        Main()
    else:
        print()
    
    # if "class"in keys: 
    #     for i in detections: 
    #         width = keys.index("width")
    #         height = keys.index("height")
    #         boxarea = values[width]*values[height]
    #         print(boxarea)


# Call Main
Main()
