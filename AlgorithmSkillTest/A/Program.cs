using System;

namespace A
{
    class Program
    {
        static void Main(string[] args)
        {
            string s = Console.ReadLine();
            string t = Console.ReadLine();

            string result = "";

            if (s == t)
            {
                result = "same";
            }
            else if (s.ToLower() == t.ToLower())
            {
                result = "case-insensitive";
            }
            else
            {
                result = "different";
            }

            Console.Write(result);
        }
    }
}
