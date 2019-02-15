import re
def clear_url(target):
    return re.sub('.*www\.','',target,1).split('/')[0].strip()


print clear_url('https://www.esecurity.ir')