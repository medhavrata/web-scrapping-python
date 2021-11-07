import webbrowser

listOfWebsites = ['https://www.google.com', 'https://www.next.co.uk/', 'https://www.yahoo.com']

for website in listOfWebsites:
    webbrowser.open(website)

if __name__ == '__main__':
    main()