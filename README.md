# Fraction（Freshman Practice）

分数模块，python初学者小练习

* 学习把分数封装到类里，重载运算符
* 学习运用package文件系统

## 特点

* 重载分数类的简单运算

  ```
  class frac:
       |  __add__(self, other) #加法操作
       |  
       |  __sub__(self, other) #减法
       |  
       |  __mul__(self, other) #乘法
       |  
       |  __truediv__(self, other) #除法
       |      
       |  __pow__(self, other) #分数的整数次幂操作，快速幂实现
       | 
       |  __abs__(self) #绝对值运算
       |  
       |  __eq__(self,other) #相等判断 
       |  
       |  __radd__(self, other) #加法反转
       |  
       |  __rmul__(self, other) #乘法反转
       |  
       |  __rpow__(self, ohter) #幂运算反转
       |  
       |  __rsub__(self, other) #减法反转
       |  
       |  __rtruediv__(self, other) #除法反转
       |  
       |  
       |  
       |  
       
       
  ```

## 安装说明

* 将fraction文件夹放入path目录

* 导入：`import fraction as frac`

* 构造一个分数：例如，`a = frac.make_frac(1,2)`,即为：
  $$
  a=\frac{1}{2}
  $$

* 代码示例：

  ```
  import fraction as frac
  
  a=frac.make_frac(3,5)
  b=frac.make_frac(7,10)
  print("a=",end='')
  a.show_frac()
  print("b=",end='')
  b.show_frac()
  
  c=a+b
  print("a+b=",end='')
  c.show_frac()
  
  c=a+1
  print("a+1=",end='')
  c.show_frac()
  
  c=a-b
  print("a-b=",end='')
  c.show_frac()
  
  c=a*b
  print("a*b=",end='')
  c.show_frac()
  
  c=a/b
  print("a/b=",end='')
  c.show_frac()
  
  c=1/a
  print("1/a=",end='')
  c.show_frac()
  
  c=a**3
  print("a**3=",end='')
  c.show_frac()
  
  c=a**(-3)
  print("a**(-3)=",end='')
  ```

  输出：

  ```
  a=3/5
  b=7/10
  a+b=13/10
  a+1=8/5
  a-b=-1/10
  a*b=21/50
  a/b=6/7
  1/a=5/3
  a**3=27/125
  a**(-3)=125/27
  ```

  