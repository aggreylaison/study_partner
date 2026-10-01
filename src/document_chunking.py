from markitdown import MarkItDown
from langchain_text_splitters import RecursiveCharacterTextSplitter
from embedding import get_embedding
from database import get_conection,insert_chunks
from document import insert_doc_name
from user import get_user_id
import os

file_path="/home/aggrey/Projects/ai_agent/ML_DL_Agentic_AI_Notes.pdf"
filename=os.path.basename(file_path)

md=MarkItDown()

result=md.convert("/home/aggrey/Projects/ai_agent/ML_DL_Agentic_AI_Notes.pdf")

marked_down=result.text_content

text_splitter=RecursiveCharacterTextSplitter(chunk_size=500,chunk_overlap=20)

chunks=text_splitter.split_text(marked_down)


embeded_chunks=[]
conn=get_conection()
user_id=get_user_id(conn,"john")

document_id=insert_doc_name(conn,filename,user_id)


for index,chunk in enumerate(chunks):
    embed=get_embedding(chunk)
    embeded_chunks.append(embed)

    
    insert_chunks(conn,document_id,chunk,index,embed)

conn.close()
