// See https://aka.ms/new-console-template for more information
using Let_code;

Console.WriteLine("Hello, World!");

int[] numbers = [2, 7, 11, 15];
int[] numbers_unordered = [11, 7, 4, 2, 15];
int target = 9;

TwoSum.FindTwoSum_HashMap(numbers_unordered, target);
TwoSum.FindTwoSum_TwoPointers(numbers, target);