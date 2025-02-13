import java.util.Scanner;

public class AffineGapPenalties {
    /**
     * @param m - the match score
     * @param mu - the mismatch score
     * @param sigma - the gap opening penalty
     * @param eps - the gap extension penalty
     * @param s - the first string to be aligned
     * @param t - the second string to be aligned
     *
     * @return a string with the alignment score and reconstructed 
     * alignment in the correct format for this problem
     */
    private static String align(int m, int mu, int sigma, int eps, String s, String t) {
        // TODO: your code here
        return "";
    }

    public static void main(String[] args) {
        Scanner stdin = new Scanner(System.in);
        int m = stdin.nextInt();
        int mu = stdin.nextInt();
        int sigma = stdin.nextInt();
        int eps = stdin.nextInt();

        stdin.nextLine();

        String s = stdin.nextLine();
        String t = stdin.nextLine();

        System.out.println(align(m,mu,sigma,eps,s,t));
    }
}
