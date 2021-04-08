using System;
using System.IO;
namespace Document
{
    class Program
    {
        static void Main(string[] args)
        {
            //Declaring variables
            string fileName;
            string name;
            string fileContent;
            bool exception = false;

            Console.WriteLine("Document");
            Console.WriteLine();

            //Get user input for filename and content
            Console.WriteLine("What would you like the name of the file to be?");
            name = Console.ReadLine();
            Console.WriteLine("What would you like to put into the file?");
            fileContent = Console.ReadLine();

            //Append .txt to filename
            fileName = name + ".txt";

            //Write to file
            try {
                StreamWriter sw = new StreamWriter(fileName);
                sw.WriteLine(fileContent);
                sw.Close();
            }
            catch (Exception e){
                Console.WriteLine("Exception:" + e.Message);
                exception = true;
            }

            //Output message if no error occured
            if(exception == false) {
                Console.WriteLine($"{name} was successfully saved. The document contains " + fileContent.Length + " characters.");
            }

        }
    }
}
