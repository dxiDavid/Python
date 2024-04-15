def find_needle(haystack):
    return f'found the needle at position {haystack.index("needle")}'

arr = ["hay", "junk", "hay", "hay", "moreJunk", "needle", "randomJunk"]
find_needle(arr)
