
s=input("Enter the course code (java or pyt): ")
java_course=["Jack","John","Jill","Joe"]
python_course=["Jakes","John","Eric","Jill"]

if "pyt" in s.lower():
    print("strudents enrolled in python course : " ,len(python_course))
    print("name of strudents erolled in python course : " ,str(python_course))
if "java" in s.lower():
    print("strudents enrolled in java course : " ,len(java_course))
    print("name of strudents erolled in java course : " ,str(java_course))
