import java.util.Random;
import java.util.Scanner;

public class Guess {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        Random r = new Random();
        int totalWon = 0;

        for (int i = 0; i < 5; i++) {
            System.out.println("Guess 1 - 3 :");

            int n = s.nextInt();
            int c = r.nextInt(3) + 1;

            if (n == c) {
                System.out.println("You Won!\n");
                totalWon++;
            } else {
                System.out.println("You Lost! Computer chose : " + c + "\n");
            }
        }
        System.out.println("Total Won : " + totalWon + "/5");
    }
}

