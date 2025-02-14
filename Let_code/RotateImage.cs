namespace Let_code
{
    public class RotateImage
    {
        public static void Rotate(int[][] matrix)
        {
            /* 
                ⬇
                1 2 3
                4 5 6
                7 8 9
            */
            int left = 0;

            /* 
                    ⬇
                1 2 3 
                4 5 6
                7 8 9
            */
            int right = matrix.Length - 1;

            while(left < right)
            {
                for(int i = 0; i < right - left; i++)
                {
                    int top = left;
                    int bottom = right;

                    // Armazena a variável que irá sair primeiro, neste caso o "1"
                    int topLeft = matrix[top][left + i];

                    matrix[top][left + i] = matrix[bottom - i][left];
                    matrix[bottom - i][left] = matrix[bottom][right - i];
                    matrix[bottom][right - i] = matrix[top + i][right];
                    matrix[top + i][right] = topLeft;
                }

                // Movemos para a próxima camada
                right--;
                left++;
            }

            foreach (var item in matrix)
            {
                foreach (var i in item)
                {
                    Console.Write(i + " ");
                }
                Console.WriteLine();
            }
        }
    }
}