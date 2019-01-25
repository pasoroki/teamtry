def pprint(obj, title: str="", all: bool=False):
    print("\n {}:".format(title))
    for i in dir(obj):
        if not all and i.startswith("_"): continue
        try:
            print("{}   - {:30} : {}".format(title, i, getattr(obj, i)))
        except Exception as err:
            print("{}   - {:30} : ????? {}".format(title, i, err))
