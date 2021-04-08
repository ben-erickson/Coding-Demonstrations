using System;
using System.IO;
using System.Collections;
using System.Collections.Generic;

namespace Document_Merger
{
    class Program
    {
        public static List<string> ReadDocument(string fileName) {
            //Read file given by user and return as a list of the lines
            while(true) {
                try {
                    //Open and read file
                    var outList = new List<string>();
                    StreamReader sr = new StreamReader(fileName);
                    string line = sr.ReadLine();

                    while(line != null) {
                        outList.Add(line);
                        charCount += line.Length;
                        line = sr.ReadLine();
                    }
                    sr.Close();
                    outList.Add(fileName);
                    return outList;
                }
                catch {
                    Console.WriteLine("Please enter a valid filename.");
                    fileName = Console.ReadLine();
                }
            }
        }
        public static void WriteDocument(string fileName, List<string> fileData) {
            try {
                StreamWriter sw = new StreamWriter(fileName);
                //Write data to file
                foreach (string elem in fileData) {
                    sw.WriteLine(elem);
                }
                sw.Close();
            }
            catch {
                Console.WriteLine("An error occured writing to the new file.");
            }
        }
        public static string mergedFile;
        public static int charCount;
        public static string userFileName;
        static void Main(string[] args)
        {
            ProgramStart:
            //Declare variables
            var file1 = new List<string>();
            var file2 = new List<string>();
            var mergedList = new List<string>();

            Console.WriteLine("Document Merger\n");

            //Get first file data
            Console.WriteLine("Please enter the first file name.");
            string fileName1 = Console.ReadLine();
            file1 = ReadDocument(fileName1);
            fileName1 = file1[file1.Count - 1];
            file1.Remove(file1[file1.Count - 1]);

            //Get second file data
            Console.WriteLine("Please enter the second file name.");
            string fileName2 = Console.ReadLine();
            file2 = ReadDocument(fileName2);
            fileName2 = file2[file2.Count - 1];
            file2.Remove(file2[file2.Count - 1]);

            //Merge the lists
            mergedList = file1;
            foreach (string elem in file2) {
                mergedList.Add(elem);
            }

            //Remove .txt from first file name
            int txtIndex = fileName1.IndexOf(".txt");
            if (txtIndex >= 0) {
                mergedFile = fileName1.Remove(txtIndex);
            }
            //Merge filenames
            mergedFile += fileName2;

            //Ask the user for the merged filename
            Console.WriteLine($"What would you like to call the new file? (Default: {mergedFile})");
            userFileName = Console.ReadLine();
            if (userFileName.Equals("")) {
                userFileName = mergedFile;
            }
            //Append .txt to the user file name
            if (userFileName.Contains(".txt") != true) {
                userFileName += ".txt";
            }

            //Merge the files and tell the user it was done
            WriteDocument(userFileName, mergedList);
            Console.WriteLine($"{userFileName} was successfully saved. The document contained {charCount} characters.");

            //Repeat if user wants to
            Console.WriteLine("Would you like to combine two more files? (y/n)");
            if (Console.ReadLine().Equals('y')) {
                goto ProgramStart;
            }
        }
    }
}