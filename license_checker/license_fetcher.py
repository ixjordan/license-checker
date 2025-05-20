import requests

API_KEY = "434df902ecdedd73db413f1896d1df12"

def fetch_license(package_name):
    """
    Fetch a license of a given package from libraries.io

    Args:
         package_name(str): Name of the Python package (e.g. 'requests')

    Return:
        str or None: License type (e.g, 'MIT', 'GPL-3.0'), or None if not found
    """
    url = f"https://libraries.io/api/pypi/{package_name}?api_key={API_KEY}"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        return data.get("licenses")
    except Exception as e:
        print(f"[!] Failed to fetch license for {package_name}: {e}")
        return None

if __name__ == "__main__":
    print(fetch_license("requests"))