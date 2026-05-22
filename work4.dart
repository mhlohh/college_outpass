class Student {
  // 1. Properties (Variables)

  String name;

  // add the others here...

  int rollno;

  bool isSuspended;

  // 2. The Constructor

  // This strange syntax (this.name) tells Dart:

  // "Take the name given when building the object, and save it to the variable 'name' above."

  Student(this.name, this.rollno, this.isSuspended /* add others here */);

  String chechLeave(int day) {
    int maxDay = 5;

    if (day <= maxDay && !isSuspended) {
      return "Your leave is permitted!";
    } else if (isSuspended) {
      return "You are Suspended";
    } else {
      return "Max leave is $maxDay Days!";
    }
  }
}

void main() {
  Student firstStudent = Student("Alex", 101, false);

  Student secondStudent = Student("Sam", 102, true);

  Student thridStudent = Student("Mia", 103, false);

  Student fourStudent = Student("Mushil NR", 12, false);

  print(firstStudent.chechLeave(1));

  print(secondStudent.chechLeave(5));

  print(thridStudent.chechLeave(1));

  print(fourStudent.chechLeave(7));
}
