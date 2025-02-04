from importlib import resources

def get_flatland():
    """Get pathtoexample"Flatland"[1]_textfile.
    Returns
    -------
    pathlib.PosixPath
    Path tofile.
    References
    ----------
    .. [1]E.A.Abbott,"Flatland",Seeley&Co.,1884.
    """
    with resources.path("pycounts_co.data", "flatland.txt") as f:
        data_file_path = f
    return data_file_path