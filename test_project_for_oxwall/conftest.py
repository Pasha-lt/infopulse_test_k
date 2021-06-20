import json

import pytest
from selenium import webdriver
from oxwall_app import OxwallApp
from user_object import User
import os.path

PROJECT_DIR = os.path.dirname(__file__)

@pytest.fixture()
def driver(selenium):
    # Open site
    driver = selenium
    # driver.get("https://demo.oxwall.com")
    yield driver
    driver.quit()


@pytest.fixture()
def app(driver):
    base_url = "https://demo.oxwall.com"
    return OxwallApp(driver, base_url)


@pytest.fixture()
def login_user(app):
    user = User(username="demo", password="demo", real_name="Demo")
    app.login(user.username, user.password)
    yield user
    app.logout()


file_name = os.path.join(PROJECT_DIR, "data", "user_positive.json")
with open(file_name, encoding="utf8") as f:
    users_data = json.load(f)


@pytest.fixture(params=users_data, ids=[str(u) for u in users_data])
def user(request):
    user = User(**request.param)
    return user
