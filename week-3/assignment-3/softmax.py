'''
Câu 1: Trong pytorch, torch.nn.Module là lớp cơ bản để từ đó xây dựng lên các mô hình hoặc các phương
thức kích hoạt (activation funtion) như sigmoid, softmax,... Trong phần này, chúng ta xây dựng
class Softmax và softmax_stable nhận đầu vào là mảng 1 chiều (tensor 1 chiều) dựa vào kế thừa
từ lớp Module và ghi đè vào phương thức forward() theo công thức sau đây

'''
import torch 

class MySoftmax(torch.nn.Module):
    def __init__(self):
        super(MySoftmax, self).__init__()

    def forward(self, x):
        return torch.exp(x) / (torch.sum(torch.exp(x)))


class SoftmaxStable(torch.nn.Module):
    def __init__(self):
        super(SoftmaxStable, self).__init__()
    
    def forward(self, x):
        c = torch.max(x)
        return torch.exp(x-c) / (torch.sum(torch.exp(x-c)))
