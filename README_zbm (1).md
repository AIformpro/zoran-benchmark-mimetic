# zoran-benchmark-mimetic

**Benchmark IA ↔ IA** — mesure la *densité*, la *cohérence*, la *latence*, le *transfert* et la *persistance* des sorties IA.  
Ce prototype est conçu pour tester la robustesse et la stabilité des modèles en interaction.

![Build](https://img.shields.io/github/actions/workflow/status/Alformpro/zoran-benchmark-mimetic/ci.yml?branch=main)
![License](https://img.shields.io/github/license/Alformpro/zoran-benchmark-mimetic)
![Python](https://img.shields.io/badge/python-3.10%2B-blue)

---

## 🚀 Installation

```bash
git clone https://github.com/Alformpro/zoran-benchmark-mimetic.git
cd zoran-benchmark-mimetic
python -m venv .venv && source .venv/bin/activate
pip install -e ".[test]"
```

---

## 🛠 Utilisation CLI

Exécuter le benchmark sur un texte donné :

```bash
zbm run --text "Bonjour Zoran, test mimétique."
```

Sortie exemple :
```json
{
  "densite": 0.833,
  "coherence": 0.833,
  "latence_ms": 164,
  "transfert": 1.0,
  "persistance": 1.0,
  "elapsed_ms": 0
}
```

---

## 📊 Métriques

- **Densité** : proportion de tokens non vides dans la sortie.
- **Cohérence** : mesure simple de diversité lexicale.
- **Latence** : temps de réponse simulé (ms).
- **Transfert** : stabilité de hachage après modification mineure.
- **Persistance** : robustesse face à une perturbation légère.

---

## 📂 Structure du projet

```
.github/workflows/ci.yml    # Intégration continue (tests)
src/zbm/                    # Code source du benchmark
tests/                      # Tests unitaires (pytest)
examples/                   # Exemples d'utilisation
```

---

## 🧪 Tests

```bash
pytest
```

---

## 📄 Licence

MIT — voir le fichier [LICENSE](LICENSE).
