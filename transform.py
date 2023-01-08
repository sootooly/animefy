# transform.py
import base64
import requests

import config

def transform_image(image_data):
  """
  Transforms the given image data using the deepai anime style transfer model.
  Returns the transformed image data.
  """
  # Set up the request headers and payload
  headers = {'api-key': config.api_key}
  data = {'style': 'anime'}

  # Encode the image data as base64 and set it in the payload
  image_data = base64.b64encode(image_data).decode('utf-8')
  data['image'] = image_data

  # Make the request to the API using a secure connection and verifying the SSL certificate
  response = requests.post('https://api.deepai.org/api/fast-style-transfer', headers=headers, json=data, verify=True)

  # Get the transformed image from the response
  transformed_image_data = response.json()['data']['output_url']
  transformed_image = requests.get(transformed_image_data)

  return transformed_image.content
