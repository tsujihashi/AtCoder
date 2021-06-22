using System;

namespace MyLib
{
    public static class MyLib
    {
        public static void test()
        {
            Console.Write("test");
        }

        /// <summary>
        /// int配列内のi番目とj番目の入れ替え
        /// </summary>
        /// <param name="a"></param>
        /// <param name="i"></param>
        /// <param name="j"></param>
        public static void swap(ref int[] a,int i,int j)
        {
            if ((0 <= i&& i < a.Length)&& (0 <= j && j < a.Length))
            {
                int w = a[i];
                a[i] = a[j];
                a[j] = w;
            }
            else
            {
                Console.Write("インデックスが配列の境界外です。i="+i+"j="+j+"\r\n");
            }
        }

        /// <summary>
        /// 文字列配列をint配列に変換
        /// </summary>
        /// <param name="strArr"></param>
        /// <returns></returns>
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

        /// <summary>
        /// string配列をDouble配列に変換
        /// </summary>
        /// <param name="strArr"></param>
        /// <returns></returns>
        public static int[] stringArrayToDoubleArray(string[] strArr)
        {
            double[] doubleArr = new int[strArr.Length];
            for (int i = 0; i < strArr.Length; i++)
            {
                try
                {
                    doubleArr[i] = double.Parse(strArr[i]);
                }
                catch
                {
                    doubleArr[i] = -9999;
                }

            }
            return doubleArr;
        }

        /// <summary>
        /// 文字列を逆順にソート
        /// </summary>
        /// <param name="s"></param>
        public static void reverseSort(ref string s)
        {
            char[] c = s.ToCharArray();
            for(int i = 0; i < c.Length/2; i++)
            {
                char w;
                w = c[i];
                c[i] = c[c.Length - 1 - i];
                c[c.Length - 1 - i] = w;
            }
            s = c.ToString();
        }
    }
}
