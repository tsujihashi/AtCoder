using System;

namespace J
{
    class Program
    {
        static void Main(string[] args)
        {
            string[] str = Console.ReadLine().Split(' ');
            int N = int.Parse(str[0]);
            int M = int.Parse(str[1]);

            int[] children = new int[N];
            string[]sushi = Console.ReadLine().Split(' ');
            int[] result = new int[M];

            for(int i = 0; i < M; i++)
            {
                int point = int.Parse(sushi[i]);
                for(int j = 0; j < N; j++)
                {
                    if (point > children[j])
                    {
                        children[j] = point;
                        result[i] = j + 1;
                        break;
                    }
                    else if (j == N - 1)
                    {
                        result[i] = -1;
                        break;
                    }
                }
            }

            for(int i = 0; i < M; i++)
            {
                Console.WriteLine(result[i]);
            }

        }
    }
    
}
