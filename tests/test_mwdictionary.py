from dataclasses import asdict

import pytest

from mwthesaurus import __version__, MWClient


def test_version():
    assert __version__ == "0.1.0"


def test_sync_async(sync_result, async_result):
    assert all(sr == asr for (sr, asr) in zip(sync_result, async_result))


def test_asdict(sync_result, async_result):
    assert all(asdict(sr) == asdict(asr) for (sr, asr) in zip(sync_result, async_result))
    # If the async and sync results are equal, we can just test one or the other:
    for w in sync_result:
        w_dict = asdict(w)
        for k, v in w.__dict__.items():
            assert v == w_dict.get(k)