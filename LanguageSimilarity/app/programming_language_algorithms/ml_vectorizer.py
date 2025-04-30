from transformers import AutoTokenizer, AutoModel
import torch
import torch.nn.functional as functional

tokenizer = AutoTokenizer.from_pretrained("microsoft/codebert-base")
model = AutoModel.from_pretrained("microsoft/codebert-base")

def embed(code):
    inputs = tokenizer(code, return_tensors="pt", truncation=True)
    with torch.no_grad():
        outputs = model(**inputs)
    return outputs.last_hidden_state.mean(dim=1)

def get_similarity(code1:str, code2:str)->float:
    vec1 = embed(code1)
    vec2 = embed(code2)
    sim = functional.cosine_similarity(vec1, vec2).item()
    return round(sim, 2)

