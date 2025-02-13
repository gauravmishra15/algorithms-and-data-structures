import java.util.Scanner;
import java.util.List;
import java.util.ArrayList;

public class StringReconstruction {
    /*
     * Reconstructs a string from its k-mer composition
     *
     * @param k         the length of the k-mers in the composition
     * @param patterns  a List of Strings containing the k-mer composition
     *
     * @return a String text with k-mer composition equal to patterns
     */
    public static String reconstruct(int k, List<String> patterns) {
        // TODO: your code here
        return "";
    }

    public static void main(String[] args) {
        Scanner stdin = new Scanner(System.in);

        int k = stdin.nextInt();
        stdin.nextLine(); // ignore newline char after k

        List<String> patterns = new ArrayList<>();

        while (stdin.hasNextLine()) patterns.add(stdin.nextLine());

        System.out.println(reconstruct(k, patterns));
    }
}
