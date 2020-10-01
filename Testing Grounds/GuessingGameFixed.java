import java.util.Random;   //to create a random number
import java.util.Scanner;  //rely on user input

/*
 * Creating a game called the Guessing Game to find guess an integer between 1 and 1000
 * Project 2
 */
public class GuessingGame 				//public class GuessingGame
{

	public static void main (String[] args) //main
	{
		
		Random rand = new Random();  //random variable
		
		int specialNum = rand.nextInt(1001); //produce random in the interval [1, 1000)
												    
		Scanner scan = new Scanner(System.in);         							
		int guess, totalGuesses = 0;  //renamed to guess for clairity	
		int points = 100;  //renamed to points for clairity				       									
		boolean win = false;  //declare boolean for while loop
	
		System.out.println ("Welcome to the Guessing Game!"); 					
		while (!win) {

			System.out.print ("Enter a positive integer up to 1000: "); //prompt to start game and get user number
			guess = scan.nextInt();

			totalGuesses = totalGuesses + 1; //increment total guesses
			points = points - 5;			//decrement points
			
			if (guess < specialNum) // if guess is less than the random num, tell the user and continue to loop.
				System.out.println ("Too Low");  

			else if (guess > specialNum) // if guess is greater than the random num, tell the user and continue to loop.
				System.out.println ("Too High");  
			
			else if (guess == specialNum)  // if guess is equal to the random num, we can exit the while loop.
				win = true;	
		}
	
		System.out.println ("You Win!"); 
		System.out.println ("It took you " + totalGuesses + " guesses to figure it out."); 	//Tell user how many guesses it took
		System.out.println ("You earned " +  points + " points.");                     		// Total points earned starting from 100
		System.out.println ();														 		//line break for visual appearance
		System.out.println ("Goodbye");                                              		// print out "Goodbye". End of game	
		scan.close();
	}//main


	
}//GuessingGame
