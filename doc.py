def examble(name):
    ext=name.split('.')[-1]
    if(ext=="pdf"):
        return"pdf*"
    else:
        return ext
print(examble("document.pdf"))
print(examble("image.jpg"))