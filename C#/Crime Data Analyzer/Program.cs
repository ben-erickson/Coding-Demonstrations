using System;
using System.IO;
using System.Collections.Generic;
using System.Linq;

namespace Crime_Data_Analyzer
{
    public class IncorrectCLAException : Exception {
        public IncorrectCLAException() {} 
    }
    public class Data {
        public int Year {get; set;}
        public int Population {get; set;}
        public int ViolentCrime {get; set;}
        public int Murder {get; set;}
        public int Rape {get; set;}
        public int Robbery {get; set;}
        public int AggravatedAssault {get; set;}
        public int PropertyCrime {get; set;}
        public int Burglary {get; set;}
        public int Theft {get; set;}
        public int MotorVehicleTheft {get; set;}
        public static Data ParseRow(string row) {
            //Take a row of data and create a Data object using it
            var point = row.Split(',');
            //I needed to convert all the elements to ints, and I couldn't figure out a better way
            //with linq, but I am sure that there is one
            List<int> tempList = new List<int>();
            foreach (string elem in point) {
                try {
                    tempList.Add(Int32.Parse(elem));
                }
                catch {
                    Console.WriteLine("One of the datapoints was not a number.");
                }
            }
            return new Data {
                Year = tempList[0],
                Population = tempList[1],
                ViolentCrime = tempList[2],
                Murder = tempList[3],
                Rape = tempList[4],
                Robbery = tempList[5],
                AggravatedAssault = tempList[6],
                PropertyCrime = tempList[7],
                Burglary = tempList[8],
                Theft = tempList[9],
                MotorVehicleTheft = tempList[10]
            };
        }
    }
    class Program
    {
        static void Main(string[] args)
        {
            try {
                //Get the filenames from Command Line Arguments and put them in a list
                List<string> fileNames = new List<string>();
                foreach (string arg in args) {
                    fileNames.Add(arg);
                }
                //Get data and create class objects of each row using the ParseRow method
                var data = File.ReadAllLines(fileNames[0])
                    .Skip(1)
                    .Select(Data.ParseRow);

                //Data list
                string[] outList = new string[11];

                //Query 1
                Object[] extYear = new Object[]{(data.First()).Year, (data.Last()).Year};
                outList[0] = $"This report covers the years {extYear[0]}-{extYear[1]}.";

                //Query 2
                int yearDiff = (data.Last().Year - data.First().Year);
                outList[1] = $"The report covers {yearDiff} years.";

                //Query 3
                var qMurder = from elem in data
                    where elem.Murder < 15000
                    select elem.Year;
                string sMurder = string.Join(',', qMurder);
                outList[2] = $"Years with murder < 15000: {sMurder}.";

                //Query 4
                var qRobbery = from elem in data
                    where elem.Robbery > 500000
                    select new { Year = elem.Year, Robbery = elem.Robbery};
                string sRobbery = "";
                foreach (var elem in qRobbery) {
                    sRobbery += $"{elem.Year} = {elem.Robbery}, ";
                }
                outList[3] = $"Years with robberies > 500000: {sRobbery}";

                //Query 5
                var qRobb = from elem in data
                    where elem.Year == 2010
                    select elem.Robbery;
                var qPopu = from elem in data
                    where elem.Year == 2010
                    select elem.Population;
                float sRobb = qRobb.FirstOrDefault();
                float sCapita = sRobb / qPopu.FirstOrDefault();
                outList[4] = $"The violent crime per capita in 2010 was: {sCapita}.";

                //Query 6
                var qAvMur = (from elem in data
                    select elem.Murder)
                    .Average();
                outList[5] = $"The average of murders for all years is: {qAvMur}.";

                //Query 7
                var q90sMur = (from elem in data
                    where elem.Year < 1998 && elem.Year >1993
                    select elem.Murder)
                    .Average();
                outList[6] = $"The average for murders from 1994-1997 is: {q90sMur}.";

                //Query 8
                var q10sMur = (from elem in data
                    where elem.Year < 2014 && elem.Year > 2009
                    select elem.Murder)
                    .Average();
                outList[7] = $"The average for murders from 2010-2013 is: {q10sMur}.";

                //Query 9
                var qMinRob = (from elem in data
                    where elem.Year > 1998 && elem.Year < 2005
                    select elem.Robbery)
                    .Min();
                outList[8] = $"The minimum amount of robberies per year from 1999-2004 is: {qMinRob}.";

                //Query 10
                var qMaxRob = (from elem in data
                    where elem.Year > 1998 && elem.Year < 2005
                    select elem.Robbery)
                    .Max();
                outList[9] = $"The maximum amount of robberies per year from 1999-2004 is: {qMaxRob}.";

                //Query 11
                var qMaxGTA = (from elem in data
                    select elem.MotorVehicleTheft)
                    .Max();
                var qMaxGTAYear = from elem in data
                    where elem.MotorVehicleTheft == qMaxGTA
                    select elem.Year;
                string sMaxGTA = string.Join(',',qMaxGTAYear);
                outList[10] = $"The year with the most motor vehicle theft was: {sMaxGTA}.";

                File.WriteAllLines(fileNames[1],outList);
                Console.WriteLine($"Data written to {fileNames[1]}.");
            }
            catch(IncorrectCLAException) {
                Console.WriteLine("Please run the program as: CrimeDataAnalyzer <crime_csv_file_path> <report_file_path>");
            }
            catch {
                Console.WriteLine("An error occured. /:");
            }
        }
    }
}
