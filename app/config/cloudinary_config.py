import cloudinary
import os
import stripe
from dotenv import load_dotenv

load_dotenv()

cloudinary.config(
  cloud_name=os.getenv('CLOUDINARY_NAME'),
  api_key=os.getenv('CLOUDINARY_API_KEY'),
  api_secret=os.getenv('CLOUDINARY_SECRET_KEY')
)
stripe.api_key = os.getenv("STRIPE_SECRET_KEY")

