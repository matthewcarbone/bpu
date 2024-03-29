from warnings import warn

_dunamai = None
try:
    import dunamai as _dunamai
except ImportError:
    pass


def get_version(fallback_version="dev"):
    """A simple helper to get the version of your code using vcs.

    Parameters
    ----------
    fallback_version : str
        Fallback version to use if dunamai is not installed.

    Returns
    -------
    str
        The version of the code extracted using VCS.
    """

    if _dunamai is None:
        warn(
            "Dynamic versioning requires dunamai, which has not been "
            "installed; install accord using a package manager, or use pip "
            "to install the desired version of dunamai. The fallback "
            f"version {fallback_version} will be used."
        )
        return fallback_version
    try:
        version = _dunamai.Version.from_any_vcs().serialize()
    except Exception as e:
        warn(
            "Something went wrong when attempting to all dunamai.Version. "
            f"Exception {e} was thrown. Are you using a local version of "
            "accord without having initialized git? That could cause the "
            f"issue. Falling back on {fallback_version}"
        )
        return fallback_version
    return version
