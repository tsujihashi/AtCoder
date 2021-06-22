using System;
using System.Linq;

namespace H
{
    class Program
    {
        static void Main(string[] args)
        {
            int N = int.Parse(Console.ReadLine());
            string[] C_str = Console.ReadLine().Split(' ');
            int[] C = new int[N];
            for(int i = 0; i < N; i++)
            {
                C[i] = int.Parse(C_str[i]);
            }
            int Q = int.Parse(Console.ReadLine());
            
            int[][] S = new int[Q][];
            for (int i = 0; i < Q; i++)
            {
                string[] query_str = Console.ReadLine().Split(' ');
                int[] query = stringArrayToIntArray(query_str);
                S[i] = query;
            }

            int result = 0;
            for(int i = 0; i < Q; i++)
            {
                int mode = S[i][0];
                int x, a;
                switch (mode)
                {
                    case 1: 
                        //xをa枚
                        x = S[i][1];
                        a = S[i][2];
                        if (a <= C[x-1])
                        {
                            C[x-1] -= a;
                            result += a;
                        }
                        break;
                    case 2:
                        //奇数カードをa枚
                        a = S[i][1];
                        int min = int.MaxValue;
                        for(int j = 0; j < N; j+=2)
                        {
                            if(C[j]<min)
                            {
                                min = C[j];
                            }
                        }
                        if (a <= min)
                        {
                            for (int j = 0; j < N; j+=2)
                            {
                                C[j] -= a;
                                result += a;
                            }
                        }
                        break;
                    case 3: 
                        //全カードをa枚
                        a = S[i][1];
                        if (a <= C.Min())
                        {
                            for(int j = 0; j < N; j++)
                            {
                                C[j] -= a;
                                result += a;
                            }
                        }
                            
                        break;
                }
            }

            Console.Write(result);
        }

        public static int[] stringArrayToIntArray(string[] strArr)
        {
            int[] intArr = new int[strArr.Length];
            for (int i = 0; i < strArr.Length; i++)
            {
                try
                {
                    intArr[i] = int.Parse(strArr[i]);
                }
                catch
                {
                    intArr[i] = -9999;
                }

            }
            return intArr;
        }
    }
}
