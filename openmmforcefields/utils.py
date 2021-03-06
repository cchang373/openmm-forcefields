from pkg_resources import resource_filename

def get_ffxml_path():
    """
    Return the path where OpenMM ffxml forcefield files are stored in this package.

    Returns
    -------
    path : str
        The absolute path where OpenMM ffxml forcefield files are stored in this package
    """
    return resource_filename('openmmforcefields', 'ffxml')
