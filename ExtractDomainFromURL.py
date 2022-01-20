from lib2to3.pygram import pattern_symbols
import re

def domain_name(url):
    """ Write a function that when given a URL as a string, 
    parses out just the domain name and returns it as a string.
    domain_name("http://github.com/carbonfive/raygun") == "github" 
    domain_name("http://www.zombie-bites.com") == "zombie-bites"
    domain_name("https://www.cnet.com") == "cnet"
    """
    patron='(https*://)?(www.)?([\w-]+.)'
    name=re.findall(patron,url)
    _,_,res = (name[0])
    domain=res.split('.')
    return domain[0]

print(domain_name("www.xakep.ru"))

