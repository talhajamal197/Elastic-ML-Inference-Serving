# model.py
import torch
import torchvision.models as models
import torchvision.transforms as transforms
from PIL import Image
import io

model = models.resnet18(pretrained=True)
model.eval()

preprocess = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])

with open("imagenet_classes.txt") as f:
    labels = [line.strip() for line in f.readlines()]


def predict(image_bytes):
    img = Image.open(io.BytesIO(image_bytes))
    img_tensor = preprocess(img).unsqueeze(0)

    with torch.no_grad():
        output = model(img_tensor)

    _, predicted_idx = torch.max(output, 1)
    return labels[predicted_idx.item()]
