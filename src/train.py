# train.py

import torch
from model import MyModel
from data_loader import get_dataloader

def train():
    # Setup
    model = MyModel(...)
    dataloader = get_dataloader(...)
    optimizer = torch.optim.Adam(model.parameters())
    loss_fn = torch.nn.CrossEntropyLoss()

    # Training loop
    for epoch in range(num_epochs):
        for x, y in dataloader:
            preds = model(x)
            loss = loss_fn(preds, y)

            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

        print(f"Epoch {epoch}: Loss = {loss.item()}")

if __name__ == "__main__":
    train()