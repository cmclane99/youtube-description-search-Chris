from whoosh.index import create_in, open_dir
from whoosh.fields import Schema, TEXT, ID 
from whoosh.analysis import StemmingAnalyzer
from whoosh.lang.porter import stem
from whoosh.qparser import QueryParser
from whoosh import scoring

import os

def create_whoosh_index(video_list, index_name):
    # Schema definition: video_id, video_title, video_description
    schema = Schema(id=ID(stored=True),
                    title=TEXT(stored=True),
                    description=TEXT(analyzer=StemmingAnalyzer(), stored=True))
                    # StemmingAnalyzer - reduces words to their most basic form
    
    # create a folder to store the index
    if not os.path.exists(index_name):
        os.mkdir(index_name)

    index = create_in(index_name, schema)
    writer = index.writer() # like the Java FileWriter

    for video_item in video_list:
        video_id = video_item['id']
        video_title = video_item['snippet']['title']
        video_description = video_item['snippet']['description']
        writer.add_document(id=video_id, title=video_title, description=video_description)
    
    writer.commit()

