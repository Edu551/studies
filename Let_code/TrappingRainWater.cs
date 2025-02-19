namespace Let_code
{
    public class TrappingRainWater
    {
        public static void Trap(int[] height)
        {
            int arrayLength = height.Length;
            int[] water = new int[arrayLength];

            int highestElevation = 0;

            for (int i = 0; i < arrayLength; i++)
            {
                if (height[i] > highestElevation)
                {
                    highestElevation = height[i];
                }

                if (height[i] < highestElevation)
                {
                    water[i] += highestElevation - height[i];
                }
            }

            highestElevation = 0;

            for (int i = arrayLength - 1; i >= 0; i--)
            {
                if (height[i] > highestElevation)
                {
                    highestElevation = height[i];
                }

                int diff = highestElevation - height[i];

                if (diff < water[i])
                {
                    water[i] = diff;
                }
            }

            Console.WriteLine(water.Sum());
        }

        public static void BestSolution(int[] height) {

            int left = 0;
            int right = height.Length-1;
            int leftMax = height[left];
            int rightMax = height[right];        

            int result = 0;

            while(left < right) {
                if(leftMax < rightMax) {
                    left++;
                    leftMax = Math.Max(leftMax, height[left]);
                    result += leftMax - height[left];
                }
                else {
                    right--;
                    rightMax = Math.Max(rightMax, height[right]);
                    result += rightMax - height[right];
                }
            }

            Console.WriteLine(result);

        }
    }
}