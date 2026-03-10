import torch
from PIL import Image
from transformers import CLIPProcessor, CLIPModel

# Load a lightweight model that understands images and text
model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

categories = ["electronics", "furniture", "fashion", "books", "auto"]

def identify_item_from_image(image_content):
    image = Image.open(image_content)
    inputs = processor(text=categories, images=image, return_tensors="pt", padding=True)
    
    outputs = model(**inputs)
    logits_per_image = outputs.logits_per_image
    probs = logits_per_image.softmax(dim=1) # get probabilities
    
    best_match_idx = probs.argmax().item()
    return categories[best_match_idx]