text = "WE, THE PEOPLE OF INDIA, having solemnly resolved to constitute India into a "
text = text + "SOVEREIGN, SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC and to secure to all "
text = text + "its citizens"
_index1 = text.index(" having solemnly")
_index2 = text.index(" SOCIALIST")
_index3 = text.index(" and to")

print(text[0: _index1])
print("\t" + text[_index1: _index2] + "!")
print("\t\t" + text[_index2: _index3])
print("\t\t " + text[_index3: ] + ":")