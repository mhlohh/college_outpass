void main() {
  int firstValue = 25;
  print(firstValue);
  firstValue += 75;
  print(firstValue);
  String greeting = 'Hello, World';
  print(greeting);
  greeting = '${greeting}' + ' YOO';
  print(greeting);
  // Dynamic can change the value type ignoring the compile time error
  dynamic greet = 'hello, world';
  print(greet);
  greet = 1;
  print(greet);
  //variables
  // var / final / const variableName = value;
  //var
  //var can assigned to any type of data and value can be changed
  var someValue1 = '10';
  print(someValue1);
  //final
  // final means final value this doesnt change this is fixed but it is run time constant it can be set on run time
  final someValue2 = DateTime.now(); // Works: Value determined at runtime
  print(someValue2);
  //const
  //const means constant value that is compile time that why it shows error
  const someValue3 = 106; // Works: Known at compile-time
  print(
    someValue3,
  ); // fixedNumbers.add(4); // ERROR: Const collections are deeply immutable

  print("----------");

  someValue1 = '10001';
  print(someValue2);

  //Optional Variable
  // String/int/bool and null

  String? someValue4;

  print(someValue4);

  someValue4 = '354 Heloo World';

  print(someValue4.length);

  someValue4 = null;

  // If it shows error on length use ! before the object '.'
  //On null value we cannot use length\
  //No compile time error but runtime error

  print(someValue4?.length);

  // If it is null print out null if it is not null print the value
  print(someValue4?.length);
}
