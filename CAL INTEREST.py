# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 07:45:08 2024

@author: admin
"""
sotien = 10000000
laisuat = 5.1/100
sonam = 0

while sotien < 15000000:
    sonam += 1
    sotien = sotien * (1 + laisuat)
    
    print("So tien sau", sonam, "nam:", sotien)
    
print("Sau", sonam, "ban se co 15000000 trieu,")
