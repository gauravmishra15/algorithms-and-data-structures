import java.util.Scanner;

public class DeBruijnString {
    /*
     * Creates a de Bruijn graph from a string given a value of k
     *
     * @param k         the length of strings represented by edges in the 
     *                  de Bruijn graph
     * @param text      the String from which the de Bruijn graph will be 
     *                  constructed
     *
     * @return a String containing an adjacency list representation of the
     * de Bruijn graph as described in the problem specification
     */
    public static String deBruijn(int k, String text) {
        // TODO: your code here
        return "";
    }

    public static void main(String[] args) {
        Scanner stdin = new Scanner(System.in);

        int k = stdin.nextInt();
        stdin.nextLine(); // skip newline after k

        String text = stdin.nextLine();

        System.out.println(deBruijn(k, text));
    }
}
