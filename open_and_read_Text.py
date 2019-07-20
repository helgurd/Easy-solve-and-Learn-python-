def read_text():
    quotes=open('quotes.txt')
    contents_of_file=quotes.read()
    print(contents_of_file)
    quotes.close()
print (read_text())
    