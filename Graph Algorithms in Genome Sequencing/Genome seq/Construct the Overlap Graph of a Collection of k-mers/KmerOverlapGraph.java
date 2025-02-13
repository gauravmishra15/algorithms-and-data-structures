import java.util.Scanner;
import java.util.ArrayList;
import java.util.List;

public class KmerOverlapGraph {
    /*
     * Creates an overlap graph from a list of k-mers
     *
     * @param patterns      a list of String k-mers
     *
     * @return a string containing an adjacency list representation of the
     * overlap graph as described in the problem specification
     */
    public static String overlapGraph(List<String> patterns) {
        // TODO: your code here
        return "";
    }

    public static void main(String[] args) {
        Scanner stdin = new Scanner(System.in);
        List<String> patterns = new ArrayList<String>();

        while (stdin.hasNextLine()) patterns.add(stdin.nextLine());

        System.out.println(overlapGraph(patterns));
    }
}
