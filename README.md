# 🪴 How Old Is My Plant

### See how old your potted plant might be in a range of 1-4 weeks or if it is ready to be harvested!

Built with the Roboflow ```inference``` API and pipelines.

## ▶️ How to Run

1. Simply **FORK** and clone the repository onto your local machine or download it as a standalone ZIP file
2. If you do not have Python already, download and install it through the [python.org](https://www.python.org) website. Note that these modules only support Python versions 3.8 and higher - as of writing this
3. Run ```pip install inference``` and then ```pip install inference-sdk``` in your terminal (either globally or under a Python virtual environment with the repository) to get the prerequisite APIs and other Python modules successfully installed
4. Then, run the ```main.py``` file with the ```py main.py``` terminal command OR in your favorite Python-supporting IDE and follow the friendly on-screen text prompts to select an image and its type and choose whether to save a separate PNG output with the model's visualized predictions
   - Image Types:
     - ```Local``` - referring to the image being directly accessed through a path on your own filesystem. Or...
     - ```Hosted``` - with the image being on the internet, per se, or any other file-sharing network
5. Finally, wait a couple of seconds for the model to, "do its magic" and spew out its predictions as a flattened list of values as well as individual dictionaries and ultimately tell you how old your plant is - although this, "estimate" might not be extremely accurate. Hence, take it with a grain of salt :(
