import java.util.Scanner;

public class ChangeCoins {
    private static int findChange(int money, int[] coins) {
        // TODO: your code here
        return -1;
    }

    public static void main(String[] args) {
        Scanner stdin = new Scanner(System.in);
        int money = stdin.nextInt();
        stdin.nextLine();

        String[] rawCoins = stdin.nextLine().split(",");
        int[] coins = new int[rawCoins.length];

        for (int i = 0; i < rawCoins.length; i++) {
            coins[i] = Integer.parseInt(rawCoins[i]);
        }

        System.out.println(findChange(money, coins));
    }
}
