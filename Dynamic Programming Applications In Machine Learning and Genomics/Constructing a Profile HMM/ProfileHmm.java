import java.util.Scanner;
import java.util.ArrayList;


public class ProfileHmm {

    /*
     * Creates a profile HMM from a multiple alignment.
     *
     * @param theta         a double threshold for the seed alignment
     * @param sigma         an array of chars containing the HMM alphabet 
     * @param alignment     an array of Strings containing the multiple alignment 
     *                      for which the profile HMM will be constructed.  
     *
     * @return a String with the emission and transition matrices formatted 
     * according to the problem output specification.
     */
    public static String profileHmm(double theta, char[] sigma, String[] alignment) {
        // TODO: your code here
        return "";
    }

    public static void main(String[] args) {
        Scanner stdin = new Scanner(System.in);

        // read in theta threshold
        double theta = stdin.nextDouble();
        stdin.nextLine();   // newline at the end of first
        stdin.nextLine();   // delimiter

        // read in HMM alphabet
        char[] sigma = String.join("", stdin.nextLine().split(" ")).toCharArray();
        stdin.nextLine();   // delimiter

        // read in multiple alignment
        ArrayList<String> tempAlignment = new ArrayList<>(); 
        while (stdin.hasNextLine()) {
            tempAlignment.add(stdin.nextLine());
        }
        String[] alignment = new String[tempAlignment.size()];
        alignment = tempAlignment.toArray(alignment);

        // compute profile HMM
        System.out.println(profileHmm(theta, sigma, alignment));
    }
}
