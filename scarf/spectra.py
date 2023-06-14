from photutils.aperture import aperture_photometry
from numpy import array


def get_spectra(cube, aper):
    """ Obtain spectra of cube at a given region. 
        Iterates through cube and 

    Args:
        cube (np.ndarray): The spectral datacube.
        aper: The input aperture. Can be any one of EllipticalAperture, CircularAperture, etc.

    Returns:
        np.ndarray: Returns array of the flux.
    """

    reg_flux = []
    for frame in cube:
        phot = aperture_photometry(frame, aper)

        reg_flux.append(float(phot["aperture_sum"]))
    return array(reg_flux)
