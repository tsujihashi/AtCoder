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
            string[] str = Console.ReadLine().Split(' ');
            int N = int.Parse(str[0]);
            int A = int.Parse(str[1]);
            int B = int.Parse(str[2]);
            int C = int.Parse(str[3]);
            int D = int.Parse(str[4]);
            string S = Console.ReadLine();
            string result="Yes";

            if (C < D)//すぬけとふぬけが入れ替わらない場合
            {
                if (S.Substring(A-1,D-A+1).Contains("##"))
                {
                    result = "No";
                }

                if (S.Substring(C - 1, 1) == "#"/*&&S.Substring(B,1)=="#"*/)
                {
                    result = "No";
                }

                //for (int i = A; i < D; i++)
                //{
                //    string a = S.Substring(i - 1,2);
                //    if (a == "##")
                //    {
                //        result = "No";
                //        break;
                //    }

                //}
            }
            else
            {
                if (S.Substring(A-1, C - A+1).Contains("##")|| (!S.Contains("...")))
                {
                    result = "No";
                }

                if (S.Substring(D - 1, 1) == "#"/*&&S.Substring(B, 1) == "#"*/)
                {
                    result = "No";
                }

                //for (int i = A; i < D; i++)
                //{
                //    string a = S.Substring(i - 1, 2);
                //    if (a == "##")
                //    {
                //        result = "No";
                //        break;
                //    }
                //    if (!S.Contains("..."))
                //    {
                //        result = "No";
                //        break;
                //    }
                //}
            }

            Console.Write(result);
        }
    }
}
