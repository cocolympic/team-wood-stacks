import xml.etree.ElementTree as ET

root = ET.Element("root")
child = ET.SubElement(root, "child")
child.text = "Hello, World!"

print(ET.tostring(root, encoding="utf-8").decode("utf-8"))