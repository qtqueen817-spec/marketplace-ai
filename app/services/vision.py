import os
import google.generativeai as genai
from PIL import Image
from dotenv import load_dotenv

load_dotenv()

# Configure the Gemini API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel('gemini-1.5-flash')

def identify_item_from_image(image_path: str):
    """
    Analyzes an image and returns a marketplace category.
    """
    try:
        img = Image.open(image_path)
        prompt = "Look at this item. Return only: Category (Electronics, Fashion, or Furniture) and a 1-word name."
        
        response = model.generate_content([prompt, img])
        return response.text.strip()
    except Exception as e:
        return f"AI Error: {str(e)}"