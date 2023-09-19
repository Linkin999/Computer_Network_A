# CS305-2022Autumn Lab2 Report #
<font size=4>
Name: Xudong Zhang 12011923@mail.sutech.edu.cn
## Practice 1: Find Narcissistic Number ##
<font size=5>
- **Source code**

```python
def narcissistic(value:int)->bool:
    length = len(str(value))
    value2 = str(value)
    every=[]
    sub1=0
    for number1 in range(0,length,1):
        every.append(value2[number1])
    for number2 in range(0,length,1):
        sub=int(every[number2])**3
        sub1=sub1+sub
    if sub1==value:
        return sub1
```

```python
import Narcissistic
```

```python
def find_narcissistic_number(start:int,end:int)->list:
    result=[]
    for number in range(start,end+1,1):
        if Narcissistic.narcissistic(number):
            result.append(number)
    return result
find_narcissistic_number(100,1000)
```



![捕获](D:\Study in SUSTech\First semester of junior year\Computer Network A\lab2\捕获.JPG)