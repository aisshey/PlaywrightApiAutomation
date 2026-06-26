# Separate file: google_login_page.py
class GoogleLoginPage:
    def __init__(self, page):
        self.page = page
    
    def enter_email(self, email):
        self.page.fill("#identifierId", email)
    
    def click_next(self):
        self.page.click('//*[@id="identifierNext"]')
    
    def enter_password(self, password):
        self.page.fill('//*[@id="password"]/div[1]/div/div[1]/input', password)
    
    def click_password_next(self):
        self.page.locator("#passwordNext").click()
    
    def login(self, email, password):
        self.enter_email(email)
        self.click_next()
        self.enter_password(password)
        self.click_password_next()