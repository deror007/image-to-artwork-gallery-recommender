import numpy as np
import faiss
from helpers import get_image_embedding, load_image, load_url_image
import pandas as pd

# Create index file pipeline
def createIndex(art_urls, model, preprocess, device, filename):

    # Calculate image embeddings with efficientNet model
    embeddings = np.vstack([get_image_embedding(model, load_url_image(path, preprocess, device)) for path in art_urls])
    
    # Set up index object
    index = faiss.IndexFlatL2(embeddings.shape[1]) #Dimension of vector is 1000 or column width for 1000 classes in imagenet1k.

    # Add embeddings into the index
    index.add(embeddings)

    # Save index embeddings:
    faiss.write_index(index, filename)
    print(f"Saved index to {filename}; embedding size is {embeddings.shape}")




    # Call the following function like this:  --->>
    ## Append new artwork to index:
    ## art_name = "Sculpture 9"
    # art_url = "https://signetcontemporaryart.com/wp-content/uploads/2023/06/G07-2-scaled.jpg"
    # df = appendIndex(art_name,art_url, df, model, preprocess, device, index_name)


# NOTE: By design FAISS vector stores cannot incrementally update vectors. 
    # But there are some indexes that may allow this like HNSW (Hierarchical Navigable Small World), trade off is that it can be slow.
    # : Look to chatgpt and FAISS DOCS 
    
# Update index with a new image. THIS DOESN'T WORK IN FAISS!!!!!!
def appendIndex(new_name, new_art_url, df, model, preprocess, device, index_name):
    # Update dataframe 
    # print(df.columns)
    print(new_name)
    print(new_art_url)

    # New data to append
    new_data = {'ARTWORK': new_name, 'URL': new_art_url}

    # Append the new row
    df = df._append(new_data, ignore_index=True)


    # print(df.to_string())

    # Get index
    index = faiss.read_index(index_name)

    # Get new image embedding
    embedding = np.vstack([get_image_embedding(model, load_url_image(new_art_url, preprocess, device))])

    # add new image embedding
    index.add(embedding)

    # Save index embeddings:
    faiss.write_index(index, index_name)
    print("updated index")

    # return updated dataframe for visualisation:
    return df



