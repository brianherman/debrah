import os
# Alexa Voice Service
DEVICE_TYPE_ID = ''
CLIENT_ID = ''
CLIENT_SECRET = ''
REFRESH_TOKEN = ''
os.environ['DEVICE_TYPE_ID'] = 'debra'
os.environ['CLIENT_ID']      = ''
os.environ['CLIENT_SECRET']  = ''
os.environ['REFRESH_TOKEN']  = ''

if os.environ.get('DEVICE_TYPE_ID', False):
    DEVICE_TYPE_ID = os.environ.get('DEVICE_TYPE_ID', False)
if os.environ.get('CLIENT_ID', False):
    CLIENT_ID = os.environ.get('CLIENT_ID', False)
if os.environ.get('CLIENT_SECRET', False):
    CLIENT_SECRET = os.environ.get('CLIENT_SECRET', False)
if os.environ.get('REFRESH_TOKEN', False):
    REFRESH_TOKEN = os.environ.get('REFRESH_TOKEN', False)

# Temporary directory for storing mp3 and text files
TEMP_DIR = 'C:\\tmp\\alexa-client'
