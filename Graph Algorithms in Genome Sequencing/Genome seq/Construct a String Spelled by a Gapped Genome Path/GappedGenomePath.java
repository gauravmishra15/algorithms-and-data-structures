import java.util.Scanner;
import java.util.List;
import java.util.ArrayList;


public class GappedGenomePath {
    /*
     * Reconstructs a String from its gapped genome path
     *
     * @param k             length of k-mers
     * @param d             length of gap
     * @param paired_comp   List of Strings containing the gapped genome path
     *
     * @return a String with the appropriate gapped genome path
     */
    public static String reconstruct(int k, int d, List<String> pairedComp) {
        // TODO: your code here
        return "";
    }

    public static void main(String[] args) {
        Scanner stdin = new Scanner(System.in);

        int k = stdin.nextInt();
        int d = stdin.nextInt();
        stdin.nextLine(); // ignore extra newline

        List<String> pairedComp = new ArrayList<>();

        while (stdin.hasNextLine()) pairedComp.add(stdin.nextLine());

        System.out.println(reconstruct(k, d, pairedComp));
    }
}
