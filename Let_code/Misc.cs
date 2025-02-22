namespace Let_code
{
    public class Misc
    {
        public static void Fibonacci(int n)
        {
            long a = 0, b = 1, temp;

            for (int i = 0; i < n; i++)
            {
                Console.Write(a + " ");
                temp = a + b;
                a = b;
                b = temp;
            }
        }

        public static long FibonacciRecursive(int n)
        {
            if (n <= 1) return n;
            return FibonacciRecursive(n - 1) + FibonacciRecursive(n - 2);
        }

        public static bool IsPalindrome(string str)
        {
            int left = 0, right = str.Length - 1;
            while (left < right)
            {
                if (str[left] != str[right])
                {
                    return false;
                }
                left++;
                right--;
            }
            return true;
        }

        public static void ReverseString(string str)
        {
            char[] charArray = str.ToCharArray();
            Array.Reverse(charArray);
            Console.WriteLine(new string(charArray));
        }

        public static void FindDuplicate(int[] nums)
        {
            Array.Sort(nums);
            for (int i = 0; i < nums.Length - 1; i++)
            {
                if (nums[i] == nums[i + 1])
                {
                    Console.WriteLine(nums[i]);
                    return;
                }
            }

            Console.WriteLine("Números não repetidos");
        }

        public static void FindMax(int[] nums)
        {
            int max = nums[0];
            foreach (int num in nums)
            {
                if (num > max)
                {
                    max = num;
                }
            }
            Console.WriteLine(max);
        }
    }
}