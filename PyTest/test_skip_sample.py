import sys

import pytest


@pytest.mark.skip(reason="not for this build")
def test_sample_skip():
    assert True


@pytest.mark.skipif(sys.version_info < (3.6), reason="will be skipped for this version")
def test_sample_skip_if():
    assert False


@pytest.mark.windows
def test_sample_windows():
    assert False


@pytest.mark.mac
def test_sample_mac():
    assert False
