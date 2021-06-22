using System;

namespace MyLib
{
    public static class MyLib
    {
        public static void test()
        {
            Console.Write("test");
        }

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
    }
}
