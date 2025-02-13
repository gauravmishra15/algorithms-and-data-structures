import java.util.Scanner;
import java.util.List;
import java.util.ArrayList;

public class DeBruijnKmers {
    /*
     * Creates a de Bruijn graph from a collection of k-mers
     *
     * @param patterns      a List of Strings containing the collection of k-mers
     *                      to be made into a de Bruijn graph
     *
     * @return a String containing an adjacency list representation of the
     * de Bruijn graph as described in the problem specification
     */
    public static String deBruijn(List<String> patterns) {
        // TODO: your code here
        return "";
    }

    public static void main(String[] args) {
        Scanner stdin = new Scanner(System.in);
        List<String> patterns = new ArrayList<String>();

        while (stdin.hasNextLine()) patterns.add(stdin.nextLine());

        System.out.println(deBruijn(patterns));
    }
}
