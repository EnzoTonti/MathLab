#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ####################################################################################
# Copyright (c) 2016, Francesco De Carlo                                             #
# All rights reserved.                                                               #
#                                                                                    #
# Redistribution and use in source and binary forms, with or without                 #
# modification, are permitted provided that the following conditions are met:        #
#                                                                                    #
# * Redistributions of source code must retain the above copyright notice, this      #
#   list of conditions and the following disclaimer.                                 #
#                                                                                    #
# * Redistributions in binary form must reproduce the above copyright notice,        #
#   this list of conditions and the following disclaimer in the documentation        #
#   and/or other materials provided with the distribution.                           #
#                                                                                    #
# * Neither the name of project nor the names of its                                 #
#   contributors may be used to endorse or promote products derived from             #
#   this software without specific prior written permission.                         #
#                                                                                    #
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"        #
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE          #
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE     #
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE       #
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL         #
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR         #
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER         #
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,      #
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE      #
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.               #
# ####################################################################################

"""
Collection of geometry tutorials
"""

from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import numpy
import math
import matplotlib.pyplot as plt
import scipy as sp

__authors__ = "Enzo Tonti"
__credits__ = "Francesco De Carlo"
__copyright__ = "Copyright (c) 2016"
__version__ = "0.1.0"
__docformat__ = "restructuredtext en"
__all__ = ['point_line',
           'gravity_center',
           'electric_dipole']

def electric_dipole(charge_location):
    """
    To do: complete documentation

    Parameters
    ----------
    charge_location
        Coordinate ....
    """

    charge_x = []    
    charge_y = []    
    for i in xrange(len(charge_location)):        
        charge_x.append(charge_location[i][0])        
        charge_y.append(charge_location[i][1])

    n = 20  
    p = 0.5
    c = 1
    Q1 = +1.0
    Q2 = -1.0
    fs = 0.4;
    for i in range(1, n):        
        for j in range(1, n):            
            x = -5.25 + i * p       
            y = -5.25 + j * p
            r1 = math.sqrt(math.pow((x - charge_x[0]), 2) +  math.pow((y - charge_y[0]), 2))
            r2 = math.sqrt(math.pow((x - charge_x[1]), 2) + math.pow((y - charge_y[1]), 2))
            Ex= c * Q1 * (x - charge_x[0]) / math.pow(r1, 3) + c * Q2* (x - charge_x[1]) / math.pow(r2, 3)
            Ey= c * Q1 * (y- charge_y[0]) / math.pow(r1, 3) + c * Q2* (y- charge_y[1]) / math.pow(r2, 3)       
            xa = x + fs * Ex
            ya = y + fs * Ey             
            s1 = math.pow((x - charge_x[0]), 2) + math.pow((y - charge_y[0]), 2)
            s2 =  math.pow((x - charge_x[1]), 2) +  math.pow((y - charge_y[0]), 2)            
            if  (s1 > p) & (s2 > p):                
                plt.plot([x, xa], [y, ya])
                plt.gca().set_aspect('equal', adjustable='box')
                plt.show()


def gravity_center(points):
    """
    To do: complete documentation

    Parameters
    ----------
    points
        Coordinate ....
    """

    n_points = len(points)
    n_sides = n_points - 1
    print (n_points, n_sides)
    
    x = []    
    y = []    
    for i in xrange(n_points):        
        x.append(points[i][0])        
        y.append(points[i][1])

    print ("x[]", x)
    print ("y[]", y)
    for k in range (0, n_points):
        plt.plot([0, x[k]], [0, y[k]])

    area = []
    for k in range (0, n_sides):
        area.append(((x[k] * y[k+1]) - (x[k+1] * y[k])) / 2.0)
    print ("area[]:", area)
    
    total_area = 0
    for k in range (0, n_sides):
        total_area += area[k]
        k += 1
        
    print ("total area: ", total_area)   
    xg = []
    yg = []
    for k in range (0, n_sides):
        xg.append((0+x[k]+x[k+1])/float(n_sides-1))
        yg.append((0+y[k]+y[k+1])/float(n_sides-1))
  
    s = 0
    t = 0
    for k in range (0, n_sides):
        s = s + area[k]*xg[k];        
        t = t + area[k]*yg[k];

    XG = s/total_area
    YG = t/total_area

    plt.scatter(x,y)
    plt.plot(x, y)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.scatter(XG, YG)    plt.show()    


def point_line(xa, ya, xb, yb, xp, yp):
    """
    Given a line r passing through two points A and B and assigned a point P, 
    this function determines the projection of P on the line, evaluates its
    distance from the line and it indicates whether the projection is internal 
    to the segment AB.

    Parameters
    ----------
    xa, ya, xb, yb, xp, yp : float
        Coordinate (X, Y) of A, B and P.

    Returns
    -------
    distance
        Distance between P and the line
    """
    
    length = math.sqrt((xb-xa)*(xb-xa)+(yb-ya)*(yb-ya))
    cos = (xb-xa)/length
    sin = (yb-ya)/length
    
    
    # coeffiecient matrix:
    A = [[0 for y in xrange(2)] for x in xrange(2)]
    A[0][0] = xb-xa
    A[0][1] = -sin 
    A[1][0] = yb-ya
    A[1][1] = cos 
        
    # known term:
    b = [[0 for y in xrange(1)] for x in xrange(2)]
    b[0] = xp-xa
    b[1] = yp-ya
    
    # solution:
    z = numpy.linalg.solve(A, b)
    s = z[0]
    t = z[1]
    
    # projection point
    xq=xa+s*(xb-xa);
    yq=ya+s*(yb-ya);

    print ("projection point: ", xq, yq)
    print ("distance: ", t)
 
    plt.plot([xa, xa+1*(xb-xa)], [ya,ya+1*(yb-ya)])
    plt.plot([xp, xp+t*sin], [yp,yp-t*cos])
    plt.gca().set_aspect('equal', adjustable='box')
    
    plt.show()
    
    return t

