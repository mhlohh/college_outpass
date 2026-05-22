//Control statement

void main() {
  int requestedDays = 1;
  int maxAllowedDays = 2;
  bool isSuspended = false;
  if (isSuspended == true) {
    print("You are Suspended");
  } else if (requestedDays <= maxAllowedDays) {
    print("The leave allowed");
  } else {
    print("The maximum allowed leave is $maxAllowedDays!");
  }
}
