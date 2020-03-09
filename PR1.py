#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 27 20:15:06 2019

@author: ujjwal
"""
import numpy as np
import pylab as plt
####LONGITUDINAL STATIC STABILITY########

# Stick-fixed stability characteristics at design conditions
#parametr _input#
t = 0.4
epsilon = 0
v_ht = 0.58 
a_t = 0.1
i_w = 1
e_t = 0.8
i_t = -1.5 # calulated 
def momment_coef_not (a_t, v_ht, e_t, i_w, epsilon, t, delta_e):
    return (i_w + epsilon - i_t - t * delta_e)*a_t * v_ht * e_t

delta_e = np.linspace(-15, 15 ,7) 
table = {}
for val in delta_e:
    table[val] = momment_coef_not (a_t, v_ht, e_t, i_w, epsilon, t, val)
    

####### INPUt PARAMETRS #########
c_mac = -0.03
a_w = 0.15
diff_cm_cl = -0.1106
# alpha_w scaled
alpha_w = np.linspace(0,16,9)

def momment_coeff(c_mac,alpha_w, a_w, diff_cm_cl, c_mo):
    """
    function to calculate momment coeffiecient
    """
    return c_mac + alpha_w *a_w * diff_cm_cl + c_mo 
# rough plotting
for val in table:
    plt.plot(alpha_w ,  momment_coeff(c_mac,alpha_w, a_w, diff_cm_cl, table[val])
    ,linestyle = 'dashdot',linewidth = 3.0, label = str(val))

plt.legend(loc='upper right')
plt.xlabel("Angle of attack")
plt.ylabel('Momment coefficient')   
ax = plt.gca()  # gca stands for 'get current axis'
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))
plt.title('Stick-fixed stability characteristics at design conditions')

