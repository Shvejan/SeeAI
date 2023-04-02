# SeeAI

Introducing **SeeAI** - **the revolutionary AI-powered smart sunglasses designed to enhance accessibility for the visually impaired.**

![SeeAI Demo](SeeAI.png)
<h1 align="center"> Making Accessibility a Reality </h1>


## Features

SeeAI is powered by Hugging Face transformers and a state-of-the-art facial recognition system. It is capable of giving the user a completely hands-free experience helping them understand the world better through audio-based instructions. 

Some of the key features of SeeAI are:

- Facial recognition: SeeAI is equipped with DeepFace, one of the best facial recognition models in the market. It can identify, remember (registering a new face), and recognize people (detecting unknown face detected and calling 911).

- Traffic mode: SeeAI can help the visually impaired cross the road. With the Hugging Face vision transformer, the model can recognize various traffic signs like walk-sign, wait-sign, etc. and guide the user to take action accordingly.

- Video call assistance: If the user is not confident with the instructions that the model is giving or if they require additional assistance, SeeAI's innovative design allows the user to easily make a video call to someone simply by long-pressing the button on the glasses. A live video will be streamed to another person, who can give live instructions through the call.

## Files in the SeeAI repo:

| File Name        | Description           |
| ----------------|-----------------------|
| cassFiles        | Contains files related to haar cascade classifiers |
| db               | Database of face images that are registered |
| .gitignore       | Git ignore file for the repository |
| app.py           | Main application file - Flask Sever Applicationn |
| call_face_rec.py | Python module for making calls to facial recognition model |
| cap.py           | Python module for capturing images |
| curr_img.png     | Image frame for facial recognition |
| face_rec.py      | Python module for facial recognition |
| multi.png        | Example image for multi-face detection |
| multi_both.png   | Example image for both face detection and facial recognition |
| multiface.jpg    | Example image for multi-face detection |
| nb.ipynb         | Jupyter Notebook for testing the facial recognition model |
| test.py          | Python script for testing the application |

## Technology Stacks used:

- Machine Learning and AI: Powered by SOTA (State of the ART) models using Hugging Face transformers, RESNET for Image Classification, Open AI clip for converting the image to text with little information given as prompts, VIT GPT-2 for converting images to Text Captions. 
- Twillio: For having a video conferencing solution by adding custom made tasks. Used NgRock, i.e for creating a Public IP. Main functionality of NgRock is to redirect all the calls from the IP to the local host.
- Github: Utilized Github for code versioning, collaborating and to have the entire code structure with all the data stored in a remote place for easy accessibility and collaboration between people on the team.

## Usage

To use SeeAI, simply put on the smart sunglasses and interact with the device through voice commands or button presses. SeeAI will provide audio instructions based on what it sees and recognizes.


