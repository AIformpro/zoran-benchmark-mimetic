# zoran-benchmark-mimetic

Bench IA<->IA (prototype) — **densité, cohérence, latence, transfert, persistance**.

### Installation
```bash
pip install -e .
```

### CLI
```bash
zbm run --text "bonjour zoran"
```
→ renvoie un JSON avec les 5 métriques.

### Métriques (placeholders)
- **densité**: ratio de tokens non vides
- **cohérence**: score [0..1] simple basé sur répétitions
- **latence**: simulée (ms)
- **transfert**: hash-stabilité entre 2 passages
- **persistance**: stabilité après perturbation légère
