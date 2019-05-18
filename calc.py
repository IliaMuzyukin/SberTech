#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 18 23:35:00 2019

"""
class Calculator:
    def __init__(self, num1, num2):
        self.num1=num1
        self.num2=num2
    def Add(self):
        return self.num1+self.num2
    def Sub(self):
        return self.num1-self.num2
    def Mul(self):
        return self.num1/self.num2
    def Div(self):
        return self.num1*self.num2
