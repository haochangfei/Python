# -*- coding: cp936 -*-
person = {"male":{"name":"Shawn"}, "female":{"name":"Betty","age":23},"children":{"name":{"first_name":"��", "last_name":{"old":"����","now":"��"}},"age":4}}

def all_dict (dict_a):
    if isinstance(dict_a,dict):#������������Ƿ�Ϊ�ֵ�
        for i in range(len(dict_a)):
            a_key = dict_a.keys()[i]
            a_value = dict_a[a_key] 
            if isinstance(a_value,dict):
                print a_key + ":"
            else:
                print"  %s : %s" %(a_key,a_value)
            all_dict(a_value)
all_dict(person)
