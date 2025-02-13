import java.util.Scanner;

class LongestPathDAG {
    /**
     * @param source is the integer label of the source node
     * @param sink is the integer label of the sink node
     * @param edges is a String array of the edges as represented in the input file
     *
     * @return a string containing the output in the correct format
     */
    private static String longestPath(int source, int sink, String[] edges) {
        // TODO: your code here
        return "";
    }

    public static void main(String[] args) {
        Scanner stdin = new Scanner(System.in);
        int source = stdin.nextInt();
        int sink = stdin.nextInt();

        stdin.nextLine();
        
        stdin.useDelimiter("\\Z");
        String[] edges = stdin.next().split("\\n");

        System.out.println(longestPath(source, sink, edges));
    }
}
