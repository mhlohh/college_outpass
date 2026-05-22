//user defined function

String checkLeave(int day, bool isSuspended) {
  int maxDay = 5;
  if (!isSuspended && day <= maxDay) {
    return "Your leave is premitted!";
  } else if (isSuspended) {
    return "You are Suspended";
  } else {
    return "Max Leave is $maxDay!";
  }
}

void main() {
  print(checkLeave(1, false));
  print(checkLeave(5, false));
  print(checkLeave(1, true));
  print(checkLeave(7, false));
}
