student_bio = {"name": "Shahzaib Noor", "age": 24, "city": "Karachi"};
#
print();
print("Dictionary items")
for item in student_bio.items():
    print(item)
#
print();
print("Getting dictionary items in tuples");
for (key, val) in student_bio.items():
    print("{} : {}".format(key,val));
