import numpy as np


def beam_area(bmaj, bmin):
    """ Return the Gaussian beam area. Beam will have units of bmaj * bmin.

    Args:
        bmaj (float): The major axis of the ellipse (BMAJ in most datacubes)
        bmin (float): The minor axis of the ellipse (BMIN in most datacubes)

    Returns:
        float: The area of the ellipse
    """
    return np.pi * bmaj * bmin / (4 * np.log(2))


def equiv_r(area):
    """ Generate the radius of a circular Gaussian beam with the same input area.

    Args:
        area (float): Beam area.

    Returns:
        float: Radius of circularized beam.
    """
    return np.sqrt(area * 4 * np.log(2) / np.pi)


def sample_ellipse(x, y, a, b, theta, num_points=100):
    """ Generate coordinates for an ellipse based on key input coordinates.

    Args:
        x (float): x position of ellipse centre.
        y (float): y position of ellipse centre.
        a (float): Semimajor axis of ellipse.
        b (float): Semiminor axis of ellipse.
        theta (float): Angle of ellpise (Clockwise from positive x-axis) in degrees.
        num_points (int, optional): Number of points to sample. Defaults to 100.

    Returns:
        np.ndarray: The two arrays of x coordinates and y coordinates.
    """
    # Convert theta to radians
    theta_rad = np.radians(theta)

    # Generate angles for sampling
    angles = np.linspace(0, 2*np.pi, num_points)
    
    # Parametric equation for the ellipse
    x_coords = x + a * np.cos(angles) * np.cos(theta_rad) - b * np.sin(angles) * np.sin(theta_rad)
    y_coords = y + a * np.cos(angles) * np.sin(theta_rad) + b * np.sin(angles) * np.cos(theta_rad)

    # Return the sampled coordinates as a NumPy array
    return np.ndarray((x_coords, y_coords))
