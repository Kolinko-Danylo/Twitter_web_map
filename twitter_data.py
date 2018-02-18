import twitter1
import twitter2

param_dict = {}


def recursion_twi(dic):
    """
    dict -> None
    Recursive processing of python dict from json file and rewriting
    into param_dict.
    """
    global param_dict
    for i in dic:
        if type(dic[i]) == dict:
            recursion_twi(dic[i])
        elif dic[i] and i not in param_dict:
            param_dict[i] = dic[i]


def account(data_str):
    """
    list or dict -> dict
    Return rewritten dict with all user key-information.
    """
    global param_dict
    param_dict.clear()
    lst = twitter1.twitter_info(data_str)
    lst.append(twitter2.twitter_info_prof(data_str))
    for i in lst:
        recursion_twi(i)
    return param_dict
