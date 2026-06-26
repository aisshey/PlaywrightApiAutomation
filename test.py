# from playwright.sync_api import sync_playwright
# import time


# with sync_playwright() as p:
#     browser = p.chromium.launch(headless=False)
#     context = browser.new_context()
#     newpage = context.new_page()
#     newpage.goto('https://the-internet.herokuapp.com/')
#     newpage.wait_for_load_state('networkidle')  # add this!

#     nnewcontexttwo = context.new_page()
#     nnewcontexttwo.goto('https://the-internet.herokuapp.com/login')
#     nnewcontexttwo.wait_for_load_state('networkidle')
   
#     nnewcontexttwo.locator('xpath=//*[@id="username"]').fill('tmsmith')
#     nnewcontexttwo.locator('xpath=//*[@id="password"]').fill('SuperSecretPassword!')
#     nnewcontexttwo.locator('xpath=//*[@id="login"]/button/i').click()
#     error = newpage.locator('#flash').text_content()
#     print("Error message:", error)
    
#     input("press enter to close...")
#     nnewcontexttwo.locator('xpath=//*[@id="content"]/div/a').click()
#     time.sleep(5)
#herok#login page example
# from playwright.sync_api import sync_playwright
# import time
# with sync_playwright() as p:
#     browser = p.chromium.launch(headless=False)
#     context = browser.new_context()
#     newpage = context.new_page()
#     newpage.goto('https://the-internet.herokuapp.com/')
#     page2 = context.new_page()
#     page2.goto('https://the-internet.herokuapp.com/login')
#     page2.locator('xpath=//*[@id="username"]').fill('ttomsmith')

#     page2.locator('//*[@id="password"]').fill('SuperSecretPassword!')
#     page2.locator('//*[@id="login"]/button').click()
#     error = newpage.locator('xpath=//*[@id="flash"]').text_content()
#     print("Error message:", error)  
#     time.sleep(5)

#https://practice.expandtesting.com/login
# from playwright.sync_api import sync_playwright
# import time
# with sync_playwright() as p:
#     browser = p.chromium.launch(headless=False)
#     context = browser.new_context()
#     newpage = context.new_page()
#     newpage.wait_for_load_state('networkidle')

#     newpage.goto('https://practice.expandtesting.com/login')
#     newpage.locator('xpath=//*[@id="username"]').fill('practice')
#     newpage.locator('xpath=//*[@id="password"]').fill('SuperSecretPassword!')
#     newpage.locator('xpath=//*[@id="submit-login"]').click()
#     newpage.wait_for_load_state('networkidle')

#     newpage.locator('xpath=//*[@id="core"]/div/div/a').click()
#     newpagetwo=context.new_page()

#     newpagetwo.goto('https://practice.expandtesting.com/register')
#     newpagetwo.wait_for_load_state('networkidle')

#     newpagetwo.get_by_label('Username').fill('usernametest')
#     newpagetwo.get_by_label('Password').nth(0).fill('Password@123')      # first password field
#     newpagetwo.get_by_label('Password').nth(1).fill('Password@123')      # confirm password field
#     newpagetwo.locator('xpath=//*[@id="register"]/button').click()
#     newpagetwo.wait_for_load_state('networkidle')
#     time.sleep(5)


# ============================================================
# Website: The Internet - Herokuapp
# URL: https://the-internet.herokuapp.com/
# Test: Login and Logout
# Date: 25-06-2026
# ============================================================
from playwright.sync_api import sync_playwright
import time
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    internetone = context.new_page()
    internetone.goto('https://the-internet.herokuapp.com/')

    internetone.get_by_text('Form Authentication').click()
    internetone.wait_for_load_state('networkidle')

    internetone.get_by_label('Username').fill('tomsmith')
    internetone.get_by_label('Password').fill('SuperSecretPassword!')
    internetone.locator('xpath=//*[@id="login"]/button').click()
    internetone.wait_for_load_state('networkidle')
    internetone.get_by_role('link',name='Logout').click()
    internetone.wait_for_load_state('networkidle') 

# ============================================================
# Website: DemoQA
# URL: https://demoqa.com/login
# Test: Login
# Date: 25-06-2026
# ============================================================
    demoqa = context.new_page()
    demoqa.goto('https://demoqa.com/')
    demoqa.wait_for_load_state('networkidle')
    demoqa.get_by_role('link', name='Forms').click()
    formopen = context.new_page()
    formopen.goto('https://demoqa.com/login')
    formopen.wait_for_load_state('domcontentloaded')

    formopen.locator('#newUser').click()
    formopen.get_by_placeholder('First Name').fill('Ayesha')
    formopen.get_by_placeholder('Last Name').fill('Sulatan')
    formopen.get_by_placeholder('UserName').fill('aisha')
    formopen.get_by_placeholder('Password').fill('22January@9896')
    formopen.wait_for_load_state('domcontentloaded')

    formopen.locator('xpath=//*[@id="register"]').click()
    formopen.locator('xpath=//*[@id="gotologin"]').click()
    formopen.wait_for_load_state('networkidle')
    registration = context.new_page()
    registration.goto('https://demoqa.com/automation-practice-form')
    registration.wait_for_load_state('domcontentloaded')  # ✅
    registration.get_by_placeholder('First Name').fill('ayesha')
    registration.get_by_placeholder('Last Name').fill('Sultan')
    registration.locator('xpath=//*[@id="userEmail"]').fill('aishfxa@gmail.com')
    registration.locator('#gender-radio-2').click(force=True)
    registration.get_by_placeholder('Mobile Number').fill('9276363635')
    registration.locator('#dateOfBirthInput').fill('20 Jun 2026')
    registration.keyboard.press('Escape')
    registration.locator('#subjectsInput').fill('hi')
    registration.locator('xpath=//*[@id="hobbies-checkbox-1"]').click(force=True)
    registration.locator('#uploadPicture').set_input_files(r'C:\Users\Ayesha Sultan\Downloads\Transactions on Bus - 20260615200416.pdf')
    registration.get_by_placeholder('Current Address').scroll_into_view_if_needed()
    registration.get_by_placeholder('Current Address').fill('johar')
#   # State
    registration.locator('xpath=//*[@id="state"]').scroll_into_view_if_needed()
    registration.locator('xpath=//*[@id="state"]').click(force=True)
    registration.locator('#react-select-3-input').fill('NCR')
    registration.get_by_text('NCR', exact=True).click()

# # City
    registration.locator('#city').click(force=True)
    registration.locator('#react-select-4-input').fill('Delhi')
    registration.get_by_text('Delhi', exact=True).click()
    registration.locator('#submit').click()
    registration.locator('#closeLargeModal').click(force=True)
    registration.wait_for_load_state('networkidle')
    # ============================================================
# Website: OrangeHRM
# URL: https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
# Test: Login
# Date: 25-06-2026
# ============================================================
    orangehrm = context.new_page()
    orangehrm.goto('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
    orangehrm.get_by_placeholder('Username').fill('Admin')
    orangehrm.get_by_placeholder('Password').fill('admin123')
    orangehrm.locator('.oxd-button.oxd-button--medium.oxd-button--main.orangehrm-login-button').click()
    orangehrm.wait_for_load_state('networkidle')
    orangehrm.locator('.oxd-userdropdown-tab').click()
    orangehrm.wait_for_load_state('domcontentloaded')


    orangehrm.get_by_text('Logout').click()
    orangehrm.wait_for_load_state('networkidle')
    orangehrm.locator('.oxd-text.oxd-text--p.orangehrm-login-forgot-header').click()
    orangehrm.locator('.oxd-input.oxd-input--active').fill('aishdfa@gmail.com')
    orangehrm.locator('.oxd-button.oxd-button--large.oxd-button--secondary.orangehrm-forgot-password-button.orangehrm-forgot-password-button--reset').click()
    orangehrm.wait_for_load_state('domcontentloaded')
    orangehrm.wait_for_load_state('networkidle')

    # ============================================================
# Website: Practice
# URL:https://practice.expandtesting.com/
# Test: Login
# Date: 25-06-2026
# ============================================================

    practice = context.new_page()
    practice.goto('https://practice.expandtesting.com/', timeout=60000)
    practice.wait_for_load_state('domcontentloaded')
    practice.locator('xpath=//*[@id="examples"]/div[1]/div[2]/div/div[2]/div/a').scroll_into_view_if_needed()

    practice.locator('xpath=//*[@id="examples"]/div[1]/div[2]/div/div[2]/div/a').click()
    practice.wait_for_load_state('domcontentloaded')  # ✅
    # Close popup if it appears
    # close_btn = practice.locator('text=Close')
    # if close_btn.is_visible():
    #     close_btn.click(force=True)
    practice.wait_for_timeout(2000) 
    practice.locator('xpath=//*[@id="username"]').fill('practice')
    practice.locator('xpath=//*[@id="password"]').fill('SuperSecretPassword!')
    practice.locator('.btn.btn-bg.btn-primary.d-block.w-100').click()
    practice.wait_for_load_state('domcontentloaded')
    practice.go_back()
    practice.locator('xpath=//*[@id="core"]/div/div[1]/div[1]/div/p[3]/a').click()
    practice.locator('xpath=//*[@id="core"]/div/div/a').click()
    practice.locator('xpath=//*[@id="core"]/div/div[1]/div[1]/div/p[3]/a').click()
    practice.wait_for_load_state('domcontentloaded')
    practice.locator('xpath=//*[@id="username"]').fill('aish')
    practice.locator('xpath=//*[@id="password"]').fill('22January@9896')

    practice.locator('xpath=//*[@id="confirmPassword"]').fill('22January@9896')
    practice.locator('xpath=//*[@id="register"]/button').click()
    practice.wait_for_load_state('domcontentloaded')

    # ============================================================
# Website: Saucedemo
# URL: https://www.saucedemo.com/
# Test: Login
# Date: 25-06-2026
# ============================================================
    saucedemo = context.new_page()
    saucedemo.goto('https://www.saucedemo.com/')
    saucedemo.locator('#user-name').fill('standard_user')
    saucedemo.locator('#password').fill('secret_sauce')
    saucedemo.locator('#login-button').click()
    saucedemo.wait_for_load_state('domcontentloaded')
    saucedemo.locator('#react-burger-menu-btn').click()
    saucedemo.locator('#logout_sidebar_link').click()
    saucedemo.wait_for_load_state('domcontentloaded')
#     ============================================================
# Website: automationexcercise
# URL: https://automationexercise.com/login
# Test: Login
# Date: 25-06-2026
# ============================================================
    automationexcercise = context.new_page()
    automationexcercise.goto('https://automationexercise.com/login')
    automationexcercise.locator('[data-qa="signup-name"]').fill('aisha')
    automationexcercise.locator('[data-qa="signup-email"]').fill('afyrfdefdee@gmail.com')
    automationexcercise.locator('[data-qa="signup-button"]').click()
    automationexcercise.wait_for_load_state('domcontentloaded')
    automationexcercise.locator('label[for="id_gender1"]').click(force=True)
    automationexcercise.locator('[data-qa="password"]').fill('22January@9896')
    automationexcercise.locator('#days').click()
    automationexcercise.locator('#days').select_option('1')
    automationexcercise.locator('#months').select_option('4')
    automationexcercise.locator('#years').click(force=True)
    automationexcercise.locator('#years').scroll_into_view_if_needed()
    automationexcercise.locator('#years').select_option('2000')
    
    automationexcercise.keyboard.press('Escape')    
    automationexcercise.locator('input[type="checkbox"]').first.click(force=True)
    automationexcercise.get_by_text('Receive special offers from our partners!').click(force=True)
    automationexcercise.locator('[data-qa="first_name"]').fill('Ayesha')
    automationexcercise.locator('[data-qa="last_name"]').fill('sultan')
    automationexcercise.locator('[data-qa="company"]').fill('factor')
    automationexcercise.locator('[data-qa="address"]').fill('johar')
    automationexcercise.locator('[data-qa="state"]').fill('NT')
    automationexcercise.locator('#country').select_option(label='India')
    automationexcercise.locator('[data-qa="zipcode"]').fill('03045')
    automationexcercise.locator('[data-qa="mobile_number"]').fill('0304233232')
    automationexcercise.locator('[data-qa="city"]').fill('kara')
    automationexcercise.locator('[data-qa="create-account"]').click()
    print(automationexcercise.url)  # page alive hai?
    automationexcercise.wait_for_load_state('domcontentloaded')
    automationexcercise.get_by_role('link', name='Continue').click()
    automationexcercise.wait_for_load_state('domcontentloaded')
    automationexcercise.locator(['data-qa="continue-button"']).click
    automationexcercise.get_by_role('link', name='Logout').click()
    automationexcercise.wait_for_load_state('domcontentloaded')
    login = context.new_page()
    login.goto('https://automationexercise.com/login')
    login.wait_for_load_state('domcontentloaded')
    login.locator('[data-qa="login-email"]').fill('aishaidu8@gmail.com')
    login.locator('[data-qa="login-password"]').fill('22January@9896')
    login.locator('[data-qa="login-button"]').click()

    print(login.url)
   #     ============================================================
# Website: automationexcercise
# URL: https://demo.guru99.com/test/newtours/register.php
# Test: Login
# Date: 25-06-2026
# ============================================================ 
    demoguru = context.new_page()
    demoguru.goto('https://demo.guru99.com/test/newtours/register.php')
    demoguru.locator('[name="firstName"]').fill('Ayesa')
    demoguru.locator('[name="lastName"]').fill('Sultan')
    demoguru.locator('[name="phone"]').fill('03058855570')
    demoguru.locator('[name="userName"]').fill('aisha123')
    demoguru.locator('[name="address1"]').fill('johar')
    demoguru.locator('[name="city"]').fill('johar')
    #province
    demoguru.locator('[name="state"]').fill('sindh')
    #postalcode
    demoguru.locator('[name="postalCode"]').fill('32344')
    demoguru.locator('[name="country"]').click()
    demoguru.locator('[name="country"]').select_option(value='PAKISTAN')
    demoguru.keyboard.press('Escape')
    demoguru.locator('[name="email"]').fill('aishaidu@gmail.com')
    demoguru.locator('[name="password"]').fill('22January@9896')
    demoguru.locator('[name="confirmPassword"]').fill('22January@9896')
    demoguru.locator('[name="submit"]').click()
    demoguru.wait_for_load_state('networkidle')
    demoguru.get_by_role('link', name='sign-in').click()
    demoguru.locator('[name="userName"]').fill('mercury')
    demoguru.locator('[name="password"]').fill('mercury')
    demoguru.locator('[name="submit"]').click()
    # Registration ke baad URL print karo
    demoguru.wait_for_load_state('domcontentloaded')
    print(demoguru.url)


# #     ============================================================
# # Website: parabank
# # URL: https://parabank.parasoft.com/parabank/register.htm
# # Test: Login
# # Date: 25-06-2026
# # ============================================================

    parabank = context.new_page()
    parabank.goto('https://parabank.parasoft.com/parabank/register.htm')
    parabank.locator('[id="customer.firstName"]').fill('Ayesha')
    parabank.locator('[id="customer.lastName"]').fill('Sultan')
    parabank.locator('[id="customer.address.street"]').fill('Johar')
    parabank.locator('[id="customer.address.city"]').fill('Karachi')
    parabank.locator('[id="customer.address.state"]').fill('Sindh')

    parabank.locator('[id="customer.address.zipCode"]').fill('03045')
    parabank.locator('[id="customer.phoneNumber"]').fill('03058855570')
    parabank.locator('[id="customer.ssn"]').fill('1234567')
    parabank.locator('[id="customer.username"]').fill('aisrredhgy3')
    parabank.locator('[id="customer.password"]').fill('22January@9896')
    parabank.locator('[id="repeatedPassword"]').fill('22January@9896')
    parabank.locator('[value="Register"]').click()
    parabank.wait_for_load_state('domcontentloaded')
    parabank.goto('https://parabank.parasoft.com/parabank/register.htm',  timeout=60000)
    parabank.wait_for_load_state('domcontentloaded')

    parabank.locator('[name="username"]').fill('aisrredhgy3')
    parabank.locator('[name="password"]').fill('22January@9896')
    parabank.locator('[value="Log In"]').click()
    parabank.get_by_role('link', name='Log Out').click()

    
#     ============================================================
# Website: demoblazee
# URL: https://www.demoblaze.com/
# Test: Login
# Date: 25-06-2026
# ============================================================

    demoblaze = context.new_page()
    demoblaze.goto('https://www.demoblaze.com/')
    demoblaze.wait_for_load_state('domcontentloaded')
    demoblaze.locator('#signin2').click()
    demoblaze.locator('#sign-username').fill('aiai=du8@gmail.com')
    demoblaze.locator('#sign-password').fill('22January@9896')
    demoblaze.get_by_role('button', name='Sign up').click()
#Sign in
    demoblaze.locator('#login2').click()
    demoblaze.locator('#loginusername').fill('aishaidu8@gmail.com')
    demoblaze.locator('#loginpassword').fill('22January@9896')
    demoblaze.get_by_role('button', name='Log in').click()
    demoblaze.wait_for_load_state('domcontentloaded')
    demoblaze.locator('[onclick="logOut()"]').click()



#     ============================================================
# Website: Naveen
# URL: https://naveenautomationlabs.com/opencart/
# Test: Login
# Date: 25-06-2026
# ============================================================
    naveen = context.new_page()
    naveen.goto('https://naveenautomationlabs.com/opencart/')
    naveen.wait_for_load_state('domcontentloaded')

    # Hover karo pehle
    naveen.locator('[title="My Account"]').click()
    naveen.wait_for_timeout(1000)

    # Phir Login click karo
    naveen.get_by_role('link', name='Register').click()
    naveen.wait_for_load_state('domcontentloaded')
    naveen.get_by_placeholder('First Name').fill('Ayesha')
    naveen.get_by_placeholder('Last Name').fill('Sultan')
    naveen.get_by_placeholder('E-Mail').fill('arfffdjggtt@gmail.com')
    naveen.get_by_placeholder('Telephone').fill('03058s855570')
    naveen.locator('#input-password').fill('22January@9896')
    naveen.get_by_placeholder('Password Confirm').fill('22January@9896')
    naveen.locator('input[name="newsletter"][value="0"]').click()
    naveen.locator('input[type="checkbox"][value="1"]').click()
    naveen.locator('input[type="submit"]').click()
    naveen.wait_for_load_state('domcontentloaded')
    naveen.get_by_role('link', name='Continue').click()
    naveen.locator('[title="My Account"]').click()
    naveen.locator('#top-links').get_by_role('link', name='Logout').click()
    naveen.wait_for_load_state('domcontentloaded')
    naveen.get_by_role('link', name='Continue').click()
    naveen.wait_for_load_state('domcontentloaded')
    naveentwo = context.new_page()
    naveentwo.goto('https://naveenautomationlabs.com/opencart/index.php?route=account/login')
    naveentwo.wait_for_load_state('networkidle')
    naveentwo.wait_for_timeout(2000)
    naveentwo.get_by_placeholder('E-Mail Address').fill('aishaidu8@gmail.com')
    naveentwo.get_by_placeholder('Password').fill('22January@9896')
    naveentwo.locator('input[value="Login"]').click()













    







    time.sleep(10)







