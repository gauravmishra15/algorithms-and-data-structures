import java.util.Scanner;
import java.util.List;
import java.util.ArrayList;

public class Contigs {
    /*
     * Finds all contigs in a de Bruijn graph made from patterns
     *
     * @param patterns      a List of Strings containing all k-mers to
     *                      be used to construct the de Bruijn graph for
     *                      this problem
     *
     * @return a String with all the contigs in the format specified in the
     * problem description
     */
    public static String contigs(List<String> patterns) {
        // TODO: your code here
        return "";
    }

    public static void main(String[] args) {
        Scanner stdin = new Scanner(System.in);

        List<String> patterns = new ArrayList<>();
        while (stdin.hasNextLine()) patterns.add(stdin.nextLine());

        System.out.println(contigs(patterns));
    }
}
