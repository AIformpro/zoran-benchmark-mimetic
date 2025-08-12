import argparse, json, time, hashlib, random, os

def metric_density(text: str) -> float:
    tokens = [t for t in text.split() if t.strip()]
    return 0.0 if not text else min(1.0, len(tokens) / max(1, len(text.split())))

def metric_coherence(text: str) -> float:
    # simplistic: penalize too many repeated tokens
    toks = text.lower().split()
    if not toks: return 0.0
    uniq = len(set(toks))
    return round(uniq / len(toks), 3)

def metric_latency(text: str) -> int:
    # simulate deterministic latency based on hash prefix
    h = int(hashlib.sha256(text.encode()).hexdigest()[:6], 16)
    return 50 + (h % 150)  # 50..199 ms

def stable_hash(text: str) -> str:
    return hashlib.sha256(text.encode()).hexdigest()

def metric_transfer(text: str) -> float:
    # compare hash stability against a minor formatting change
    h1 = stable_hash(text)
    h2 = stable_hash(text.strip() + " ")
    return 1.0 if h1 == h2 else 0.0

def metric_persistence(text: str) -> float:
    # add small noise; check if density/coherence stable within tolerance
    d1, c1 = metric_density(text), metric_coherence(text)
    noisy = " ".join((text + "  ").split())  # collapse/expand spaces
    d2, c2 = metric_density(noisy), metric_coherence(noisy)
    ok = (abs(d1 - d2) <= 0.01) and (abs(c1 - c2) <= 0.02)
    return 1.0 if ok else 0.0

def run(text: str) -> dict:
    t0 = time.time()
    metrics = {
        "densite": round(metric_density(text), 3),
        "coherence": round(metric_coherence(text), 3),
        "latence_ms": metric_latency(text),
        "transfert": metric_transfer(text),
        "persistance": metric_persistence(text),
    }
    metrics["elapsed_ms"] = int((time.time() - t0) * 1000)
    return metrics

def main(argv=None):
    parser = argparse.ArgumentParser(prog="zbm", description="Zoran Benchmark Mimetic (prototype)")
    sub = parser.add_subparsers(dest="cmd")
    r = sub.add_parser("run")
    r.add_argument("--text", required=True, help="Texte d'entrée")
    args = parser.parse_args(argv)
    if args.cmd == "run":
        print(json.dumps(run(args.text), ensure_ascii=False))
    else:
        parser.print_help()
