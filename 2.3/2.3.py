from xml.dom import minidom
doc = minidom.parse("sample.xml")
company_name = doc.getElementsByTagName("name")[0].firstChild.data
print(f"Tên công ty: {company_name}")

staff_list = doc.getElementsByTagName("staff")

for staff in staff_list:
    staff_id = staff.getAttribute("id")
    name = staff.getElementsByTagName("name")[0].firstChild.data
    salary = staff.getElementsByTagName("salary")[0].firstChild.data
    print(f"ID: {staff_id}, Tên: {name}, Lương: {salary}")
