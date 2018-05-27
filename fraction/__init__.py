# -*- coding: utf-8 -*-
"""
@author: Allen
"""
from __future__ import division

__version__='0.10'

INF=float('inf')

def make_frac(numerator=INF, denominator=INF, value=INF):
    return frac(numerator,denominator,value)   

class frac:
    """
    nt为分子，dt为分母
    """
    def __init__(self, numerator=INF, denominator=INF, value=INF):
        valid1=self.not_valid_frac(numerator, denominator)
        valid2=self.not_valid_value(value)
        if not valid1 and not valid2:
            raise RuntimeError('无效的分数构造，请检查是否分母为0')
        if valid1:
            self.nt=int(numerator)
            self.dt=int(denominator)
            if(self.dt<0):
                self.dt*=-1
                self.nt*=-1
            self.reduction()
            self.value=self.nt/float(self.dt)
        else:
            pass
            
        
    def not_valid_frac(self,numerator, denominator):
        if(numerator==INF or denominator==INF or denominator==0):
            return False
        else:
            return True
    def not_valid_value(self,value):
        if(value==INF):
            return False
        else:
            return True
        
    def reduction(self):
        """约分"""
        _gcd=gcd(self.nt,self.dt)
        self.nt//=_gcd
        self.dt//=_gcd

    def __add__(self,other):
        temp_type=type(other)
        if temp_type==int:
            other=frac(other,1)
        elif temp_type==float:
            other=frac(value=other)
        elif 'frac' not in str(temp_type):
            raise RuntimeError("无效的加法，请检查是否加数无效")
        _lcm=lcm(self.dt,other.dt)
        _nt=_lcm//self.dt*self.nt+_lcm//other.dt*other.nt
        _dt=_lcm
        frac_d=frac(_nt,_dt)
        return frac_d
    
    def __radd__(self,other):
        return self+other
    
    def __sub__(self,other):
        temp_type=type(other)
        if temp_type==int:
            other=frac(other,1)
        elif temp_type==float:
            other=frac(value=other)
        elif 'frac' not in str(temp_type):
            raise RuntimeError("无效的减法，请检查是否加数无效")
        _lcm=lcm(self.dt,other.dt)
        _nt=_lcm//self.dt*self.nt-_lcm//other.dt*other.nt
        _dt=_lcm
        frac_d=frac(_nt,_dt)
        return frac_d
       
    def __rsub__(self,other):
        frac_d=self-other
        frac_d.nt*=-1
        return frac_d
    
    def __mul__(self,other):
        temp_type=type(other)
        if temp_type==int:
            other=frac(other,1)
        elif temp_type==float:
            other=frac(value=other)
        elif 'frac' not in str(temp_type):
            raise RuntimeError("无效的乘法，请检查是否乘数无效")
        _nt=self.nt*other.nt
        _dt=self.dt*other.dt
        return frac(_nt,_dt)
    
    def __rmul__(self,other):
        return self*other
    
    def __truediv__(self,other):
        temp_type=type(other)
        if temp_type==int:
            other=frac(other,1)
        elif temp_type==float:
            other=frac(value=other)
        elif 'frac' not in str(temp_type):
            raise RuntimeError("无效的除法法，请检查是否操作数无效")
        _nt=self.nt*other.dt
        _dt=self.dt*other.nt
        return frac(_nt,_dt)
    
    def __rtruediv__(self,other):
        frac_d=self/other
        _nt=frac_d.dt
        _dt=frac_d.nt
        return frac(_nt,_dt)
    
    def __pow__(self,other):
        """分数的整数次幂操作，快速幂"""
        temp_type=type(other)
        if temp_type!=int:
            raise RuntimeError("哈哈该功能暂不支持，摸摸头")
        n=other
        if(n<0):
            pow_neg=True
            n=abs(n)
        else:
            pow_neg=False
        frac_d=frac(1,1)
        frac_op=frac(self.nt,self.dt)
        while(n!=0):
            if(n%2==1):
                frac_d*=frac_op
            frac_op*=frac_op
            n//=2
        if not pow_neg:
            return(frac(frac_d.nt,frac_d.dt))
        else:
            return(frac(frac_d.dt,frac_d.nt))
    
    def __rpow__(self,ohter):
        raise RuntimeError("哈哈该功能暂不支持，摸摸头")
    
    def __abs__(self):
        frac_d=frac(abs(self.nt),self.dt)
        return frac_d
    
    def __eq__(self,other):
        if self.nt==0 and other.nt==0: 
            return True
        if self.dt==other.dt and self.nt==other.nt:
            return True
        return False
    
    def doubling(self,mul):
        self.nt*=mul
        self.dt*=mul
        
    def show(self,retention=7):
        print("分数形式:%d/%d"%(self.nt,self.dt))
        print("浮点数形式:%.*f\n"%(retention,self.value))
    
    def show_frac(self):
        print("%d/%d"%(self.nt,self.dt))
    
    def show_value(self,retention=7):
        print("%.*f\n"%(retention,self.value))
        
    def __del__(self):
        pass


def gcd(a,b):
    """
    求ab的最大公约数
    """
    return gcd(b,a%b) if b!=0 else a
def lcm(a,b):
    """
    求ab的最小公倍数
    """
    return int(a*b/gcd(a,b))
