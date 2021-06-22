using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace A
{
    class Program
    {
        static void Main(string[] args)
        {
            int N = int.Parse(Console.ReadLine());
            string[] str = Console.ReadLine().Split(' ');
            int[] W = new int[N];
            for(int i = 0; i < N; i++)
            {
                W[i] = int.Parse(str[i]);
            }

            int min = int.MaxValue;
            int sum = W.Sum();

            for(int i = 1; i < N; i++)
            {
                //int[] a = new int[i];
                //int[] b = new int[N - i];
                
                int asum = 0;
                int bsum = 0;

                for (int j = 0; j < i; j++)
                {
                    asum += W[j];
                }

                bsum = sum - asum;

                int score = Math.Abs(asum - bsum);
                if (min > score)
                {
                    min = score;
                }
                else
                {
                    break;
                }
            }

            Console.Write(min);
        }
    }
}
