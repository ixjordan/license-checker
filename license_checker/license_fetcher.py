import os
import requests
from dotenv import load_dotenv
from . import cli

load_dotenv()


API_KEY = os.getenv("libraries.io-API_KEY")
if not API_KEY:
    raise ValueError(f"Libraries.io API key not found {API_KEY}")


def fetch_license(package_name, package_type):
    """
    Fetch a license of a given package from libraries.io

    Args:
         package_name(str): Name of the Python package (e.g. 'requests')
         package_type(str): package type, (pypi, npm ect)

    Return:
        str or None: License type (e.g, 'MIT', 'GPL-3.0'), or None if not found
    """
    url = f"https://libraries.io/api/{package_type}/{package_name}?api_key={API_KEY}"

    try:
        # get request using specified url
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        return data.get("licenses")
    except Exception as e:
        print(f"[!] Failed to fetch license for {package_name}: {e}")
        return None

if __name__ == "__main__":
    print(fetch_license("requests", "npm"))