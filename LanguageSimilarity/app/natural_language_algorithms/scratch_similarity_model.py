import torch
import torch.nn as nn
import pytorch_lightning as pl
import joblib


class SimilarityModel(pl.LightningModule):
    def __init__(self, input_dim=5000):
        super().__init__()
        self.model = nn.Sequential(
            nn.Linear(input_dim * 2, 256),
            nn.ReLU(),
            nn.Linear(256, 1),
            nn.Sigmoid()
        )

    def forward(self, x1, x2):
        x = torch.cat((x1, x2), dim=1)
        return self.model(x)

vectorizer = joblib.load("Models/zero_vectorizer.joblib")

model = SimilarityModel.load_from_checkpoint("Models/zero_similarity_model.ckpt")
model.eval()

def get_similarity(text1: str, text2: str) -> float:
    vec1 = vectorizer.transform([text1]).toarray()[0]
    vec2 = vectorizer.transform([text2]).toarray()[0]
    x1 = torch.tensor(vec1, dtype=torch.float32).unsqueeze(0)
    x2 = torch.tensor(vec2, dtype=torch.float32).unsqueeze(0)

    with torch.no_grad():
        similarity = model(x1, x2).item()
    return similarity
