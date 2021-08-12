CONTENT_TYPE = "application/json"


def getuuid():
    uuid = -1
    return uuid


def get_uniq_bankid():
    uid = 'bnk_' + getuuid()
    return uid


def get_uniq_customerid():
    uid = 'cst_' + getuuid()
    return uid


def get_uniq_loanid():
    uid = 'ln_' + getuuid()
    return uid
