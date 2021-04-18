# Youtube Description Search Engine
## Chris McLane
This is a class project for COSC 381 at EMU. It is a web-based search engine that searches for user-specified keywords from the description section of youtube videos.

# youtube-search-description-cmclane99
To run the repo:
1. add your Google API key and CSE key to flaskr/config.py
2. create a virual environment and install the packages:
    - python3 -m venv env
    - source env/bin/activate
    - pip install -r requirements.txt
3. run the app: flask run --host 0.0.0.0

## Set up selenium

### Download chromedriver
Download the chrome driver with the proper verion and put it (the executable file, not the zip file or folder) to tests/.