
'''
USE:
	pip install --user PyAbel

Perform forward abel transform on RHO data
Called in vpsolver.py
outputs image of the RHO_array and forward and inverse abel transformations
'''
import abel
import numpy as np
import matplotlib.pyplot as plt

#PUSH TO POST PROCESSING, TAKE IN SOLUTION.
#Look geco-post-process deficit angle

def forward_abel_transform(RHO):	
    #r_max,z_max - dimensions of quarter-image
    r_max = 2
    #resolution of images
    res = 500
    rvals = np.linspace(0,r_max,res)
    
    z_max = 2
    zvals = np.linspace(0,z_max,res)
	
    #naive double-for loop numpy array creation
    RHO_array_A = np.zeros((len(rvals), len(zvals)))

    for i in range(len(rvals)):
        for j in range(len(zvals)):
            r = rvals[i]
            z = zvals[j]
            RHO_array_A[j,i] = RHO(r,z)
	
    #printing for debugging	
    #print("RHO_array shape: ", RHO_array_A.shape)
    #print("RHO_array size: ", RHO_array_A.size)
    #print(RHO_array_A[0:])
    
	#It looks like the following 3 lines of code can be avoided
	#by using symmetry_axis attribute in pyabel? Check p.11 of
	#https://buildmedia.readthedocs.org/media/pdf/pyabel/latest/pyabel.pdf
	
	#These two lines create a reflection of the array across horiz. axis
	RHO_array_B = np.flipud(RHO_array_A)
    RHO_array_C = np.concatenate((RHO_array_B,RHO_array_A), axis=0)
	
	#this line mirrors over vert. axis
    RHO_array = np.concatenate((np.fliplr(RHO_array_C),RHO_array_C), axis=1)
	
	
	#Using 'hansenlaw' is much faster than 'direct' without cython implementation
    forward_abel = abel.Transform(RHO_array, direction='forward', method='hansenlaw').transform
    inverse_abel = abel.Transform(forward_abel, direction='inverse', method='hansenlaw').transform
    
	
	#forward_abel = abel.Transform(RHO_array, direction='inverse', method='hansenlaw').transform
    #inverse_abel = abel.Transform(forward_abel, direction='forward', method='hansenlaw').transform
    fig, axs = plt.subplots(1, 3, figsize=(6, 4))

	#Output saved in "demo/abel_out" directory
    #Constant multiple applied to second paramater alters contrast
    axs[0].imshow(RHO_array, clim=(0, np.max(RHO_array)*1.15), origin='lower')
    axs[1].imshow(forward_abel, clim=(0, np.max(forward_abel)*1.15), origin='lower')
    axs[2].imshow(inverse_abel, clim=(0, np.max(inverse_abel)*1.15), origin='lower')
    axs[0].set_title('Original')
    axs[1].set_title('Forward Transform')
    axs[2].set_title('Inverse Transform')
    plt.tight_layout()
    plt.savefig("abel_out/out.png")