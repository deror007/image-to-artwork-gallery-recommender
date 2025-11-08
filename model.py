from torchvision import models, transforms
import torch
from torch import nn
from torchvision.models import EfficientNet_V2_M_Weights, EfficientNet_B2_Weights

# Efficient Net Model Setup:
def get_EffNetM_details():
    device = torch.device("cpu")
    model_weights=EfficientNet_V2_M_Weights.DEFAULT
    preprocess = model_weights.transforms() 
    model = models.efficientnet_v2_m(weights=model_weights)
    model = model.to(device)
    model.eval()

    return model, preprocess, device

# Code taken from the blog https://medium.com/@alaeddine.grine/artwork-classification-in-pytorch-b4f3395b877e
def create_effnetMArt_model(num_classes:int=10,
                          seed:int=42,
                          is_TrivialAugmentWide = False,
                          freeze_layers=True):
    """Creates an EfficientNetB2 feature extractor model and transforms.
    Args:
        num_classes (int): number of classes in the classifier head, default = 10
        seed (int): random seed value, default = 42
        is_TrivialAugmentWide (boolean): Artificially increase the diversity of a training dataset with data augmentation.
    Returns:
        effnetb2_model (torch.nn.Module): EfficientNet_B2 model.
        effnetb2_transforms (torchvision.transforms): EfficientNet_B2 image transforms.
    """
    # 0. Select compute location
    device = torch.device("cpu")

    # 1. Create EfficientNet_B2 pretrained weights and transforms
    weights = EfficientNet_V2_M_Weights.DEFAULT
    preprocess = weights.transforms()

    if is_TrivialAugmentWide:
      preprocess = transforms.Compose([
          transforms.TrivialAugmentWide(),
          preprocess,
      ])

    # 2. Create the EfficientNet_B2 model
    model = models.efficientnet_v2_m(weights=weights)
    model = model.to(device)

    # IMPORTANT STAGES FOR FINE-TUNED custom data model:

    # 3. Freeze all layers of the model
    if freeze_layers:
        for param in model.parameters():
            param.requires_grad = False

    # 4. Change classifier head to allow classifier of 10 art styles
    torch.manual_seed(seed)
    model.classifier = nn.Sequential(
        nn.Dropout(p=0.3, inplace=True),
        nn.Linear(in_features=1408, out_features=num_classes),
    )

    #  5. fine-tune model custom data
    
    # model weights:
    # model.load_state_dict(torch.load('EfficientNet_B2_FT.pth',device))

    
    #  6. Set model to inference mode:
    model.eval()
    
    return model, preprocess, device