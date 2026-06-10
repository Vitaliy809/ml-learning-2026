import numpy as np
from sklearn.datasets import fetch_openml

# x = [0, 1, -1]

# w1 = [-0.2, 0.3, 0.5]
# w2 = [-0.1, -0.8, 0.2]

# y1 = sum([x[i] * w1[i] for i in range(3)])
# y2 = sum([x[i] * w2[i] for i in range(3)])

# y = [y1, y2]

# # print(y)

# x = np.array([0, 0, 0])
# target = np.array([1, 1])

# w = np.array([
#     [-0.2, 0.3],
#     [-0.1, -0.8],
#     [0.3, 0.1],
  
# ])

# n_inp = len(x)
# n_out = len(target)
# w = np.random.randn(n_inp,n_out)

# bias = np.array([1.0, 0.1])
# bias = np.random.randn(n_out)

# y = x @ w + bias
#MAE Loss
# error = sum(abs(y - target))/n_out

# print(f"result{y}, target={target}, error={error}")

# ................................................

def get_batches(x, y, batch_size):
    for i in range(0, len(x), batch_size):
        yield x[i:i+batch_size], y[i:i+batch_size]
class LeakyReLU:
    def __init__(self, alpa = 0.01):
        self.alpa = alpa

    def forward(self, x):
        self.x = x
        return np.where(x > 0, x, self.alpa * x)

    def backward(self, grad):
        return grad * np.where(self.x > 0, 1, self.alpa)
    

class Linear:
    def __init__(self, n_inp, n_out):
        self.n_inp = n_inp
        self.n_out = n_out

        # self.w = np.random.randn(n_inp,n_out) * 0.1
        # self.bias = np.random.randn(1,n_out) * 0.1

        #Xavier init
        n = 6**0.5 / (n_inp + n_out)**0.5
        self.w = np.random.uniform(-n, n, (n_inp, n_out))
        n = 6**0.5 / (1 + n_out)**0.5
        self.bias = np.random.uniform(-n, n, (1, n_out))
        
        self.zero_grad()

    def __call__(self, x):
        return self.forward(x)
    
    def zero_grad(self):
        self.grad_w = np.zeros_like(self.w)
        self.grad_bias = np.zeros_like(self.bias)

    def forward(self, x):
        self.x = x
        return x @ self.w + self.bias
    
    def backward(self, grad_x):
        #y = x * w + b
        #dy/db = 1
        #dy/dw = x 
        #dy/dx = w
        
        self.grad_bias +=np.sum(grad_x, axis = 0, keepdims = True)
        self.grad_w += self.x.T @ grad_x
        grad_x = grad_x @ self.w.T
        
        return grad_x
    
    def step(self, lr):
        self.w -= self.grad_w * lr
        self.bias -= self.grad_bias * lr
    
    
def MAELoss(y, target):
    loss = np.sum(abs(y - target))/len(x)

    grad_y= None
    grad_target = None
    # if y > target:
    #   grad_y = np.full((y.shape), 1)
    #   grad_target = np.full((target.shape), -1)
    # elif y < target:
    #   grad_y = np.full((y.shape), -1)
    #   grad_target = np.full((target.shape), 1)

    grad_y = np.where(y > target, 1, np.where(y < target, -1, 0))
    grad_target = -grad_y

  
    return loss, grad_y
class Sequensial:
    def __init__(self, *args):
        self.layers = args

    def __call__(self, x):
        return self.forward(x)

    def forward(self, x):
       for layer in self.layers:
           x = layer.forward(x)
       return x

    def backward(self, grad):
        for layer in reversed(self.layers):
            grad = layer.backward(grad)
        return grad

    def step(self, lr = 0.01):
        for layer in self.layers:
            if hasattr(layer, 'step'):
             layer.step(lr)

    def zero_grad(self):
        for layer in self.layers:
            if hasattr(layer, 'zero_grad'):
             layer.zero_grad()
  

def MSELoss(y, target):
    loss = np.sum(abs(y - target)**2)/len(y)
    grad_y = 2 * (y - target) / y.size
    grad_target = -grad_y

    return loss, grad_y
   

mnist = fetch_openml('mnist_784', version=1)

x = np.array(mnist.data) / 255.0
labels = np.array(mnist.target).astype(int)
y = np.eye(10)[labels]

lr = 0.01
steps = 20

# x = np.array([[0, 0, 0]])
# target = np.array([[1, 1]])


model = Sequensial(
    Sequensial(
        Linear(784, 100),
        LeakyReLU(0.1)
    ),
    Linear(100, 10),
    LeakyReLU(0.1)

)

# model = Sequensial(
#     Sequensial(
#          Linear(3, 5),
#          LeakyReLU(),
#     ),
#    Sequensial(
#         Linear(5, 2),
#         LeakyReLU(),
#    )
# )
accuracy = np.mean(np.argmax(model(x), axis = 1) == labels)
print(f"Точність до тренування: {round(accuracy * 100, 1)}%")




batch_size = 32
for i in range(steps):
    epoch_loss = []
    permutation = np.random.permutation(x.shape[0])

    x_shuffled = x[permutation]
    y_shuffled = y[permutation]

    for x_batch, y_batch in get_batches(x_shuffled,y_shuffled, batch_size):
        model.zero_grad()

        res = model(x_batch)
        loss, grad = MSELoss(res, y_batch)
        epoch_loss.append(loss)
       

        model.backward(grad)
        model.step(lr)

    epoch_loss = sum(epoch_loss)/len(epoch_loss)

    print(epoch_loss)

accuracy = np.mean(np.argmax(model(x), axis = 1) == labels)
print(f"Точність після тренування: {round(accuracy * 100, 1)}%")


# for i in range(steps):
    # model.zero_grad()

    # y = model.forward(x)

    #MAE Loss
    # loss, grad = MSELoss(y, target)

    # grad = model.backward(grad)
    # model.step(lr = 0.01)

    # grad = layer2.backward(grad)
    # grad = layer1.backward(grad)

    # layer1.step()
    # layer2.step()

    # print(loss)
# print(f"result{y}, target={target}, error={grad}")

