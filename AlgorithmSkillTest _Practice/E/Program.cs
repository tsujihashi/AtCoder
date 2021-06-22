using System;
using System.Collections.Generic;

namespace E
{
    class Program
    {
        static void Main(string[] args)
        {
            string[] str = Console.ReadLine().Split(' ');
            int N = int.Parse(str[0]);
            int Q = int.Parse(str[1]);

            string[] S = new string[Q];
            for(int i = 0; i < Q; i++)
            {
                S[i] = Console.ReadLine();
            }

            char[,] f = new char[N, N];
            for(int i = 0; i < N; i++)
            {
                for(int j = 0; j < N; j++)
                {
                    f[i, j] = 'N';
                }
            }

            for(int i = 0; i < Q; i++)
            {
                string[] str2 = S[i].Split(' ');
                int mode = int.Parse(str2[0]);
                int a, b;

                switch (mode)
                {
                    case 1:
                        a = int.Parse(str2[1]);
                        b = int.Parse(str2[2]);
                        f[a - 1, b - 1] = 'Y';
                        break;

                    case 2:
                        a = int.Parse(str2[1]);
                        for (int j = 0; j < N; j++)
                        {
                            if (f[j, a - 1] == 'Y')
                            {
                                f[a - 1, j] = 'Y';
                            }
                        }
                        break;
                    case 3:
                        a = int.Parse(str2[1]);
                        List<int> tofollow = new List<int>();
                        for (int j = 0; j < N; j++)
                        {
                            if(f[a - 1, j] == 'Y')
                            {
                                for (int k = 0; k < N; k++)
                                {
                                    if (f[j, k] == 'Y')
                                    {
                                        tofollow.Add(k);
                                        
                                    }
                                }
                            }
                            
                        }

                        for(int j = 0; j < tofollow.Count; j++)
                        {
                            f[a - 1, tofollow[j]] = 'Y';
                        }
                        break;

                }

                
            }

            for (int i = 0; i < N; i++)
            {
                for(int j = 0; j < N; j++)
                {
                    Console.Write(f[i, j]);
                }
                Console.Write("\r\n");
            }

        }
    }
}
