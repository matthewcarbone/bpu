from bpu.version import get_version


def test_get_version():
    fallback_version = "dev"
    version = get_version(fallback_version=fallback_version)
    assert version != fallback_version
