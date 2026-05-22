class Student {
  String name;
  int rollno;
  bool isSuspended;
  //Constructor
  Student(this.name, this.rollno, this.isSuspended);

  String checkLeave(int days) {
    int maxDays = 5;
    if (days <= maxDays && !isSuspended) {
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
    Student("Alex", 101, false),
    Student("Sam", 102, true),
    Student("Mia", 103, false),
    Student("Mushil NR", 104, false),
  ];
  print(allStudents[0].checkLeave(2));
  print(allStudents[1].checkLeave(3));
  print(allStudents[2].checkLeave(1));
  print(allStudents[3].checkLeave(7));

  // The Syntax
  for (Student currentStudent in allStudents) {
    // logic goes here
    print(currentStudent.name);
  }
}
