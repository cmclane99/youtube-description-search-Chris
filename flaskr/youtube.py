import sys
import config
import json
from googleapiclient.discovery import build

api_key = config.api_key
cse_id = config.cse_id
 # Create and get the custom search service from Google 
service = build("youtube", "v3", developerKey=api_key)

def search(query_term, max_page_cnt, music): # boolean variable to determine a music search
    def get_video_info(video_id):
        result = service.videos().list(part='snippet', id=video_id).execute()
        try:
            return result['items'][0]
        except:
            return None
    
    def get_video_list(search_results):
        video_list = []
        for item in search_results['items']:
            video_id = item['id']['videoId']
            video_info = get_video_info(video_id)
            if video_info:
                video_list.append(video_info)
        
        return video_list

    result_list = []

    if music == True:
        results = service.search().list(part='snippet', type="video", topicId="/m/04rlf", q=query_term, maxResults=50).execute()
    else:
        results = service.search().list(part='snippet', type="video", q=query_term,  maxResults=50).execute()
    # print(results['pageInfo'])
    video_list = get_video_list(results)
    result_list.extend(video_list)      
        
    page_limit = 0
    while results['nextPageToken'] and page_limit < max_page_cnt:
        nextPageToken=results['nextPageToken']
        if music == True:
            results = service.search().list(part='snippet', type="video", topicId="/m/04rlf", q=query_term, maxResults=50, pageToken=nextPageToken).execute()
        else:
            results = service.search().list(part='snippet', type="video", q=query_term, maxResults=50, pageToken=nextPageToken).execute()
        video_list = get_video_list(results)
        result_list.extend(video_list)
        page_limit += 1

    if music == True:
        with open('youtube_music_search_' + query_term + '.json', 'w', encoding='utf-8') as f:
            json.dump(result_list, f, ensure_ascii=False, indent=4)
    else:
        with open('youtube_search_' + query_term +'.json', 'w', encoding='utf-8') as f:
            json.dump(result_list, f, ensure_ascii=False, indent=4)

    return result_list

# Check if the script is being called from the terminal
if __name__=='__main__':
    # Get the first command line argument which is the script name
    arg1 = sys.argv[0]

    # Check the number of arguments in the command
    if len(sys.argv) == 2:
        # Get the first argument (provided by the user)
        query_term = sys.argv[1]
        print("query: " + query_term)

        results = search(query_term, 1)
        with open('youtube_search_' + query_term +'.json', 'w', encoding='utf-8') as f:
            json.dump(result_list, f, ensure_ascii=False, indent=4)

    else:
        # Print usage of the script
        print("usage: " + arg1 + " [search_term]")
