using System;

namespace F
{
    class Program
    {
        static void Main(string[] args)
        {
            int N = int.Parse(Console.ReadLine());
            string[]a = new string[N];
            char[] alphabet = new char[26]
            {
                'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o',
                'p','q','r','s','t','u','v','w','x','y','z'
            };
            for(int i = 0; i < N; i++)
            {
                a[i] = Console.ReadLine();
            }
            char[] result = new char[N];
            for(int i = 0; i < (N+1)/2; i++)
            {
                bool ok = false;
                for(int j = 0; j < 26; j++)
                {
                    if(a[i].Contains(alphabet[j])&&
                            a[N - 1 - i].Contains(alphabet[j]))
                    {
                        ok = true;
                        result[i]= alphabet[j];
                        result[N - 1 - i] = alphabet[j];
                    }
                }
                if (!ok) result = new char[2] { '-', '1' };
            }

            string result_str = result.ToString();
            Console.Write(result);
        }
    }
}
