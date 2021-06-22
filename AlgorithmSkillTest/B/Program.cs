using System;
using System.Collections.Generic;

namespace B
{
    class Program
    {
        static void Main(string[] args)
        {
            string[] str = Console.ReadLine().Split(' ');
            int N = int.Parse(str[0]);
            int M = int.Parse(str[1]);
            int Q = int.Parse(str[2]);

            //int[] score = new int[N];
            //int[] solvedNum = new int[M];
            List<List<int>> solvedList = new List<List<int>>();
            for(int i = 0; i < M; i++)
            {
                solvedList.Add(new List<int>());
            }

            string[] query = new string[Q];
            for(int i = 0; i < Q; i++)
            {
                query[i] = Console.ReadLine();
            }

            //クエリ処理
            for(int i = 0; i < Q; i++)
            {
                string[] s = query[i].Split(' ');
                int sankasya = int.Parse(s[1])-1;

                if (s.Length ==2)
                {
                    //スコア表示
                    int score = 0;
                    for(int j = 0; j < M; j++)
                    {
                        if (solvedList[j].Contains(sankasya)) score += N - solvedList[j].Count;
                    }
                    Console.WriteLine(score);
                }
                else
                {
                    //問題を解いた
                    int problem = int.Parse(s[2]) - 1;
                    solvedList[problem].Add(sankasya);
                }
            }
        }
    }
}
