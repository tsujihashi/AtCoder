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
            int P = int.Parse(str[0]);
            int Q = int.Parse(str[1]);
            int R = int.Parse(str[2]);

            
            //int PQ = P + Q;
            //int QR = Q + R;
            //int RP = R + P;

            int[] array = new int[3];
            array[0] = P;
            array[1] = Q;
            array[2] = R;
            Array.Sort(array);

            int result = array[0] + array[1];
            Console.Write(result);


            //Console.ReadKey();
            
        }
    }
}
