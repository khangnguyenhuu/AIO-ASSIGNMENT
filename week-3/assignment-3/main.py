import torch
import torch.nn as nn

from queue import MyQueue
from softmax import MySoftmax, SoftmaxStable
from stack import MyStack
from ward import Student, Doctor, Teacher, Ward

if __name__ == "__main__":
    '''
    Cau 1 trac nghiem
    '''
    data = torch.Tensor([1, 2, 3])
    softmax_function = nn.Softmax(dim=0)
    output = softmax_function(data)
    compare_value = 0.09
    assert round(output[0].item(), 2) == compare_value
    print("output cau 1", output)
    print('='*20)
    '''
    Cau 2 trac nghiem
    '''
    data = torch.Tensor([5, 2, 4])
    my_softmax = MySoftmax()
    output = my_softmax(data)
    compare_value = 0.26
    assert round(output[-1].item(), 2) == compare_value
    print("output cau 2", output)
    print('='*20)
    '''
    Cau 3 trac nghiem
    '''
    data = torch.Tensor([1, 2, 300000000])
    my_softmax = MySoftmax()
    output = my_softmax(data)
    compare_value = 0.0
    assert round(output[0].item(), 2) == compare_value
    print("output cau 3", output)
    print('='*20)
    '''
    Cau 4 trac nghiem
    '''
    data = torch.Tensor([1, 2, 3])
    softmax_stable = SoftmaxStable()
    output = softmax_stable(data)
    compare_value = 0.67
    assert round(output[-1].item(), 2) == compare_value
    print("output cau 4", output)
    print('='*20)

    '''
    Cau 5 trac nghiem
    '''
    student1 = Student(name="studentZ2023", yob=2011, grade="6")
    assert student1._yob == 2011
    print("output cau 5")
    student1.describe()
    print('='*20)

    '''
    Cau 6 trac nghiem
    '''
    teacher1 = Teacher(name="teacherZ2023", yob=1991, subject="History")
    assert teacher1._yob == 1991
    print("output cau 6")
    teacher1.describe()
    print('='*20)

    '''
    Cau 7 trac nghiem
    '''
    doctor1 = Doctor(name="doctorZ2023", yob=1981,
                     specialist="Endocrinologists")
    assert doctor1._yob == 1981
    print("output cau 7")
    doctor1.describe()
    print('='*20)

    '''
    Cau 8
    '''
    student1 = Student(name="studentA", yob=2010, grade="7")
    teacher1 = Teacher(name="teacherA", yob=1969, subject="Math")
    teacher2 = Teacher(name="teacherB", yob=1995, subject="History")
    doctor1 = Doctor(name="doctorA", yob=1945,
                     specialist="Endocrinologists")
    doctor2 = Doctor(name=" doctorB ", yob=1975, specialist="Cardiologists")
    ward1 = Ward(name="Ward1")
    ward1.add_person(student1)
    ward1.add_person(teacher1)
    ward1.add_person(teacher2)
    ward1.add_person(doctor1)
    assert ward1.count_doctor() == 1
    ward1.add_person(doctor2)
    print("output cau 8")
    print(ward1.count_doctor())
    print('='*20)

    '''
    Cau 9
    '''
    stack1 = MyStack(capacity=5)
    stack1.push(1)
    assert stack1.is_full() == False
    stack1.push(2)
    print("output cau 9")
    print(stack1.is_full())
    print("="*20)

    '''
    Cau 10
    '''
    stack1 = MyStack(capacity=5)
    stack1.push(1)
    assert stack1.is_full() == False
    stack1.push(2)
    print("output cau 10")
    print(stack1.top())
    print('='*20)

    '''
    Cau 11
    '''
    queue1 = MyQueue(capacity=5)
    queue1.enqueue(1)
    assert queue1.is_full() == False
    queue1.enqueue(2)
    print('output cau 11')
    print(queue1.enqueue(2))
    print('='*20)

    '''
    Cau 12
    '''
    queue1 = MyQueue(capacity=5)
    queue1.enqueue(1)
    assert queue1.is_full() == False
    queue1.enqueue(2)
    print('output cau 12')
    print(queue1.front())
    print('='*20)
