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
                if (numDict.ContainsKey(complement))
                {
                    Console.WriteLine($"Key = {complement}, index(value) = {numDict[complement]}. Current index = {i}, current value = {numbers[i]}");
                    return;
                }
                numDict[numbers[i]] = i;
            }

            Console.WriteLine("No two sum solution");
        }

        public static void FindTwoSum_Ordered_TwoPointers(int[] numbers, int target)
        {
            int leftPointer = 0;
            int rightPointer = numbers.Length - 1;
            
            while (leftPointer < rightPointer)
            {
                int sum = numbers[leftPointer] + numbers[rightPointer];

                if(sum == target){
                    Console.WriteLine($"Index i = {leftPointer} and j = {rightPointer}");
                    break;
                }
                else if(sum < target){
                    leftPointer++;
                }else{
                    rightPointer--;
                }
            }
        }
    }
}