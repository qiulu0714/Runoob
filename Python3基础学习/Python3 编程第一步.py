# 在前面的教程中我们已经学习了一些 Python3 的基本语法知识，下面我们尝试来写一个斐波纳契数列。
# Fibonacci series: 斐波纳契数列
# 两个元素的总和确定了下一个数
a, b = 0, 1
while b < 10:
    print(b)
    a, b = b, a + b
# 其中代码a, b = b, a + b的计算方式为先计算右边表达式，然后同时赋值给左边，等价于：
n = b
print(n)
m = a + b
print(m)
a = n
print(a)
b = m
print(b)
# 这个例子介绍了几个新特征。
# 第一行包含了一个复合赋值：变量 a 和 b 同时得到新值 0 和 1。最后一行再次使用了同样的方法，可以看到，
# 右边的表达式会在赋值变动之前执行。右边表达式的执行顺序是从左往右的。
# 输出变量值:
i = 256*256
print('i 的值为：', i)
#  -------------------end关键字--------------------------
# 关键字end可以用于将结果输出到同一行，或者在输出的末尾添加不同的字符，实例如下：
# Fibonacci series: 斐波纳契数列
# 两个元素的总和确定了下一个数
a, b = 0, 1
while b < 1000:
    print(b, end=',')
    a, b = b, a + b
