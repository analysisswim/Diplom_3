## Diplom_3 UI tests (Stellar Burgers)

### Install
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

### Run
pytest

### Run headless
pytest --headless

### Allure
pytest --alluredir=allure-results
allure serve allure-results
