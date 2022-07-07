import json

annotation_file = "OVAD_Benchmark/ovad/ovad1200.json"
attribute_file = "OVAD_Benchmark/ovad/attributes_data.json"

att_dict = {"name": "OVA", "id": "0", "children": []}

data_file = json.load(open(annotation_file, "r"))

attr2idx = {}
attr_type = {}
attr_parent_type = {}
for att in data_file["attributes"]:
    attr2idx[att["name"]] = att["id"]

    if att["type"] not in attr_type.keys():
        attr_type[att["type"]] = set()
    attr_type[att["type"]].add(att["name"])

    if att["parent_type"] not in attr_parent_type.keys():
        attr_parent_type[att["parent_type"]] = set()
    attr_parent_type[att["parent_type"]].add(att["type"])

for att_type in attr_parent_type.values():
    attr_parent_type_name = " / ".join(att_type)
    attr_parent_type_id = str(len(att_dict["children"]) + 1)
    children = []
    att_name_set = set()

    for parent_type in att_type:
        att_list = attr_type[parent_type]
        for att in att_list:
            att_name = att.split(":")[-1]
            if att_name not in att_name_set:
                att_name_set.add(att_name)
                children.append(
                    {
                        "name": "/".join(att_name.split("/")[:3]),
                        "id": attr_parent_type_id + "_" + str(len(att_name_set)),
                    }
                )

    attr_parent_type_dict = {
        "name": attr_parent_type_name,
        "id": attr_parent_type_id,
        "children": children,
    }

    att_dict["children"].append(attr_parent_type_dict)

import ipdb

ipdb.set_trace()
