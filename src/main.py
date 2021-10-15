import webbrowser


def string_shown(_url):
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(_url)


if __name__ == '__main__':
    url = 'https://the-internet.herokuapp.com/context_menu'
    # string_shown(url)

