# ============================================================
# Project: Playwright Automation Suite
# Author: Ayesha Sultan
# Description: End-to-end automation for 10 websites
# Date: 25-06-2026
# Tech Stack: Python | Playwright
# ============================================================
# PROFESSIONAL TIPS:
# 1. Use page.wait_for_load_state() after every navigation
# 2. Prefer id/data-qa over xpath when possible
# 3. Use force=True only for hidden/covered elements
# 4. Always use exact=True for ambiguous text matches
# 5. Use select_option() for dropdowns, never fill()
# ============================================================

from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    # ✅ TIP: Use slow_mo=500 for debugging
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()

    # ============================================================
    # Website: The Internet (Herokuapp)
    # URL: https://the-internet.herokuapp.com/
    # Test: Login & Logout
    # Date: 25-06-2026
    # Locators Used: get_by_text, get_by_label, xpath
    # ============================================================
    internetone = context.new_page()
    internetone.goto('https://the-internet.herokuapp.com/')

    # Click on Form Authentication link
    internetone.get_by_text('Form Authentication').click()
    internetone.wait_for_load_state('networkidle')

    # Fill login credentials using label locator
    internetone.get_by_label('Username').fill('tomsmith')
    internetone.get_by_label('Password').fill('SuperSecretPassword!')

    # Click login button using xpath
    internetone.locator('xpath=//*[@id="login"]/button').click()
    internetone.wait_for_load_state('networkidle')

    # Logout using role locator
    internetone.get_by_role('link', name='Logout').click()
    internetone.wait_for_load_state('networkidle')

    # ============================================================
    # Website: DemoQA
    # URL: https://demoqa.com/login
    # Test: Register & Practice Form
    # Date: 25-06-2026
    # Locators Used: get_by_role, get_by_placeholder, id, xpath
    # ============================================================
    demoqa = context.new_page()
    demoqa.goto('https://demoqa.com/')
    demoqa.wait_for_load_state('networkidle')

    # Navigate to Forms section
    demoqa.get_by_role('link', name='Forms').click()

    # Open login page in new tab
    formopen = context.new_page()
    formopen.goto('https://demoqa.com/login')
    formopen.wait_for_load_state('domcontentloaded')

    # Click New User to register
    formopen.locator('#newUser').click()
    formopen.get_by_placeholder('First Name').fill('Ayesha')
    formopen.get_by_placeholder('Last Name').fill('Sulatan')
    formopen.get_by_placeholder('UserName').fill('aisha')
    formopen.get_by_placeholder('Password').fill('22January@9896')
    formopen.wait_for_load_state('domcontentloaded')

    # Submit registration and go to login
    formopen.locator('xpath=//*[@id="register"]').click()
    formopen.locator('xpath=//*[@id="gotologin"]').click()
    formopen.wait_for_load_state('networkidle')

    # ✅ TIP: Open practice form in new page for clean state
    registration = context.new_page()
    registration.goto('https://demoqa.com/automation-practice-form')
    registration.wait_for_load_state('domcontentloaded')

    # Fill personal information
    registration.get_by_placeholder('First Name').fill('ayesha')
    registration.get_by_placeholder('Last Name').fill('Sultan')
    registration.locator('xpath=//*[@id="userEmail"]').fill('aishfxa@gmail.com')

    # ✅ TIP: Use force=True for radio buttons — they are often hidden
    registration.locator('#gender-radio-2').click(force=True)
    registration.get_by_placeholder('Mobile Number').fill('9276363635')

    # Fill date and press Escape to close datepicker
    registration.locator('#dateOfBirthInput').fill('20 Jun 2026')
    registration.keyboard.press('Escape')

    registration.locator('#subjectsInput').fill('hi')

    # ✅ TIP: Use force=True for checkboxes inside labels
    registration.locator('xpath=//*[@id="hobbies-checkbox-1"]').click(force=True)

    # File upload using set_input_files
    registration.locator('#uploadPicture').set_input_files(
        r'C:\Users\Ayesha Sultan\Downloads\Transactions on Bus - 20260615200416.pdf'
    )

    # Scroll to address field before filling
    registration.get_by_placeholder('Current Address').scroll_into_view_if_needed()
    registration.get_by_placeholder('Current Address').fill('johar')

    # State dropdown — react-select requires click then fill
    registration.locator('xpath=//*[@id="state"]').scroll_into_view_if_needed()
    registration.locator('xpath=//*[@id="state"]').click(force=True)
    registration.locator('#react-select-3-input').fill('NCR')
    registration.get_by_text('NCR', exact=True).click()  # exact=True avoids partial matches

    # City dropdown
    registration.locator('#city').click(force=True)
    registration.locator('#react-select-4-input').fill('Delhi')
    registration.get_by_text('Delhi', exact=True).click()

    # Submit and close modal
    registration.locator('#submit').click()
    registration.locator('#closeLargeModal').click(force=True)
    registration.wait_for_load_state('networkidle')

    # ============================================================
    # Website: OrangeHRM
    # URL: https://opensource-demo.orangehrmlive.com
    # Test: Login, Logout, Forgot Password
    # Date: 25-06-2026
    # Locators Used: get_by_placeholder, CSS classes, get_by_text
    # ============================================================
    orangehrm = context.new_page()
    orangehrm.goto('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')

    # Login with admin credentials
    orangehrm.get_by_placeholder('Username').fill('Admin')
    orangehrm.get_by_placeholder('Password').fill('admin123')

    # ✅ TIP: Multiple CSS classes joined with dots (no spaces)
    orangehrm.locator('.oxd-button.oxd-button--medium.oxd-button--main.orangehrm-login-button').click()
    orangehrm.wait_for_load_state('networkidle')

    # Open user dropdown and logout
    orangehrm.locator('.oxd-userdropdown-tab').click()
    orangehrm.wait_for_load_state('domcontentloaded')
    orangehrm.get_by_text('Logout').click()
    orangehrm.wait_for_load_state('networkidle')

    # Test forgot password flow
    orangehrm.locator('.oxd-text.oxd-text--p.orangehrm-login-forgot-header').click()
    orangehrm.locator('.oxd-input.oxd-input--active').fill('aishdfa@gmail.com')
    orangehrm.locator('.oxd-button.oxd-button--large.oxd-button--secondary.orangehrm-forgot-password-button.orangehrm-forgot-password-button--reset').click()
    orangehrm.wait_for_load_state('domcontentloaded')
    orangehrm.wait_for_load_state('networkidle')

    # ============================================================
    # Website: Expand Testing
    # URL: https://practice.expandtesting.com/
    # Test: Login & Register
    # Date: 25-06-2026
    # Locators Used: xpath, CSS class
    # ============================================================
    practice = context.new_page()

    # ✅ TIP: Increase timeout for slow sites
    practice.goto('https://practice.expandtesting.com/', timeout=60000)
    practice.wait_for_load_state('domcontentloaded')

    # Scroll to login link and click
    practice.locator('xpath=//*[@id="examples"]/div[1]/div[2]/div/div[2]/div/a').scroll_into_view_if_needed()
    practice.locator('xpath=//*[@id="examples"]/div[1]/div[2]/div/div[2]/div/a').click()
    practice.wait_for_load_state('domcontentloaded')

    # ✅ TIP: Use wait_for_timeout for popups/animations
    practice.wait_for_timeout(2000)

    # Login with default credentials
    practice.locator('xpath=//*[@id="username"]').fill('practice')
    practice.locator('xpath=//*[@id="password"]').fill('SuperSecretPassword!')
    practice.locator('.btn.btn-bg.btn-primary.d-block.w-100').click()
    practice.wait_for_load_state('domcontentloaded')

    # Go back and register new account
    practice.go_back()
    practice.locator('xpath=//*[@id="core"]/div/div[1]/div[1]/div/p[3]/a').click()
    practice.locator('xpath=//*[@id="core"]/div/div/a').click()
    practice.locator('xpath=//*[@id="core"]/div/div[1]/div[1]/div/p[3]/a').click()
    practice.wait_for_load_state('domcontentloaded')

    # Register new user
    practice.locator('xpath=//*[@id="username"]').fill('aish')
    practice.locator('xpath=//*[@id="password"]').fill('22January@9896')
    practice.locator('xpath=//*[@id="confirmPassword"]').fill('22January@9896')
    practice.locator('xpath=//*[@id="register"]/button').click()
    practice.wait_for_load_state('domcontentloaded')

    # ============================================================
    # Website: Sauce Demo
    # URL: https://www.saucedemo.com/
    # Test: Login & Logout
    # Date: 25-06-2026
    # Locators Used: id
    # ============================================================
    saucedemo = context.new_page()
    saucedemo.goto('https://www.saucedemo.com/')

    # Login with standard user — predefined credentials
    saucedemo.locator('#user-name').fill('standard_user')
    saucedemo.locator('#password').fill('secret_sauce')
    saucedemo.locator('#login-button').click()
    saucedemo.wait_for_load_state('domcontentloaded')

    # Open burger menu and logout
    saucedemo.locator('#react-burger-menu-btn').click()
    saucedemo.locator('#logout_sidebar_link').click()
    saucedemo.wait_for_load_state('domcontentloaded')

    # ============================================================
    # Website: Automation Exercise
    # URL: https://automationexercise.com/login
    # Test: Register & Login
    # Date: 25-06-2026
    # Locators Used: data-qa, id, label[for], select_option
    # ============================================================
    automationexcercise = context.new_page()
    automationexcercise.goto('https://automationexercise.com/login')

    # Register new account
    automationexcercise.locator('[data-qa="signup-name"]').fill('aisha')
    automationexcercise.locator('[data-qa="signup-email"]').fill('afyrfdefdee@gmail.com')
    automationexcercise.locator('[data-qa="signup-button"]').click()
    automationexcercise.wait_for_load_state('domcontentloaded')

    # Select gender radio button using label[for]
    automationexcercise.locator('label[for="id_gender1"]').click(force=True)
    automationexcercise.locator('[data-qa="password"]').fill('22January@9896')

    # ✅ TIP: Use select_option() for dropdowns — never fill()
    automationexcercise.locator('#days').select_option('1')
    automationexcercise.locator('#months').select_option('4')
    automationexcercise.locator('#years').scroll_into_view_if_needed()
    automationexcercise.locator('#years').select_option('2000')
    automationexcercise.keyboard.press('Escape')

    # Select checkboxes
    automationexcercise.locator('input[type="checkbox"]').first.click(force=True)
    automationexcercise.get_by_text('Receive special offers from our partners!').click(force=True)

    # Fill address information using data-qa attributes
    automationexcercise.locator('[data-qa="first_name"]').fill('Ayesha')
    automationexcercise.locator('[data-qa="last_name"]').fill('sultan')
    automationexcercise.locator('[data-qa="company"]').fill('factor')
    automationexcercise.locator('[data-qa="address"]').fill('johar')
    automationexcercise.locator('[data-qa="state"]').fill('NT')

    # ✅ TIP: select_option with label= matches visible text
    automationexcercise.locator('#country').select_option(label='India')
    automationexcercise.locator('[data-qa="zipcode"]').fill('03045')
    automationexcercise.locator('[data-qa="mobile_number"]').fill('0304233232')
    automationexcercise.locator('[data-qa="city"]').fill('kara')
    automationexcercise.locator('[data-qa="create-account"]').click()

    print(automationexcercise.url)  # Verify account created page
    automationexcercise.wait_for_load_state('domcontentloaded')

    # Continue after account creation
    automationexcercise.get_by_role('link', name='Continue').click()
    automationexcercise.wait_for_load_state('domcontentloaded')

    # Logout
    automationexcercise.locator(['data-qa="continue-button"']).click
    automationexcercise.get_by_role('link', name='Logout').click()
    automationexcercise.wait_for_load_state('domcontentloaded')

    # Login with registered account
    login = context.new_page()
    login.goto('https://automationexercise.com/login')
    login.wait_for_load_state('domcontentloaded')
    login.locator('[data-qa="login-email"]').fill('aishaidu8@gmail.com')
    login.locator('[data-qa="login-password"]').fill('22January@9896')
    login.locator('[data-qa="login-button"]').click()
    print(login.url)  # Verify login success

    # ============================================================
    # Website: Guru99 Tours
    # URL: https://demo.guru99.com/test/newtours/register.php
    # Test: Register & Login
    # Date: 25-06-2026
    # Locators Used: name attribute, select_option
    # ============================================================
    demoguru = context.new_page()
    demoguru.goto('https://demo.guru99.com/test/newtours/register.php')

    # Fill registration form using name attributes
    demoguru.locator('[name="firstName"]').fill('Ayesa')
    demoguru.locator('[name="lastName"]').fill('Sultan')
    demoguru.locator('[name="phone"]').fill('03058855570')

    # ✅ TIP: Guru99 uses simple username — not email
    demoguru.locator('[name="userName"]').fill('aisha123')
    demoguru.locator('[name="address1"]').fill('johar')
    demoguru.locator('[name="city"]').fill('johar')
    demoguru.locator('[name="state"]').fill('sindh')
    demoguru.locator('[name="postalCode"]').fill('32344')

    # Select country from dropdown
    demoguru.locator('[name="country"]').select_option(value='PAKISTAN')
    demoguru.keyboard.press('Escape')

    demoguru.locator('[name="email"]').fill('aishaidu@gmail.com')
    demoguru.locator('[name="password"]').fill('22January@9896')
    demoguru.locator('[name="confirmPassword"]').fill('22January@9896')
    demoguru.locator('[name="submit"]').click()
    demoguru.wait_for_load_state('networkidle')

    # Login with mercury default credentials
    demoguru.get_by_role('link', name='sign-in').click()
    demoguru.locator('[name="userName"]').fill('mercury')
    demoguru.locator('[name="password"]').fill('mercury')
    demoguru.locator('[name="submit"]').click()
    demoguru.wait_for_load_state('domcontentloaded')
    print(demoguru.url)  # Verify login success URL

    # ============================================================
    # Website: ParaBank
    # URL: https://parabank.parasoft.com/parabank/register.htm
    # Test: Register & Login
    # Date: 25-06-2026
    # Locators Used: id with dots — use [id=""] not #id
    # ============================================================
    parabank = context.new_page()
    parabank.goto('https://parabank.parasoft.com/parabank/register.htm')

    # ✅ TIP: IDs with dots need [id=""] syntax not #id
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

    # ✅ TIP: After register, go to login page directly
    parabank.goto('https://parabank.parasoft.com/parabank/login.htm', timeout=60000)
    parabank.wait_for_load_state('domcontentloaded')

    # Login with registered credentials
    parabank.locator('[name="username"]').fill('aisrredhgy3')
    parabank.locator('[name="password"]').fill('22January@9896')
    parabank.locator('[value="Log In"]').click()
    parabank.wait_for_load_state('domcontentloaded')
    print(parabank.url)  # Should contain 'overview' if login successful

    # Logout
    parabank.get_by_role('link', name='Log Out').click()

    # ============================================================
    # Website: DemoBlaze
    # URL: https://www.demoblaze.com/
    # Test: Register & Login & Logout
    # Date: 25-06-2026
    # Locators Used: id, get_by_role, onclick attribute
    # ============================================================
    demoblaze = context.new_page()
    demoblaze.goto('https://www.demoblaze.com/')
    demoblaze.wait_for_load_state('domcontentloaded')

    # Open signup modal and register
    demoblaze.locator('#signin2').click()
    demoblaze.locator('#sign-username').fill('aiai=du8@gmail.com')
    demoblaze.locator('#sign-password').fill('22January@9896')
    demoblaze.get_by_role('button', name='Sign up').click()

    # Open login modal and login
    demoblaze.locator('#login2').click()
    demoblaze.locator('#loginusername').fill('aishaidu8@gmail.com')
    demoblaze.locator('#loginpassword').fill('22January@9896')
    demoblaze.get_by_role('button', name='Log in').click()
    demoblaze.wait_for_load_state('domcontentloaded')

    # ✅ TIP: Use onclick attribute for unique buttons
    demoblaze.locator('[onclick="logOut()"]').click()

    # ============================================================
    # Website: Naveen Automation Labs (OpenCart)
    # URL: https://naveenautomationlabs.com/opencart/
    # Test: Register & Login & Logout
    # Date: 25-06-2026
    # Locators Used: title, get_by_role, get_by_placeholder, id
    # ============================================================
    naveen = context.new_page()
    naveen.goto('https://naveenautomationlabs.com/opencart/')
    naveen.wait_for_load_state('domcontentloaded')

    # ✅ TIP: Dropdown needs click + wait_for_timeout
    naveen.locator('[title="My Account"]').click()
    naveen.wait_for_timeout(1000)  # Wait for dropdown animation
    naveen.get_by_role('link', name='Register').click()
    naveen.wait_for_load_state('domcontentloaded')

    # Fill registration form
    naveen.get_by_placeholder('First Name').fill('Ayesha')
    naveen.get_by_placeholder('Last Name').fill('Sultan')
    naveen.get_by_placeholder('E-Mail').fill('arfffdjggtt@gmail.com')
    naveen.get_by_placeholder('Telephone').fill('03058s855570')

    # ✅ TIP: When strict mode violation — use id directly
    naveen.locator('#input-password').fill('22January@9896')
    naveen.get_by_placeholder('Password Confirm').fill('22January@9896')

    # Radio button using name + value
    naveen.locator('input[name="newsletter"][value="0"]').click()

    # Checkbox using type + value
    naveen.locator('input[type="checkbox"][value="1"]').click()
    naveen.locator('input[type="submit"]').click()
    naveen.wait_for_load_state('domcontentloaded')
    naveen.get_by_role('link', name='Continue').click()

    # Logout via dropdown
    naveen.locator('[title="My Account"]').click()
    naveen.wait_for_timeout(1000)

    # ✅ TIP: When 2 same links — use parent locator first
    naveen.locator('#top-links').get_by_role('link', name='Logout').click()
    naveen.wait_for_load_state('domcontentloaded')

    naveen.get_by_role('link', name='Continue').click()
    naveen.wait_for_load_state('domcontentloaded')

    # Login in new page
    naveentwo = context.new_page()
    naveentwo.goto('https://naveenautomationlabs.com/opencart/index.php?route=account/login')
    naveentwo.wait_for_load_state('networkidle')
    naveentwo.wait_for_timeout(2000)
    naveentwo.get_by_placeholder('E-Mail Address').fill('aishaidu8@gmail.com')
    naveentwo.get_by_placeholder('Password').fill('22January@9896')
    naveentwo.locator('input[value="Login"]').click()

    # ============================================================
    # End of Automation Suite
    # ============================================================
    time.sleep(10)