import requests
import shutil

def remove_background_with_api(api_key, input_image_path, output_image_path):
    url = "https://api.remove.bg/v1.0/removebg"
    headers = {
        "X-Api-Key": api_key
    }
    data = {
        "image_file": open(input_image_path, "rb")
    }

    response = requests.post(url, headers=headers, files=data, stream=True)

    if response.status_code == 200:
        with open(output_image_path, 'wb') as out_file:
            shutil.copyfileobj(response.raw, out_file)
        print("Background removed successfully.")
    else:
        print(f"Failed to remove background. Status code: {response.status_code}")
        print(response.text)

# Set your remove.bg API key
api_key = "<<YOUR SAMPLE API KEY>>"

# Input image path
input_image_path = "INPUT_PATH"

# Output image path for the resulting image with the background removed
output_image_path = "OUTPUT_PATH"

# Call the function to remove the background using remove.bg API
remove_background_with_api(api_key, input_image_path, output_image_path)
