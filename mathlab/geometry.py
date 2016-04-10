#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ####################################################################################
# Copyright (c) 2016, Enzo Tonti                                                     #
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
__all__ = ['pointLine']

def pointLine(xA, yA, xB, yB, xP, yP):
    """
    Given a line r passing through two points A and B and assigned a point P, 
    this function determines the projection of P on the line, evaluates its
    distance from the line and it indicates whether the projection is internal 
    to the segment AB.

    - equation describing a line between two points A-B:
    
    .. math:: 
       x = x_{\mathrm{A}} + s * (x_{\mathrm{B}} - x_{\mathrm{A}})

       y = y_{\mathrm{A}} + s * (y_{\mathrm{B}} - y_{\mathrm{A}})

       with: 0 \leq s \leq 1
    
    - equation of a line passing through P and orthogonal to A-B:
    
    .. math:: 
       x = x_{\mathrm{P}} + t * sin

       y = y_{\mathrm{P}} + t * cos
       
       sin = (y_{\mathrm{B}} - y_{\mathrm{A}})/L

       cos = (x_{\mathrm{B}} - x_{\mathrm{A}})/L
       
       L = \sqrt{(x_{\mathrm{B}} - x_{\mathrm{A}})^2 + (y_{\mathrm{B}} - y_{\mathrm{A}})^2 }


    - instersection between the two line:
    
    .. math::
       x_{\mathrm{A}} + s * (x_{\mathrm{B}} - x_{\mathrm{A}}) = x_{\mathrm{P}} + t * sin

       y_{\mathrm{A}} + s * (y_{\mathrm{B}} - y_{\mathrm{A}}) = y_{\mathrm{P}} - t * cos

    - system of equation:
    
    .. math::
       s * (x_{\mathrm{B}} - x_{\mathrm{A}}) - t * sin = x_{\mathrm{P}} -  x_{\mathrm{A}}

       s * (y_{\mathrm{B}} - y_{\mathrm{A}}) + t * cos = y_{\mathrm{P}} -  y_{\mathrm{A}}

     

    - coeffiecient matrix [A]

      +-------------------------------------------+----------------+
      | .. math:: x_{\mathrm{B}} - x_{\mathrm{A}} | .. math:: -sin |
      +-------------------------------------------+----------------+
      | .. math:: y_{\mathrm{B}} - y_{\mathrm{A}} | .. math:: cos  |
      +-------------------------------------------+----------------+

    - known term: b
    
    .. math::
       b = [x_{\mathrm{P}} -  x_{\mathrm{A}}; y_{\mathrm{P}} -  y_{\mathrm{A}}]
    
    - solutiuon:
    	
    .. math::
	   z = A/b
 	
 	distance = z(1);

    Parameters
    ----------
    xA, yA, xB, yB, xP, yP : float
        Coordinate (X, Y) of A, B and P.

    Returns
    -------
    distance
        Distance between P and the line
    """
    
    L = math.sqrt((xB-xA)*(xB-xA)+(yB-yA)*(yB-yA))
    cos = (xB-xA)/L
    sin = (yB-yA)/L
    
    
    # coeffiecient matrix:
    A = [[0 for y in xrange(2)] for x in xrange(2)]
    A[0][0] = xB-xA
    A[0][1] = -sin 
    A[1][0] = yB-yA
    A[1][1] = cos 
        
    # known term:
    b = [[0 for y in xrange(1)] for x in xrange(2)]
    b[0] = xP-xA
    b[1] = yP-yA
    
    # solution:
    z = numpy.linalg.solve(A, b)
    s = z[0]
    t = z[1]
    
    # projection point
    xQ=xA+s*(xB-xA);
    yQ=yA+s*(yB-yA);

    print ("projection point: ", xQ, yQ)
    print ("distance: ", t)
 
    plt.plot([xA, xA+1*(xB-xA)], [yA,yA+1*(yB-yA)])
    plt.plot([xP, xP+t*sin], [yP,yP-t*cos])
    plt.gca().set_aspect('equal', adjustable='box')
    
    plt.show()
    
    return t

