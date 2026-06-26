import torch
import torch.nn as nn
import torch.optim as optim
import torchvision
import torchvision.transforms as transforms
from torch.utils.data import DataLoader
from tqdm import tqdm
import os

class Network(nn.Module):
    def __init__(self):
        super().__init__()

        self.conv = nn.Sequential(
            # 3 32 32
            nn.Conv2d(3, 64, 3, 1, 1),
            nn.LeakyReLU(0.1),
            nn.AvgPool2d(2),
            # 64 16 16 
            nn.Conv2d(64, 128, 3, 1, 1),
            nn.LeakyReLU(0.1),
            nn.AvgPool2d(2),
            # 128 8 8
            nn.Conv2d(128, 256, 3, 1, 1),
            nn.LeakyReLU(0.1),
            nn.AvgPool2d(2),      
            # 256 4 4 
             nn.Conv2d(256, 512, 3, 1, 1),
            nn.LeakyReLU(0.1),
            nn.AvgPool2d(2),   
            #512 2 2   
            nn.Flatten()
        )


        self.linear = nn.Sequential(
            nn.Linear(512*2*2, 32),
            nn.LeakyReLU(0.1),
            nn.Linear(32, 10),
            nn.Sigmoid()
        )
    def forward(self, x):
        v = self.conv(x)   
        return self.linear(v)
    
    


models_folder = "models"
os.makedirs(models_folder, exist_ok=True)

BATCH_SIZE = 256
EPOCHS = 10
LR = 1e-3

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
])

trainset = torchvision.datasets.CIFAR10(root = './data', train=True, download=True, transform=transform)
testset = torchvision.datasets.CIFAR10(root = './data', train=False, download=True, transform=transform)


testloader = DataLoader(testset, batch_size=BATCH_SIZE, shuffle=False)

model = Network().to(device)
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr = LR)

start_epcoh = 4 
checkpoint = torch.load(f"models/model_epoch_{start_epcoh}.pt", map_location=device)
model.load_state_dict(checkpoint)


def test_model(model, testloader):
    correct = total = 0
    model.eval()
    with torch.no_grad():
            for inputs, labels in testloader:
                  inputs, labels = inputs.to(device), labels.to(device)
                  output = model(inputs)
                  _, predicted = output.max(1)

                  total += labels.size(0)
                  correct += (predicted == labels).sum().item()
    return correct / total


accuracy = test_model(model,testloader)
print(f"Accuracy: {accuracy * 100}%")

loss_history = []
for epoch in range(EPOCHS):
    model.train()
    trainloader = DataLoader(trainset, batch_size=BATCH_SIZE, shuffle=True)
    for inputs, labels in tqdm(trainloader):
        inputs, labels = inputs.to(device), labels.to(device)
        optimizer.zero_grad()

        output = model(inputs)

        loss = criterion(output, labels)
        loss.backward()
        optimizer.step()

        loss_history.append(loss.item())



    avg_loss = sum(loss_history) / len(loss_history)
    print(f"Epoch {start_epcoh + epoch + 1} done! Loss: {avg_loss}, Accuracy: {accuracy*100}%")

    torch.save(model.state_dict(), f"{models_folder}/model_epoch_{start_epcoh + epoch + 1}.pt")


        # # print(inputs)
        # print(labels)
        # input()
