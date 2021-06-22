using System;

namespace D
{
    class Program
    {
        static void Main(string[] args)
        {
            int N = int.Parse(Console.ReadLine());
            string[] s = new string[5];
            for(int i = 0; i < 5; i++)
            {
                s[i] = Console.ReadLine();
            }

            string[,] num = new string[10, 5]
            { { "###.", "#.#.", "#.#.", "#.#.", "###." },//0
            { ".#..", "##..", ".#..", ".#..", "###." },//1
            { "###.", "..#.", "###.", "#...", "###." },//2
            { "###.", "..#.", "###.", "..#.", "###." },
            { "#.#.", "#.#.", "###.", "..#.", "..#." },
            { "###.", "#...", "###.", "..#.", "###." },
            { "###.", "#...", "###.", "#.#.", "###." },
            { "###.", "..#.", "..#.", "..#.", "..#." },
            { "###.", "#.#.", "###.", "#.#.", "###." },
            { "###.", "#.#.", "###.", "..#.", "###." }};

            int[] result = new int[N];

            for (int i = 1; i <= N; i++)
            {
                string[] sn = new string[5];
                for (int j = 0; j < 5; j++)
                {
                    sn[j] = s[j].Substring(4 * (i - 1) + 1, 4);
                   
                }

               
                for (int k = 0; k < 10; k++)
                {
                    int count = 0;
                    for (int j = 0; j < 5; j++)
                    {
                        if (sn[j] == num[k, j])
                        {
                            count++;
                            
                        }
                        else
                        {
                            break;
                        }
                    }
                    if (count == 5)
                    {
                        result[i-1] = k;
                    }
                }

                
            }

            for (int i = 0; i < N; i++)
            {
                Console.Write(result[i]);
            }
        }
    }
}
