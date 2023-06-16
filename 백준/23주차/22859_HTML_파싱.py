import re

html = input()
html = html.replace("<main>", '').replace("</main>", '')

divs = html.split("</div>")
for div in divs:
    if div == '':
        continue
    s = div.find('"') + 1
    e = div.find('>')
    print("title :", div[s:e-1])
    div = div.replace(div[0:e+1], '')
    ps = div.split("</p>")
    for p in ps:
        if p == '':
            continue
        p = re.sub("<(.*?)>", '', p)
        p = ' '.join(p.split())
        print(p)
