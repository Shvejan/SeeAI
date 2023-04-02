import torch
import torchvision.transforms as transforms
from PIL import Image
import numpy as np


def predict_traffic_sign():
    # Define the transformations
    image_path = './curr_img.png'
    transform = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(
            mean=[0.485, 0.456, 0.406],
            std=[0.229, 0.224, 0.225]
        )
    ])

    device = torch.device(
        'cuda') if torch.cuda.is_available() else torch.device('cpu')

    # Load the image
    image = Image.open(image_path)

    # Preprocess the image
    image_tensor = transform(image)

    # Add a batch dimension
    image_tensor = torch.unsqueeze(image_tensor, 0)

    # Load the model
    model = torch.load("model_traffic.pt", map_location=device)
    model.to(device)

    # Switch the model to evaluation mode
    model.eval()

    # Make the prediction
    with torch.no_grad():
        output = model(image_tensor.to(device))

    # Process the output to get the prediction
    output = output.cpu().numpy()
    result = output[0].argmax()

    if result == 0:
        return "Please Stop, It's a Stop Sign"
    else:
        return "Please Cross the Road, It's a Walk Sign"


