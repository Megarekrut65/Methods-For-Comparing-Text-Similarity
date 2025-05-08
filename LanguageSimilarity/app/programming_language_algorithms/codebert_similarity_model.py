from transformers import RobertaTokenizer, RobertaModel
import torch
import torch.nn.functional as functional

tokenizer = RobertaTokenizer.from_pretrained("microsoft/codebert-base")
model = RobertaModel.from_pretrained("microsoft/codebert-base")

def embed(code):
    inputs = tokenizer(code, return_tensors="pt", truncation=True, max_length=512)
    with torch.no_grad():
        outputs = model(**inputs)
    return outputs.last_hidden_state[:, 0, :]

def get_similarity(code1:str, code2:str)->float:
    vec1 = embed(code1)
    vec2 = embed(code2)
    
    sim = functional.cosine_similarity(vec1, vec2).item()
    return round(sim, 2)

