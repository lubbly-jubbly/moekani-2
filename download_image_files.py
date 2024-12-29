import os
import requests
from moekani_2 import get_wanikani_data

image_files_directory = "/Users/libbyrear/Documents/bucket/image_files"


def get_image_file_path(id):
    return os.path.join(image_files_directory, f"image_{id}.mp3")


def download_images(image_url_lookup):
    os.makedirs(image_files_directory, exist_ok=True)
    image_paths = []
    for id, url in image_url_lookup.items():
        wanikani_api_token = os.getenv("WANIKANI_API_TOKEN")

        headers = {"Authorization": "Bearer " + wanikani_api_token}

        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            temp_file = os.path.join(image_files_directory, f"image_{id}.svg")
            with open(temp_file, "wb") as f:
                f.write(response.content)
        else:
            print(f"Failed to download {url}. HTTP Status: {response.status_code}")
    return image_paths


def download_wanikani_image_files(wanikani_data):
    urls = {}
    for item in wanikani_data:
        if len(item["data"]["characters"]) > 0:
            return

        if item["data"].get("character_images", []):
            svg = next(
                (
                    image
                    for image in item["data"]["character_images"]
                    if image["content_type"] == "image/svg+xml"
                    and not image["metadata"]["inline_styles"]
                ),
                None,
            )["url"]

            if svg:
                urls[item["id"]] = svg["url"]

    image_paths = download_images(urls)
    return image_paths


download_wanikani_image_files(get_wanikani_data())
