// See https://aka.ms/new-console-template for more information
using Let_code;

Console.WriteLine("Hello, World!");

int[] numbers_Ordered = [2, 7, 11, 15];
int[] numbers_unordered = [11, 7, 4, 2, 15];
int target = 9;

// TwoSum.FindTwoSum_HashMap(numbers_unordered, target);
// TwoSum.FindTwoSum_Ordered_TwoPointers(numbers_Ordered, target);

int[][] matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]];
// RotateImage.Rotate(matrix);

string[] strs = ["eat", "tea", "tan", "ate", "nat", "bat"];
// GroupAnagrams.Group(strs);

int[] height = [3, 3, 3, 0, 2, 4, 1, 2];
// TrappingRainWater.Trap(height);

// Misc.Fibonacci(10);
// for (int i = 0; i < 10; i++)
// {
//     Console.Write(Misc.FibonacciRecursive(i) + " ");
// }

// Console.WriteLine(Misc.IsPalindrome("aerea") ? "É palíndromo" : "Não é palíndromo");
// Console.WriteLine(Misc.IsPalindrome("hello") ? "É palíndromo" : "Não é palíndromo");
// Console.WriteLine(Misc.IsPalindrome("soldadlos") ? "É palíndromo" : "Não é palíndromo");

// Misc.ReverseString("Hello, World!");

// Misc.FindDuplicate([1, 3, 4, 2, 2]);
// Misc.FindDuplicate([1, 3, 4, 2, 5]);

Misc.FindMax([1, 3, 4, 2, 5]);
