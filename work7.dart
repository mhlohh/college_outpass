// Inheritance

class Student {
  String name;
  int rollno;
  bool isSuspended;
  int leaveTaken;
  int maxDays;

  Student({
    required this.name,
    required this.rollno,
    required this.isSuspended,
    required this.leaveTaken,
    required this.maxDays,
  });

  String checkLeave(int days) {
    if (!isSuspended && leaveTaken + days <= maxDays) {
      return "Your Leave is Permitted";
    } else if (isSuspended) {
      return "You are Suspended";
    } else {
      return "Maximum days of leave is $maxDays!";
    }
  }
}

class Department {
  String department;
  List<Student> students;
  Department({required this.department, required this.students});
}

void main() {
  List<Department> myDepartment = [
    Department(
      department: "Computer Science",
      students: [
        Student(
          name: "Mushil NR",
          rollno: 1,
          isSuspended: false,
          leaveTaken: 2,
          maxDays: 5,
        ),
        Student(
          name: "Abhishke",
          rollno: 2,
          isSuspended: false,
          leaveTaken: 4,
          maxDays: 5,
        ),
        Student(
          name: "Yohan",
          rollno: 3,
          isSuspended: true,
          leaveTaken: 3,
          maxDays: 5,
        ),
        Student(
          name: "Shiya",
          rollno: 4,
          isSuspended: false,
          leaveTaken: 4,
          maxDays: 5,
        ),
        Student(
          name: "Ardra",
          rollno: 5,
          isSuspended: true,
          leaveTaken: 2,
          maxDays: 5,
        ),
      ],
    ),
    Department(
      department: "Artitficial Intelligence",
      students: [
        Student(
          name: "Mushil NR",
          rollno: 1,
          isSuspended: false,
          leaveTaken: 2,
          maxDays: 5,
        ),
        Student(
          name: "Abhishke",
          rollno: 2,
          isSuspended: false,
          leaveTaken: 4,
          maxDays: 5,
        ),
        Student(
          name: "Yohan",
          rollno: 3,
          isSuspended: true,
          leaveTaken: 3,
          maxDays: 5,
        ),
        Student(
          name: "Shiya",
          rollno: 4,
          isSuspended: false,
          leaveTaken: 4,
          maxDays: 5,
        ),
        Student(
          name: "Ardra",
          rollno: 5,
          isSuspended: true,
          leaveTaken: 2,
          maxDays: 5,
        ),
      ],
    ),
  ];

  for (Department currentDepartment in myDepartment) {
    for (Student currentStudent in currentDepartment.students) {
      print("____________Status____________");
      print("");
      print("Department Name: ${currentDepartment.department} ");
      print("👤Student Name: ${currentStudent.name}");
      print("rollno: ${currentStudent.rollno}");
      print("Is Suspended: ${currentStudent.isSuspended}");
      print("Total Leave Taken: ${currentStudent.leaveTaken}");
      print("Max days: ${currentStudent.maxDays} ");
      print("Status: ${currentStudent.checkLeave(2)}");
      print("");
    }
  }
}
