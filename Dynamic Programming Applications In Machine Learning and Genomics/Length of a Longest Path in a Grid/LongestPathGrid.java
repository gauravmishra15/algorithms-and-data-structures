import java.util.Scanner;

public class LongestPathGrid {
    private static int longestPath(int n, int m, int[][] down, int[][] right) {
        // TODO: your code here
        return -1;
    }

    public static void main(String[] args) {
        Scanner stdin = new Scanner(System.in);
        int n = stdin.nextInt();
        int m = stdin.nextInt();
        stdin.nextLine();

        int[][] down = new int[n][m+1];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m+1; j++) {
                down[i][j] = stdin.nextInt();
            }
            stdin.nextLine();
        }

        stdin.nextLine();

        int[][] right = new int[n+1][m];
        for (int i = 0; i < n+1; i++) {
            for (int j = 0; j < m; j++) {
                right[i][j] = stdin.nextInt();
            }
            stdin.nextLine();
        }

        System.out.println(longestPath(n, m, down, right));
    }
}
