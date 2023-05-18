from selenium import webdriver


def test_chrome():
    capabilities = {
        "browserName": "chrome",
        "version": "80.0_VNC",
        "enableVNC": True,
        "enableVideo": False
    }
    options = webdriver.ChromeOptions()
    options.add_argument("--user-data-dir=C:\\Users\\Administrator\\AppData\\Local\\Google\\Chrome\\User Data")
    options.add_argument('--profile-directory=Default')
    chrome = webdriver.Remote(command_executor='http://localhost:8080/wd/hub',
                              desired_capabilities=capabilities, options=options)
    chrome.get('https://www.google.com')
    print('chrome', chrome.title)
    chrome.quit()


def test_chromme():
    capabilities = {
        "browserName": "firefox",
        "browserVersion": "112.0",
        "selenoid:options": {
            "enableVideo": False
        }
    }
    chrome = webdriver.Remote(
        command_executor="http://localhost:4444/wd/hub",
        desired_capabilities=capabilities)
    chrome.get('https://www.google.com')
    print('chrome', chrome.title)
    chrome.quit()


if __name__ == "__main__":
    test_chromme()
