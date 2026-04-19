# data_loader.py

from torch.utils.data import Dataset, DataLoader

class CustomDataset(Dataset):
    def __init__(self, data_path, transform=None):
        self.data = ...
        self.transform = transform

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        x, y = ...
        if self.transform:
            x = self.transform(x)
        return x, y


def get_dataloader(data_path, batch_size, shuffle=True):
    dataset = CustomDataset(data_path)
    return DataLoader(dataset, batch_size=batch_size, shuffle=shuffle)