import markdown

# markdown.markdownFromFile(
    # input='content/index.md',
    # output='public/index.html',
    # encoding='utf8',
# )

with open('content/index.md', 'r') as f:
    text = f.read()
    html_fragment = markdown.markdown(text)
    
with open('public/index.html', 'w') as f:
    html = '''
    <html>
    <head>
    <link rel="stylesheet" href="default.css"/>
    </head>
    <body>{}</body>
    </html>
    '''.format(html_fragment)
    f.write(html)
