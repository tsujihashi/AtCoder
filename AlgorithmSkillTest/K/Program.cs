using System;
using System.Collections.Generic;

namespace K
{
    class Program
    {
        static void Main(string[] args)
        {
            string[] str = Console.ReadLine().Split(' ');
            int N = int.Parse(str[0]);
            int Q = int.Parse(str[1]);

            //List<List<int>> data = new List<List<int>>();
            //for(int i = 0; i < N; i++)
            //{
            //    List<int> containers = new List<int>();
            //    containers.Add(i);
            //    data.Add(new List<int>(containers));                    
            //}
            string[] data = new string[N];
            for(int i = 0; i < N; i++)
            {
                data[i] = (i+1).ToString();
            }

            string[] query = new string[Q];
            for(int i = 0; i < Q; i++)
            {
                query[i] = Console.ReadLine();
            }

            for(int i = 0; i < Q; i++)
            {
                string[] q = query[i].Split();
                int f = int.Parse(str[0]);
                int t = int.Parse(str[1]);
                int x = int.Parse(str[2]);

                int idx=data[f-1].IndexOf()
            }
        }
    }
}
