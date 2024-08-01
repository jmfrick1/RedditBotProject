import requests

def upload_image_to_imgur(image_path):
    client_id = 'YOUR_IMGUR_CLIENT_ID'
    headers = {'Authorization': f'Client-ID {client_id}'}
    api_url = 'https://api.imgur.com/3/upload'
    with open(image_path, 'rb') as image_file:
        response = requests.post(api_url, headers=headers, files={'image': image_file})
    if response.status_code == 200:
        return response.json()['data']['link']
    else:
        return None

if __name__ == '__main__':
    image_path = 'path/to/your/image.jpg'
    image_url = upload_image_to_imgur(image_path)
    if image_url:
        print(f"Image uploaded to: {image_url}")
    else:
        print("Failed to upload image.")
