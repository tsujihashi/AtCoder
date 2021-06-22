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
            int M = int.Parse(str[1]);
            int Q = int.Parse(str[2]);
            int[] u = new int[N];
            int[] v = new int[N];
            
            for(int i = 0; i < M; i++)
            {
                string[] uv = Console.ReadLine().Split(' ');
                u[i] = int.Parse(uv[0])-1;
                v[i] = int.Parse(uv[1])-1;
            }
            string[] color_str = Console.ReadLine().Split(' ');
            int[] color = new int[N];
            for(int i = 0; i < N; i++)
            {
                color[i] = int.Parse(color_str[i]);
            }
            string[] s = new string[Q];
            for (int i = 0; i < Q; i++)
            {
                s[i] = Console.ReadLine();
            }

            Node[] nodes = new Node[N];
            for(int i = 0; i < N; i++)
            {
                nodes[i] = new Node();
                nodes[i].c = color[i];
                nodes[i].linkedNode = new List<int>();
            }

            for(int i = 0; i < M; i++)
            {
                if (!nodes[u[i]].linkedNode.Contains(v[i]))
                {
                    int n = v[i];
                    nodes[u[i]].linkedNode.Add(n);
                    n = u[i];
                    nodes[v[i]].linkedNode.Add(n);
                }
            }

            for(int i = 0; i < Q; i++)
            {
                string[] sp = s[i].Split(' ');
                int idx = int.Parse(sp[1])-1;
                if (sp.Length == 2)
                {
                    Console.WriteLine(nodes[idx].c);
                    //スプリンクラー起動
                    for(int j = 0; j < nodes[idx].linkedNode.Count; j++)
                    {
                        nodes[nodes[idx].linkedNode[j]].c = nodes[idx].c;
                    }
                }
                else
                {
                    int newColor = int.Parse(sp[2]);
                    Console.WriteLine(nodes[idx].c);
                    nodes[idx].c = newColor;
                }
            }
                

        }
    }

    public class Node
    {
        public int c;
        public List<int> linkedNode = new List<int>();
    }
}
