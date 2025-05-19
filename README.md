# license-checker
# 📦 License Compliance Checker

A modular Python CLI tool that scans your `requirements.txt` or `package.json` and checks the licenses of all listed dependencies.

## 🚀 Project Goal
Help developers and DevSecOps professionals identify **risky open-source licenses** (e.g., GPL, AGPL) early in the software supply chain.

## 🎯 Features
- ✅ Modular structure (CLI, parsers, license fetchers)
- ✅ Parse `requirements.txt` (Python) or `package.json` (Node.js)
- 🔍 Fetch license data via the [Libraries.io API](https://libraries.io/api)
- ⚠️ Flag potentially risky licenses (GPL, AGPL, LGPL, etc.)
- 🖥️ CLI interface with colorized output (using `rich`)
- 📂 Optional export of results to a JSON/CSV file (planned)

## 📦 Example Usage
```bash
python -m license_checker.cli --file sample_data/requirements.txt
```

Output:
```
Checking licenses for dependencies...

numpy==1.23.5 ........ BSD-3-Clause ✅
requests==2.28.2 ..... Apache-2.0 ✅
fastapi==0.89.0 ...... GPL-3.0 ⚠️ (Consider replacing)

⚠️ Risky licenses found! Review before distribution.
```

## 🛠️ Tech Stack
- Python 3.10+
- Libraries.io API (license metadata)
- `argparse` or `click` for CLI
- `rich` for formatting output

## 🧠 Skills You’ll Gain
- Python scripting & modular architecture
- Working with REST APIs
- Understanding open-source license risks
- Real-world DevSecOps tooling

## ✅ TODO
- [x] Set up modular project structure
- [ ] Implement CLI in `cli.py`
- [ ] Parse `requirements.txt` in `parsers.py`
- [ ] Query license data from API in `license_fetcher.py`
- [ ] Flag risky licenses and format output
- [ ] Add support for `package.json`
- [ ] Export results to CSV/JSON
- [ ] Add unit tests for modules

## 📄 License
MIT — feel free to use, fork, and contribute.

## 🙌 Contributions
Open to PRs or suggestions!

---

> Built as part of a 6-week DevSecOps + GenAI prep journey 🚀
