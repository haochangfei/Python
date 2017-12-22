# -*- coding: cp936 -*-
person = {"male":{"name":"Shawn"}, "female":{"name":"Betty","age":23},"children":{"name":{"first_name":"李", "last_name":{"old":"明明","now":"铭"}},"age":4}}

def all_dict (dict_a):
    if isinstance(dict_a,dict):#检查数据类型是否为字典
        for i in range(len(dict_a)):
            a_key = dict_a.keys()[i]
            a_value = dict_a[a_key] 
            if isinstance(a_value,dict):
                print a_key + ":"
            else:
                print"  %s : %s" %(a_key,a_value)
            all_dict(a_value)
all_dict(person)
