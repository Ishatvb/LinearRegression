import numpy as np

# we have values of x and y and we want to find correct values of m and b

def gradient_descent(x,y):
    m_current = b_current = 0
    iterations = 1000
    n = len(x)
    learning_rate = 0.001
    
    for i in range(iterations):
        y_predicted = m_current * x + b_current
        m_derivative = -(2 / n) * sum(x * (y - y_predicted))
        b_derivative = -(2 / n) * sum(y - y_predicted)
        m_current = m_current - learning_rate * m_derivative
        b_current = b_current - learning_rate * b_derivative
        print(f"m {m_current}, b {b_current}, iteration {iteration}")

x = np.array([1,2,3,4,5])
y = np.array([5,7,9,11,13])

gradient_descent(x,y)
