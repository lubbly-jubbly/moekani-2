import requests
import os
import mimetypes
from pydub import AudioSegment

audio_files_directory = "/Users/libbyrear/Documents/bucket/audio_files"

def get_audio_file_path(id): 
    return os.path.join(audio_files_directory, f"audio_{id}.mp3")

def download_and_convert_audio(audio_url_lookup):
    os.makedirs(audio_files_directory, exist_ok=True)
    audio_paths = []
    for id, url in audio_url_lookup.items():
        response = requests.get(url)
        if response.status_code == 200:  # Check for successful response
            # Save the original file
            temp_file = os.path.join(audio_files_directory, f"audio_{id}.weba")
            with open(temp_file, 'wb') as f:
                f.write(response.content)
            
            # Convert to MP3
            try:
                audio = AudioSegment.from_file(temp_file)  # Detects format automatically
                mp3_file = get_audio_file_path(id)
                audio.export(mp3_file, format="mp3")
                audio_paths.append(mp3_file)
                
                # Clean up temporary file
                os.remove(temp_file)
            except Exception as e:
                print(f"Failed to convert {temp_file} to MP3. Error: {e}")
        else:
            print(f"Failed to download {url}. HTTP Status: {response.status_code}")
    return audio_paths

def download_wanikani_audio_files(wanikani_data):
    urls = {}
    for item in wanikani_data:
        if item['data'].get('pronunciation_audios', []):
            urls[item['id']] = item['data']['pronunciation_audios'][0]['url']
            
    audio_paths = download_and_convert_audio(urls)
    return audio_paths


