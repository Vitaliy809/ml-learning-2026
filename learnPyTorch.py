import torch
import torch.nn as nn
import torch.optim as optim
import torchvision
import torchvision.transforms as transforms
from torch.utils.data import DataLoader


BATCH_SIZE = 256
EPOCHS = 10

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
])

trainset = torchvision.datasets.CIFAR10(root = './data', train=True, download=True, transform=transform)
testset = torchvision.datasets.CIFAR10(root = './data', train=False, download=True, transform=transform)

trainloader = DataLoader(trainset, batch_size=BATCH_SIZE, shuffle=True)
testloader = DataLoader(testset, batch_size=BATCH_SIZE, shuffle=False)

for epoch in range(EPOCHS):
    for inputs, labels in (trainloader):
        inputs, labels = inputs.to(device), labels.to(device)
        print(inputs)
        print(labels)
        exit()
