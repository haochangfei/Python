# -*- coding: cp936 -*-
nodes = ('A', 'B', 'C', 'D', 'E', 'F', 'G')
distances = {
    'B': {'A': 5, 'D': 1, 'G': 2},
    'A': {'B': 5, 'D': 3, 'E': 12, 'F' :5},
    'D': {'B': 1, 'G': 1, 'E': 1, 'A': 3},
    'G': {'B': 2, 'D': 1, 'C': 2},
    'C': {'G': 2, 'E': 1, 'F': 16},
    'E': {'A': 12, 'D': 1, 'C': 1, 'F': 2},
    'F': {'A': 5, 'E': 2, 'C': 16}}

unvisited = {node: None for node in nodes} #��None��Ϊ�����ʹ��
visited = {}#������¼�Ѿ��ɳڹ�������
current = 'B' #Ҫ��B�㵽������ľ���
currentDistance = 0
unvisited[current] = currentDistance#B��B�ľ����Ϊ0

while True:
    for neighbour, distance in distances[current].items():
        if neighbour not in unvisited: continue#�����ʹ��ˣ���������ѭ��
        newDistance = currentDistance + distance#�µľ���
        if unvisited[neighbour] is None or unvisited[neighbour] > newDistance:#���������֮��ľ���֮ǰ�����������¾���С��ԭ���ľ���
            unvisited[neighbour] = newDistance#���¾���
    visited[current] = currentDistance#������Ѿ��ɳڹ�����¼
    del unvisited[current]#��δ���ʹ����ֵ��н������ɾ��
    if not unvisited: break#������е㶼�ɳڹ��������˴�ѭ��
    candidates = [node for node in unvisited.items() if node[1]]#�ҳ�Ŀǰ������Щ��δ�ɳڹ�
    current, currentDistance = sorted(candidates, key = lambda x: x[1])[0]#�ҳ�Ŀǰ���������ɳڵĵ�
