from roboflow import Roboflow

roboflowObject = Roboflow(api_key="xiu3cjOBKOMlP2zSBvTr")
project = roboflowObject.workspace().project("howoldismyplant")
model = project.version(1).model

# infer on a local image
print(model.predict("C:/Users/Joseph/Downloads/money-tree-plant-royalty-free-image-1726508639.jpg", confidence=1, overlap=30).json())

# visualize your prediction
model.predict("C:/Users/Joseph/Downloads/money-tree-plant-royalty-free-image-1726508639.jpg", confidence=1, overlap=30).save("prediction.jpg")

# infer on an image hosted elsewhere
# print(model.predict("URL_OF_YOUR_IMAGE", hosted=True, confidence=40, overlap=30).json())
