import sys
class IdotError(Exception):pass
def parse(code):
  code = code.split('i.')
  for i in code:
    f = i.split('>')[0].strip()
    a = i.split('>')[1].split(",")
    if f == "error":
      raise IdotError()
    elif f == "yoda":
      print("idot")
    elif f == "print":
      for i in a: print(i.strip())
    else:
      raise IdotError("specify a real function idot")
def r(file):
  parse(open(file).read())
r(sys.argv[1])