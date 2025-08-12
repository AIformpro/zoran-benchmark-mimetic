from zbm.core import run

def test_run_keys():
    out = run("bonjour zoran")
    for k in ["densite", "coherence", "latence_ms", "transfert", "persistance", "elapsed_ms"]:
        assert k in out
    assert 0.0 <= out["densite"] <= 1.0
    assert 0.0 <= out["coherence"] <= 1.0
    assert isinstance(out["latence_ms"], int)
