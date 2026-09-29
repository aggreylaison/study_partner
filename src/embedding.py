import os 
from dotenv import load_dotenv
from huggingface_hub import InferenceClient
import numpy as np

load_dotenv()

hf_token=os.getenv("HUGING_FACE")

client=InferenceClient(token=hf_token)

def get_embedding(text):
    model="sentence-transformers/all-MiniLM-L6-v2"

    embeding=client.feature_extraction(text)
    embeding = np.array(embeding)

    return embeding.mean(axis=0)

hi=get_embedding("you are a programer and your jib is to wrihbcdackjs cnklsdhcd cijdcadcewfbheck jdcjb dlsakhfekrjwaci cweihfnwufrugfveidcbcak;whffruiea;ue o;qfhkqaeqjfte code" )

print(hi.shape)