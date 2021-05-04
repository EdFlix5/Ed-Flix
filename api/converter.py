def longToSizeString(longVal):
    if longVal >= 1073741824 :
        return str(round(longVal/1073741824,2))+"GB"
    elif longVal >= 1048576:
        return str(round(longVal/1048576,2)) + "MB"
    elif longVal >= 1024:
        return str(round(longVal/1024,2))+"KB"
    else:
        return str(longVal)+"B"