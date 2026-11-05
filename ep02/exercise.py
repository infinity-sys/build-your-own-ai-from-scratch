text = open("../data/proverbs.txt", encoding="utf-8").read()
mine = "the camel does not see its own hump\njust like a fish needs water\na quiet tongue keeps a quick friend\n"
for t in [text, text + mine]:
    print(len(t.splitlines()), len(t), len(set(t)))
