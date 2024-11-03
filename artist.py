import base64
from io import BytesIO
from PIL import Image
from config import openai

ARTIST_MODEL = "dall-e-3"
IMAGE_SIZE = "1024x1024"

def artist(city):
    prompt = f"""
    An image representing a vacation in {city}, 
    showing tourist spots and everything unique about {city}, 
    in a vibrant pop-art style
    """
    image_response = openai.images.generate(
        model=ARTIST_MODEL,
        prompt=prompt,
        size=IMAGE_SIZE,
        n=1,
        response_format="b64_json",
    )
    image_base64 = image_response.data[0].b64_json
    image_data = base64.b64decode(image_base64)
    return Image.open(BytesIO(image_data))
