import graphspace_utils
import json_utils

def readData(filename):
    node_set = set()
    edge_ls = []
    edge_type_dict = {}
    with open(filename, 'r') as f:
        for line in f:
            data = line.strip('\n').split('\t')
            node1 = data[0]
            node2 = data[1]
            node_set.add(node1)
            node_set.add(node2)
            if node1 != node2:
                edge = (data[0], data[1])
                edge_type_dict[edge] = data[2]
                edge_ls.append(edge)

    return set_to_list(node_set), edge_ls, edge_type_dict


def get_int_types(etd):
    int_types = set()
    for k in etd:
        int_types.add(etd[k])
    return int_types


def set_to_list(s):
    ls = []
    for item in s:
        ls.append(item)
    return ls


def getEdgeAttributes(edges,edge_type_dict=None):
    attrs = {}
    for e in edges:
        source = e[0]
        target = e[1]
        if source not in attrs:
            attrs[source] = {}
        attrs[source][target] = {}
        attrs[source][target]['width'] = 2
        attrs[source][target]['target_arrow_shape'] = 'triangle'
        attrs[source][target]['target_arrow_fill'] = 'filled'
        attrs[source][target]['target_arrow_color'] = 'black'
        if edge_type_dict != None:
            attrs[source][target]['popup'] = '<b>Edge Type:</b> ' + edge_type_dict[e]
    return attrs




def main():
    nodes, edges, edge_dict = readData('EGFR1-reachable.txt')
    edgeAttrs = getEdgeAttributes(edges,edge_dict)
    print(get_int_types(edge_dict))

    data = json_utils.make_json_data(nodes,edges,None,edgeAttrs,'Lab 3','Desc.',['Tag'])
    json_utils.write_json(data,'lab3StrangeError.json')
    graphspace_utils.postGraph('lab3-2-1','lab3.json','franzni@reed.edu','bio331')

    



if __name__ == '__main__':
    main()
