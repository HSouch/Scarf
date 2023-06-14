import scarf
from matplotlib import pyplot as plt



def segment_plot(debl, cat, out_fn = "segment_plot.pdf", xlim=None, ylim=None):
    """ Generate an overall map showing the segments generated using the moment 0 map.
        Used for internal plotting routines.

    Args:
        debl (_type_): The deblended photutils segmentation map.
        cat (_type_): Catalog of corresponding morpological parameters.
        out_fn (str, optional): Output filename. Defaults to "segment_plot.pdf".
        xlim (tuple): The x-limits for the plot.
        ylim (tuple): The y-limits for the plot.
    """
    fig, ax = plt.subplots(1,1, figsize=(5,8))
    plt.imshow(debl, origin="lower")

    # Set x,y limits if specified by user.
    if xlim is not None:
        plt.xlim(xlim[0], xlim[1])
    if ylim is not None:
        plt.ylim(ylim[0], ylim[1])

    # Plot the ellipses.
    for row in cat[:]:
        x, y = row["xcentroid"], row["ycentroid"]
        a, b, theta = row["semimajor_sigma"].value, row["semiminor_sigma"].value, row["orientation"].value

        coords = scarf.sample_ellipse(x, y, a, b, theta)
        plt.scatter(x, y, s=5)
        plt.plot(coords[0], coords[1])

    # Clean up, save, and close plot.
    plt.tight_layout()
    plt.xticks([])
    plt.yticks([])
    plt.savefig(out_fn, dpi=200)
    plt.close()