from roboflow import Roboflow
import os
import time

os.system("cls")

# Initialize Roboflow project
roboflow_object = Roboflow(api_key="xiu3cjOBKOMlP2zSBvTr")
project = roboflow_object.workspace("fx-coding-club-1armu").project("howoldismyplant")
model = project.version(1).model

def main():
    os.system("cls")
    
    agreeing_responses_dictionary = ["y", "Y", "yes", "Yes", "YES"]
    visualization_image_file_name = "HowOldIsMyPlant_box_annotation_visual.png"
    
    # Display content to enter either a local image path or an online image URL for the model to analyze
    print("=== 🪴  How Old Is My Plant? ===")
    
    is_hosted_option = input("\nLocal [l/local] or Hosted [h/hosted]?: ")
    if is_hosted_option in ["l", "L", "local", "Local", "LOCAL"]:
        image_path_input = input("\nLocal Image Path: ")
        is_hosted_boolean = False
    elif is_hosted_option in ["h", "H", "hosted", "Hosted", "HOSTED"]:
        image_path_input = input("\nOnline Image URL: ")
        is_hosted_boolean = True
    else:
        print("\n😵  Oops! Try Again :(\n")
        time.sleep(2)
        main()


    # Present user with feedback that the model is currently in the process of making a prediction
    print("\nWorking...")
    time.sleep(1)
    
    # Use inference to predict on a hosted image
    prediction_result = model.predict(image_path_input.strip("\'\""), hosted = is_hosted_boolean, confidence = 1, overlap = 30).json()


    # Option of whether to save an individual image that visually displays the predictions derived from the model
    def Save_Predictions_As_Output_Image():
        print("\nWorking...")
        # Create and save a prediction image to visually see resulting predictions
        try:
            model.predict(image_path_input.strip("\'\""), hosted = is_hosted_boolean, confidence = 1, overlap = 30).save(visualization_image_file_name, 8)
            print("Output File: \"/" + visualization_image_file_name + "\"")
            time.sleep(2)
        except:
            print("\nHTTP Error 403: Forbidden")
            time.sleep(2)


    save_predictions_result_image = input("\nSave the model's predictions as a separate image? (y/yes) [n/no]: ")
    if save_predictions_result_image in agreeing_responses_dictionary:
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
    def create_data_structure(prediction_result_param):
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


    print("\nValue Key:", keys)
    print("\nValues:", values)

    # Find the class key and print the plant's age
    if 'class' in keys:
        class_index = keys.index('class')
        if values[class_index] == "soil":
            print("\n\n=== That is just soil! ===\n")
        elif values[class_index] == "harvest":
            print("\n\n=== 🎉  Your plant is ready to be harvested. ===\n")
        else:
            print("\n\n=== 🎉  Your plant is about", values[class_index], "old ===\n")


    # Enables the user to restart the program to run the model on another image of their choice
    run_on_another_image = input("\nRun model on another image? (y/yes) [n/no]: ")
    if run_on_another_image in agreeing_responses_dictionary:
        main()
    else:
        print()
    
    # if "class"in keys: 
    #     for i in detections: 
    #         width = keys.index("width")
    #         height = keys.index("height")
    #         boxarea = values[width]*values[height]
    #         print(boxarea)


# Call main
main()
