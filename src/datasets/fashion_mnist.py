"""Datasets."""
import os

import torch
from torch.utils.data import Dataset, ConcatDataset
from torchvision import datasets
from torchvision import transforms

BASEPATH = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'raw'))


class FashionMNIST:
    """Fashion MNIST dataset."""

    transforms = transforms.Compose([
        transforms.ToTensor(),
    ])

    def __init__(self, train=True):
        """FashionMNIST dataset."""

        if train is True:
            self.dataset = ConcatDataset(
                [datasets.FashionMNIST(BASEPATH, transform=self.transforms, train=True, download=True),
                 datasets.FashionMNIST(BASEPATH, transform=self.transforms, train=False, download=True)])

        else:
            self.dataset = datasets.FashionMNIST(
                BASEPATH, transform=self.transforms, train=False, download=True)

    def __len__(self):
        return self.dataset.__len__()

    def __getitem__(self, item):
        return self.dataset.__getitem__(item)

    def inverse_normalization(self, normalized):
        """Inverse the normalization applied to the original data.

        Args:
            x: Batch of data

        Returns:
            Tensor with normalization inversed.

        """
        normalized = 0.5 * (normalized + 1)
        return normalized