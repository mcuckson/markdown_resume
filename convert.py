import markdown

# markdown.markdownFromFile(
    # input='content/index.md',
    # output='public/index.html',
    # encoding='utf8',
# )

with open('content/index.md', 'r') as f:
    text = f.read()
    html_fragment = markdown.markdown(text)
    
with open('docs/index.html', 'w') as f:
    html = '''
    <html>
    <head>
    <link rel="stylesheet" href="default.css"/>
    <link rel="shortcut icon" href="favicon.ico" />
    <title>Mark Cuckson</title>
    </head>
    <body>{}</body>
    </html>
    '''.format(html_fragment)
    f.write(html)
