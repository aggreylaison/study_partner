from markitdown import MarkItDown
from langchain_text_splitters import RecursiveCharacterTextSplitter
from embedding import get_embedding
from database import get_conection,insert_chunks
from document import insert_doc_name


md=MarkItDown()

result=md.convert("/home/aggrey/Projects/ai_agent/ML_DL_Agentic_AI_Notes.pdf")

marked_down=result.text_content

text_splitter=RecursiveCharacterTextSplitter(chunk_size=500,chunk_overlap=20)

chunks=text_splitter.split_text(marked_down)

embeded_chunks=[]
conn=get_conection()


for chunk in chunks:
    embed=get_embedding(chunk)
    embeded_chunks.append(embed)

    
    insert_chunks(conn,chunk,embed)
conn.close
