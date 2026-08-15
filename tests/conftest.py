import sys
from importlib.util import find_spec
from typing import Any

import pytest


def has_module(library: str):
    """Finds out if library exists without executing any code for the library."""
    return find_spec(library) is not None


PARAMS = [pytest.param(("asyncio", {"use_uvloop": False}), id="asyncio")]

# NOTE: Extensions are optional now...
if has_module("winloop" if sys.platform == "win32" else "uvloop"):
    PARAMS.append(pytest.param(("asyncio", {"use_uvloop": True}), id="asyncio+uvloop"))

if has_module("rsloop"):
    import rsloop

    PARAMS.append(
        pytest.param(
            ("asyncio", {"loop_factory": rsloop.new_event_loop}), id="asyncio+uvloop"
        )
    )


if has_module("trio"):
    PARAMS.append(
        pytest.param(
            ("trio", {"restrict_keyboard_interrupt_to_checkpoints": True}),
            id="trio",
        )
    )


@pytest.fixture(params=PARAMS)
def anyio_backend(request: pytest.FixtureRequest) -> Any:
    return request.param


@pytest.fixture(
    params=[
        (
            "[\\%\t\r+C_",
            b"$2b$05$tNnwrSVINowzZKREwREpGu",
            "$2b$05$tNnwrSVINowzZKREwREpGu53tme485pApf/qQiFT/Uyu4mBqvMwQK",
        ),
        (
            "[>zqN`|u",
            b"$2b$05$2ngkduSwlMBQ3kAeonLv0e",
            "$2b$05$2ngkduSwlMBQ3kAeonLv0eSO1H8/KpQvJux1azbrHNSl1itpfJryi",
        ),
        (
            "6nsc\\JTe",
            b"$2b$05$Y7t.NA21lmwZ.9HdAcP4oO",
            "$2b$05$Y7t.NA21lmwZ.9HdAcP4oOZ2ete9cuYTSEjlbQepSpTf78pwKhPLC",
        ),
        (
            "cc1?D(j1",
            b"$2b$05$02pYIjuDBBxEltrSyz952e",
            "$2b$05$02pYIjuDBBxEltrSyz952eQoy1fuJByrCHMk4rPQVE7uRErWvhmYa",
        ),
        (
            "|Us}Q+'+",
            b"$2b$05$UJ6QhvXy1S8TMChvVGkd7O",
            "$2b$05$UJ6QhvXy1S8TMChvVGkd7OJGDQEf60z1w2qzyPD00LyViA7i4yrfW",
        ),
        (
            "HO.001$8",
            b"$2b$05$q9JZy.c1y.z31dwDWwxFTO",
            "$2b$05$q9JZy.c1y.z31dwDWwxFTOkNmwBI0oEkDjUTGlXk38AJwUAQpPG1e",
        ),
        (
            "<75X,`?|",
            b"$2b$05$YOTWLt74pn9rfhfLXoQYIO",
            "$2b$05$YOTWLt74pn9rfhfLXoQYIOEUw2/keoZ0XV79z6TNkfCpddxwg5b0.",
        ),
        (
            "l@$7\t[dq",
            b"$2b$05$1pUpz4E.Gm7UhbWiA4cpUe",
            "$2b$05$1pUpz4E.Gm7UhbWiA4cpUeOrVVPecN1oRyokdp7RVhJ4J/xhIGt76",
        ),
        (
            "E :CQ\"'%",
            b"$2b$05$SZHPks7f2ruKPV6OJxLuMu",
            "$2b$05$SZHPks7f2ruKPV6OJxLuMu6fD/8rNEtXJld/uMBSQIPVF6Twlo.4u",
        ),
        (
            "C>aH2[/f",
            b"$2b$05$NTbklOua640Hp/wMxiE5AO",
            "$2b$05$NTbklOua640Hp/wMxiE5AOzpF.BtOnrxHfx29yL9xovBn1fPVW.im",
        ),
    ]
)
def pass_and_salt(request: pytest.FixtureRequest) -> tuple[str, bytes, str]:
    return request.param
