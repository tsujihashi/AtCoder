using System;

namespace C
{
    class Program
    {
        static void Main(string[] args)
        {
            string[] str = Console.ReadLine().Split(' ');
            int A = int.Parse(str[0]);
            int R = int.Parse(str[1]);
            int N = int.Parse(str[2]);

            ulong value = (ulong)A;
            long limit = (long)Math.Pow(10,9);

            //value *= (int)Math.Pow(R, N - 1);
            for (int i = 1; i < N; i++)
            {
                value *= (ulong)R;
            }
            
            if (value > (ulong)limit)
            {
                Console.WriteLine("large");
            }
            else
            {
                Console.WriteLine(value);
            }
        }
    }
}
