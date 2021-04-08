using System;

namespace Dog
{
    public enum Gender {
        Male,
        Female
    }
    public class Dog {
        public string dogName;
        public string dogOwner;
        public int dogAge;
        public Gender dogGender;
        public Dog(string name, string owner, int age, Gender gender) {
            dogName = name;
            dogOwner = owner;
            dogAge = age;
            dogGender = gender;
        }
        public void Bark(int barks) {
            for (int i = 0; i < barks; i++) {
                Console.WriteLine("Woof!");
            }
        }
        public string getTag() {
            //Declare strings
            string pronoun;
            string otherPronoun;
            string plural;
            
            //Get strings ready based on gender
            if (dogGender == 0) {
                pronoun = "His";
                otherPronoun = "he";
            }
            else {
                pronoun = "Her";
                otherPronoun = "she";
            }

            if (dogAge > 1) {
                plural = "years";
            }
            else {
                plural = "year";
            }
            return($"If lost, call {dogOwner}. {pronoun} name is {dogName} and {otherPronoun} is {dogAge}  {plural} old.");
        }
    }
    class Program
    {
        static void Main(string[] args)
        {
            Dog frog = new Dog("Frog", "Mom", 12, Gender.Female);
            frog.Bark(4);
            Console.WriteLine(frog.getTag());
        }
    }
}