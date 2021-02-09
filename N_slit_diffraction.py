#################
##### Program made by : Renu Raman Sahu ##########
#About########
#Program to calculate the intensity profile and simulate the image of the pattern for diffraction by
#N slits, with slit width a, slit spacing d and a given wavelength.
#################


############## Importing the libraries ##################
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
#(Optional comment) Rendering of labels in the plot will be nice if Latex is installed in the system 


################ INPUT PARAMETERS ##################
####################################################
wavelength= 632.0 #nm, the wavelength of the monochromatic source used
gap=7*wavelength   #nm, Slit to slit separation (nearest edges of consecutive slits) in nm
a=3*wavelength   #nm, Slit Width in nm
d=a+gap
N=4     #number of slits (should be an integer)
####################################################


########### FUNCTION FOR THE DIFFRACTION PATTERN #############
def diffraction_intensity_pattern(wavelength, a, d, N):
    # theta is the angular separation between the  point of observation and central maxima with respect to the center of  diffraction grating
    #We define an array named theta, with start value -pi/7, end value pi/7 and l_theta=1003 elements in the array 
    l_theta = 1000   # Length of the array theta, a large integer more than 1000
    theta = np.linspace(-np.pi/7.0, np.pi/7.0, l_theta)

    #### checking for theta[i]==0 to avoid intederminate terms of type 0/0. #####
    for i in range(l_theta):
         if (0==theta[i]):
             theta[i]=0.0000001
    #############################################################################

    sin_theta = np.sin(theta)

    d_by_wl = d/wavelength
    a_by_wl = a/wavelength

    beta = np.pi*a_by_wl*sin_theta

    ######### Factor due to slitwidth a ################
    sinB_by_B = (np.sin(beta)/beta)
    f1 = sinB_by_B**2

    ######## Factor due to N slits with separation d between each consecutive slits ###############
    sin_NAlpha_by_Alpha = (np.sin(N*d_by_wl*np.pi*sin_theta)/np.sin(d_by_wl*np.pi*sin_theta))
    f2 = sin_NAlpha_by_Alpha**2

    diffraction_intensity = f1*f2
    
    return theta, diffraction_intensity    





############## THE FOLLOWING FUNCTION IS FOR SIMULATION OF DIFFRACTION PATTERN ############

def plot_image(wavelength, a, d, N):
    ################ Calculates the intensity profile for given input parameters###################
    theta, diffraction_intensity = diffraction_intensity_pattern(wavelength, a, d, N)
    ###############################################################################################


    ##### The following two lines computes the fraction of incident photons at different regions on the screen ########
    photon_count = 120
    n_photon = (photon_count*diffraction_intensity/max(diffraction_intensity))



    ############# The following code determines the relative number of photons at different regions on the screen ###### 
    x_count =[]
    y_count =[]
    l_theta=len(theta)
    for i in range(l_theta-1):
        yc=np.random.uniform(theta[i], theta[i+1], int(n_photon[i]))
        xc=np.random.uniform(0.0, 1.0, int(n_photon[i]))
        x_count=np.append(x_count, xc)
        y_count=np.append(y_count, yc)

    ######################################################################################################################
    


    ###### The following code is for plotting the intensity profile and the simulated image of the pattern ###########

    title=' N='+str(N)+", Slit width = "+str(a)+' nm, Slit spacing = '+str(d)+' nm,  wavelength = '+str(wavelength)+' nm'
    fig, (intensity_profile, image)=plt.subplots(2, 1, sharex=False, figsize=(8, 8))
    fig.suptitle(title)
    
    intensity_profile.plot(theta, diffraction_intensity, '-', color='red', alpha=1)
    intensity_profile.set(xlabel=r'$\sin\theta$ ', ylabel=r'$I/I_{incident}$', title="Intensity profile (top),  simulated image of the pattern(bottom)")
    intensity_profile.set_xlim([-np.pi/7., np.pi/7.0])

    image.plot(y_count, x_count, '.', color='red', alpha=.30)
    image.set(xlabel=r'$\sin\theta$ ')
    image.get_yaxis().set_visible(False)
    image.set_xlim([-np.pi/7., np.pi/7.0])

    plt.show()




########Calling the function to plot the intensity profile and the simulated image of the pattern#####
plot_image(wavelength, a, d, N)


############ Thank You #################
    
