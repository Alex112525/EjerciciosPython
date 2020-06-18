import re


def validateEmail(email):
    pattern = "[a-zA-Z0-9_]*@(python\.)?padts(\.com)?\.mx$"
    if re.match(pattern, email):
        return True
    else:
        return False


def validateNum(num):
    pattern = "^\(?[0-9]{2}\)?\ ?[0-9]{4}[\ -]?[0-9]{4}$"
    pattern2 = "^\(?[0-9]{3}\)?\ ?[0-9]{3}[\ -]?[0-9]{4}$"
    if re.match(pattern, num) or re.match(pattern2, num):
        return True
    else:
        return False


def validateRFC(rfc):
    pattern = "^[A-Z]{4}[0-9]{6}[A-Z0-9]{3}$"
    if re.match(pattern, rfc):
        return True
    else:
        return False


def validateCURP(curp):
    pattern = "^[A-Z]{4}[0-9]{6}[MH]{1}[A-Z]{5}[0-9]{2}$"
    if re.match(pattern, curp):
        return True
    else:
        return False


if __name__ == "__main__":
    x = validateEmail("Juan_12@python.padts.mx")
    n = validateNum("(33) 2218-2992")
    n2 = validateNum("331 812-2392")
    r = validateRFC("MELM8305281H0")
    c = validateCURP("AAAC961026HJCNCR09")
    print(c)
