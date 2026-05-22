class Student {
  int maxDays;
  String name;
  int rollno;
  bool isSuspended;
  int leaveTaken;

  //Constructor
  Student({
    required this.name,
    required this.rollno,
    required this.isSuspended,
    required this.leaveTaken,
    required this.maxDays,
  });

  String checkLeave(int days) {
    if (!isSuspended && leaveTaken + days <= maxDays) {
      leaveTaken += days;
      return "Your leave is permitted!";
    } else if (isSuspended) {
      return "Your are Suspended";
    } else {
      return "Maximum leave is $maxDays Days!";
    }
  }
}

void main() {
  List<Student> allStudents = [
    Student(
      name: "Alex",
      rollno: 101,
      isSuspended: false,
      leaveTaken: 5,
      maxDays: 15,
    ),
    Student(
      name: "Sam",
      rollno: 102,
      isSuspended: true,
      leaveTaken: 5,
      maxDays: 15,
    ),
    Student(
      name: "Mia",
      rollno: 103,
      isSuspended: false,
      leaveTaken: 10,
      maxDays: 15,
    ),
    Student(
      name: "Mushil NR",
      rollno: 104,
      isSuspended: false,
      leaveTaken: 5,
      maxDays: 15,
    ),
  ];

  int days = 2;

  // The Syntax
  for (Student currentStudent in allStudents) {
    // logic goes here
    print("${currentStudent.name}: ${currentStudent.checkLeave(days)}");
  }
}
