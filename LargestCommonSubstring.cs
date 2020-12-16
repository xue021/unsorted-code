using System;
//compares string s1 and s2 to find the largest substring found in both strings
namespace LargestCommonSubstring
{
    class Program
    {
        static void Main(string[] args)
        {
            String s1 = "aaabbcccccaaaaab123456789101112131415bxyxyxyxyxy";
            String s2 = "aaaab123456789101112131415babbcaaaaaabxyxyxyxyxy";

            String longestStringSeen = "";
            // find longest substring contained in both strings

            for (int i = 0; i < s1.Length; i++)
            {
                bool subStrContains = s2.Contains(s1.Substring(i, 1));
                int j = 1;


                while (subStrContains)
                {

                    if (i + j >= s1.Length)
                    {
                        break;
                    }
                    if (i + j < s1.Length)
                    {
                        //Console.WriteLine(s1.Substring(i, j));
                        j++;
                        String substr = s1.Substring(i, j);
                        subStrContains = s2.Contains(substr);
                        if (subStrContains && substr.Length > longestStringSeen.Length)
                        {
                            longestStringSeen = substr;
                        }
                    }


                }





            }
            Console.WriteLine("Longest String Seen is:");
            Console.WriteLine(longestStringSeen);
            Console.WriteLine("it is " + longestStringSeen.Length + " chars long.");

        }
    }
}
