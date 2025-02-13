import java.util.Scanner;
import java.util.ArrayList;
import java.util.List;

public class EulerianCycle {
    /*
     * Finds an Eulerian cycle in the given graph
     *
     * @param graph     a List of Strings containing edges in the graph;
     *                  one String may correspond to multiple edges if it
     *                  is of the form "X -> Y,Z"
     *
     * @return a String containing an Eulerian cycle through the given graph
     */
    public static String eulerianCycle(List<String> graph) {
        // TODO: your code here
        return "";
    }

    public static void main(String[] args) {
        Scanner stdin = new Scanner(System.in);
        List<String> graph = new ArrayList<String>();

        while (stdin.hasNextLine()) graph.add(stdin.nextLine());

        System.out.println(eulerianCycle(graph));
    }
}
