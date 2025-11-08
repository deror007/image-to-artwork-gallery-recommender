import sys
import pandas as pd
from PIL import Image
from PIL import ImageFile
import faiss
import requests

import torch
from io import BytesIO


from index import createIndex, appendIndex
from data import getArtDict, getArtPageDict
from model import get_EffNetM_details, create_effnetMArt_model

import gradio as gr
import webbrowser



pd.options.mode.chained_assignment = None  # default='warn'

def load_image(image, preprocess, device):
    print(type(image))
    image = image.convert('RGB')
    image = preprocess(image)
    image = image.unsqueeze(0).to(device)
    return image

def get_image_embedding(model, image_tensor):
    
    # Put model into evaluation mode and turn on inference mode
    print(type(image_tensor))
    with torch.no_grad():
        embedding = model(image_tensor)
        
    return embedding.cpu().numpy()

def get_Similar_Style(rankings_df, art_style):
    
    # Retrieve all images in the rankings dataframe with the artstyle name; order by rank.
    art_Style_Ranking_df = rankings_df[rankings_df['ARTWORK'].str.contains(art_style)]

    return art_Style_Ranking_df

def retrieve_images(rankings, images_retrieved):
    # Limit the number of shown images to 3 if images_retrieved is not specified

    shown_images = 3 if images_retrieved == None else images_retrieved  
    imgs_list=rankings["URL"].tolist()
    return imgs_list[:shown_images]


def find_similar_images(image, model, preprocess, device, df, index_file, return_by_style=None, images_retrieved=None):
    
    # load index embeddings
    loaded_index = faiss.read_index(index_file)

    print("Loaded index:",index_file)

    # input query image 
    query_vector = get_image_embedding(model,load_image(image,preprocess,device))

    # Take all indexed images for pandas table:
    k = loaded_index.ntotal 

    # Print dimensions for debugging
    print("Query Vector Dimension:", query_vector.shape)
    print("Faiss Index Dimension:", loaded_index.d)

    print(sys.getsizeof(loaded_index), "Bytes used for vector index")
    print(sys.getsizeof(df), "Bytes used by dataframe")

    # Perform the search
    D, I = loaded_index.search(query_vector, k=k)  
    # print(D, I)

    # Get descending order of similarity.
    top_indices = I[0]
    top_results = df.iloc[top_indices]
    
    top_results['distance'] = D[0]

    # If selected, get top artworks that match a style: 
    if return_by_style in ["Abstract", "Floral", "Pop", "Wildlife", "Seascape", "Cityscape", "Mongolian", "Landscape", "Sculpture"]:
        print(f"RANK SORTED BY: {return_by_style}")
        top_results=get_Similar_Style(top_results, return_by_style)
        
    
    # Display selected images on screen.
    print(top_results)
    return retrieve_images(top_results, images_retrieved)


def get_image_results(image, retrieved_images, art_style):
    # image: PIL image ,retrieved_images: positive integer, Art_Style: str
    if image == None:
        return None

    artworks = getArtDict()
    art_names = artworks.keys()
    art_urls = artworks.values()
    model, preprocess, device = get_EffNetM_details()
    index_name = "original.index"

    # Create dataframe for results visualisation.
    df = pd.DataFrame(art_names, columns=['ARTWORK'])
    df['URL']=art_urls
    print(df)

    return find_similar_images(image, model, preprocess, device, df, index_name, art_style, retrieved_images)

# Function for allowing users to follow interested artworks to its art page:
def get_selected_value(evt: gr.SelectData):
    print(evt.value['image']['url'])

    # retrieve selected image's display url:
    image_path = evt.value['image']['url']

    # Use the display url as a key for retrieving the shops url by using the global dict:
    selected_shop_url = shop_details[image_path]
    print(selected_shop_url)

    # follow the selected url:
    webbrowser.open(selected_shop_url, new=0, autoraise=True)
    #if (webbrowser.open(selected_shop_url, new=0, autoraise=True)):
    #     print("OPENED IMG URL.")
    #else:
    #     print("CANNOT OPEN IMG URL.")

    return evt.value

# GLOBAL VARIABLES
artwork_counts = 72
shop_details = getArtPageDict()

# User Interface
# iface = gr.Interface(
#     fn=get_image_results,
#     inputs=[gr.Image(type="pil"), 
#             gr.Number(minimum=1, maximum = artwork_counts, step=1), 
#             gr.Dropdown(["Abstract", "Floral", "Pop", "Wildlife", "Seascape", "Cityscape", "Mongolian", "Landscape", "Sculpture"])],
#     outputs="gallery",
#     live=True,
#     # css="footer {visibility: hidden}"
# )

# iface.launch()

 
with gr.Blocks(theme= gr.themes.Soft(primary_hue="gray"),title="Image to Art Gallery Recommender 🎨",
               css="footer {visibility: hidden}") as ui:
    gr.Markdown(
    """
    # Image to Art Gallery Recommender 🎨

    """)
    with gr.Row():
        with gr.Column():
            image = gr.Image(type="pil", sources=["upload", "webcam"])
            recommendations = gr.Number(minimum=0, maximum = artwork_counts, step=1,label="Retrieved Artworks",value=5)
            styles = gr.Dropdown(["All", "Abstract", "Floral", "Pop", "Wildlife", "Seascape", 
                                  "Cityscape", "Mongolian", "Landscape", "Sculpture"],label="Art Style",value="All")
            
            

        with gr.Column():
            gallery = gr.Gallery(
                label="Generated images",show_label=False, 
                elem_id="gallery", object_fit="contain", 
                height="auto", allow_preview=False)
            
            btn = gr.Button("Get Recommendations", scale=None)

            btn.click(get_image_results, [image, recommendations, styles], gallery)

            gallery.select(get_selected_value, None, None)



ui.launch()
