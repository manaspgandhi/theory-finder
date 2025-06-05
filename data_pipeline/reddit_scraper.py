# import praw
# from typing import List, Dict

# # TODO: Fill in with your Reddit API credentials
# REDDIT_CLIENT_ID = 'your_client_id'
# REDDIT_CLIENT_SECRET = 'your_client_secret'
# REDDIT_USER_AGENT = 'theory-finder-agent'

# def search_reddit(query: str, limit: int = 10) -> List[Dict]:
#     """Search Reddit for posts matching the query."""
#     # TODO: Implement Reddit search using PRAW
#     return [] 

from selenium import webdriver
from selenium.webdriver.remote.remote_connection import RemoteConnection
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from browserbase import Browserbase
import os
from dotenv import load_dotenv
from pathlib import Path

env_path = Path("..") / ".env"
load_dotenv(dotenv_path=env_path)
api_key = os.getenv("BROWSERBASE_API_KEY")

bb = Browserbase(api_key=api_key)

class CustomRemoteConnection(RemoteConnection):
    _signing_key = None

    def __init__(self, remote_server_addr: str, signing_key: str):
        super().__init__(remote_server_addr)
        self._signing_key = signing_key

    def get_remote_connection_headers(self, parsed_url, keep_alive=False):
        headers = super().get_remote_connection_headers(parsed_url, keep_alive)
        headers.update({'x-bb-signing-key': self._signing_key})
        return headers


def run():
    session = bb.sessions.create(project_id=os.environ["BROWSERBASE_PROJECT_ID"])
    custom_conn = CustomRemoteConnection(session.selenium_remote_url, session.signing_key)
    options = webdriver.ChromeOptions()
    driver = webdriver.Remote(custom_conn, options=options)
    query = "severance theories after:2025-03-01"

    #go to google first
    driver.get("https://www.google.com")
    get_title = driver.title
    print(get_title)
    # Make sure to quit the driver so your session is ended!
    driver.quit()

run()