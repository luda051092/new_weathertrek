from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Access the API keys from environment variables
OPENWEATHER_API_KEY = os.getenv('OPENWEATHER_API_KEY')
GOOGLE_PLACES_API_KEY = os.getenv('GOOGLE_PLACES_API_KEY')
