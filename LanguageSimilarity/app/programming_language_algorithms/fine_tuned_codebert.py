import torch
import torch.nn as nn
from transformers import AutoTokenizer, AutoModel

class CodeBERTSimilarity(nn.Module):
    def __init__(self, model_name="microsoft/codebert-base"):
        super().__init__()
        self.bert = AutoModel.from_pretrained(model_name)
        self.fc = nn.Sequential(
            nn.Linear(768, 256),
            nn.ReLU(),
            nn.Linear(256, 1),
            nn.Sigmoid()
        )

    def encode(self, x):
        outputs = self.bert(**x)
        return outputs.last_hidden_state[:, 0, :]

    def forward(self, x1, x2):
        v1 = self.encode(x1)
        v2 = self.encode(x2)
        diff = torch.abs(v1 - v2)
        return self.fc(diff)

tokenizer = AutoTokenizer.from_pretrained("Models/finetuned_codebert/bert")

model = CodeBERTSimilarity()
model.bert = AutoModel.from_pretrained("Models/finetuned_codebert/bert")
model.fc.load_state_dict(torch.load("Models/finetuned_codebert/fc_head.pth"))
model.eval()


def get_similarity(code1: str, code2: str) -> float:
    with torch.no_grad():
        x1 = tokenizer(code1, return_tensors="pt", truncation=True, padding=True)
        x2 = tokenizer(code2, return_tensors="pt", truncation=True, padding=True)
        sim = model(x1, x2).item()
        return round(sim, 2)