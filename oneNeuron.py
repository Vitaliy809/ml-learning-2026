import numpy as np

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

class Linear:
    def __init__(self, n_inp, n_out):
        self.n_inp = n_inp
        self.n_out = n_out

        self.w = np.random.randn(n_inp,n_out)
        self.bias = np.random.randn(1,n_out)
        
        self.reset_grad()
    
    def reset_grad(self):
        self.grad_w = np.zeros_like(self.w)
        self.grad_b = np.zeros_like(self.bias)

    def forward(self, x):
        self.x = x
        return x @ self.w + self.bias
    
    def backward(self, grad_x):
        #y = x * w + b
        #dy/db = 1
        #dy/dw = x 
        #dy/dx = w
        
        self.grad_bias = grad_x * 1
        self.grad_w = self.x.T @ grad_x
        grad_x = grad_x @ self.w.T
        
        return grad_x
    
    def step(self, lr = 0.01):
        self.w -= self.grad_w * lr
        self.bias -= self.grad_bias * lr
    
    
def MAELoss(y, target):
    loss = sum(abs(y - target))/len(x)

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

def MSELoss(y, target):
    loss = np.sum(abs(y - target)**2)/len(y)
    grad_y = 2 * (y - target) / y.size
    grad_target = -grad_y

    return loss, grad_y
   

x = np.array([[0, 0, 0]])
target = np.array([[1, 1]])

layer1 = Linear(3, 5)
layer2 = Linear(5, 2)

for i in range(100):
    y = layer1.forward(x)
    y = layer2.forward(y)
    #MAE Loss
    loss, grad = MSELoss(y, target)

    grad = layer2.backward(grad)
    grad = layer1.backward(grad)

    layer1.step()
    layer2.step()

    print(loss)
# print(f"result{y}, target={target}, error={grad}")

