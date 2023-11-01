import os 

# with open("syn_labels.txt","r",encoding="utf-8") as f:
#     lines = f.readlines()

# with open("synthe_labels.txt","w",encoding="utf-8") as w:
#     for line in lines:
#         elements = line.split(' ')
#         image_path = elements[0]
#         label =""
#         for e in elements[1:]:
#             label = label+e+" "
#         label = label.strip()
#         new_image_path = "synthetic_image/"+image_path
#         new_line = new_image_path+"\t"+label
#         w.writelines(new_line+"\n")

with open("synthe_labels.txt","r",encoding="utf-8") as f:
    lines = f.readlines()
    print(len(lines))