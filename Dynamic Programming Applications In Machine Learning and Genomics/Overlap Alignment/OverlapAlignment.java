import java.util.Scanner;

public class OverlapAlignment {
    /**
     * @param m - the match score
     * @param mu - the mismatch score
     * @param sigma - the indel score
     * @param s - the first string to be aligned
     * @param t - the second string to be aligned
     *
     * align a suffix of s with a prefix of t
     *
     * @return a string with the alignment score and reconstructed 
     * alignment in the correct format for this problem
     */
    private static String align(int m, int mu, int sigma, String s, String t) {
        // TODO: your code here
        return "";
    }

    public static void main(String[] args) {
        Scanner stdin = new Scanner(System.in);
        int m = stdin.nextInt();
        int mu = stdin.nextInt();
        int sigma = stdin.nextInt();

        stdin.nextLine();

        String s = stdin.nextLine();
        String t = stdin.nextLine();

        System.out.println(align(m,mu,sigma,s,t));
    }
}
