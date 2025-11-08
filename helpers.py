from PIL import Image
import torch
import requests
from io import BytesIO


def load_image(image_path, preprocess, device):
    image = Image.open(image_path).convert('RGB')
    image = preprocess(image)
    image = image.unsqueeze(0).to(device)
    return image

def load_url_image(url, preprocess, device):
    response = requests.get(url)
    image = Image.open(BytesIO(response.content)).convert('RGB')
    image = preprocess(image)
    image = image.unsqueeze(0).to(device)
    return image

def get_image_embedding(model, image_tensor):
    
    # Put model into evaluation mode and turn on inference mode
    with torch.no_grad():
        embedding = model(image_tensor)
        
    return embedding.cpu().numpy()



