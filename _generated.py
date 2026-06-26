from playwright.sync_api import sync_playwright
from google_login_page import GoogleLoginPage

with sync_playwright() as r:
    browser = r.chromium.launch(headless=False)
    vid = browser.new_context(record_video_dir="videos/")
    newpage = vid.new_page()
    
    # Use POM!
    login = GoogleLoginPage(newpage)
    login.login("aysultan@creativechaos.co", "22January@9896")
    
    vid.close()