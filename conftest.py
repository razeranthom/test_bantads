import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import pytest

import bantads as b


@pytest.fixture(scope="session", autouse=True)
def preparar_ambiente():
    """Antes de tudo: limpa o cache e recria o seed via /reboot (sempre)."""
    b.cache_save({})   # começa a sessão sem tokens antigos
    b.post("/reboot")  # força o estado limpo a cada execução (garante testes isolados também)
    yield
