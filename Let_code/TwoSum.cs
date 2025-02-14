namespace Let_code
{
    public class TwoSum
    {
        public static void FindTwoSum_HashMap(int[] numbers, int target)
        {
            Dictionary<int, int> numDict = [];

            for (int i = 0; i < numbers.Length; i++)
            {
                int complement = target - numbers[i];
                if (numDict.TryGetValue(complement, out int value))
                {
                    Console.WriteLine($"Key = {complement}, index(value) = {value}. Current index = {i}, current value = {numbers[i]}");
                    return;
                }
                numDict[numbers[i]] = i;
            }

            Console.WriteLine("No two sum solution");
        }

        public static void FindTwoSum_TwoPointers(int[] numbers, int target)
        {
            int i = 0;
            int j = numbers.Length - 1;

            while (i < j)
            {
                int sum = numbers[i] + numbers[j];

                if(sum == target){
                    Console.WriteLine($"Index i = {i} and j = {j}");
                    break;
                }
                else if(sum < target){
                    i++;
                }else{
                    j--;
                }
            }
        }
    }
}