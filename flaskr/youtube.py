import sys
import config
import json
from googleapiclient.discovery import build

api_key = config.api_key
cse_id = config.cse_id
 # Create and get the custom search service from Google 
service = build("youtube", "v3", developerKey=api_key)

def search(query_term, max_page_cnt):
    result_list = []
    results = service.search().list(part='snippet', q=query_term,  maxResults=50).execute()
    # print(results['pageInfo'])
    result_list.extend(results['items'])      
        
    page_limit = 0
    while results['nextPageToken'] and page_limit < max_page_cnt:
        nextPageToken=results['nextPageToken']
        results = service.search().list(part='snippet', q=query_term, maxResults=50, pageToken=nextPageToken).execute()
        result_list.extend(results['items'])
        page_limit += 1

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
