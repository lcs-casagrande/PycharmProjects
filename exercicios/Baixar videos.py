import webbrowser
url = input('Enter your youtube URL:')
url = url[:12]+'ss'+url[12:]
webbrowser.open(url)