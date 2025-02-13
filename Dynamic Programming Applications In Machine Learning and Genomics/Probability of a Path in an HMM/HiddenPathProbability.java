import java.util.Scanner;
import java.util.HashMap;

public class CompletedStarter {

    /*
     * Computes the probability of the path pi given an HMM
     *
     * @param pi            a String representing the path of states
     * @param states        an array of chars representing possible states
     * @param transition    a HashMap s.t. transition.get(x).get(y)
     *                      is the probability of transitioning from state
     *                      x to state y. x and y are both chars in states.
     *              
     *
     * @return a double with the correct probability to at least three 
     * significant figures
     */
    public static double pathProbability(String pi, char[] states, 
            HashMap<Character, HashMap<Character, Double>> transition) {
        // TODO: your code here
        return 0.0;
    }

    public static void main(String[] args) {
        Scanner stdin = new Scanner(System.in);
        String pi = stdin.nextLine();

        stdin.nextLine(); // delimiter

        char[] states = String.join("", stdin.nextLine().split(" ")).toCharArray();

        stdin.nextLine(); // delimiter
        stdin.nextLine(); // first line of transition

        HashMap<Character, HashMap<Character, Double>> transition;
        transition = new HashMap<>();

        for (char state : states) {
            HashMap<Character, Double> inner = new HashMap<>();
            String[] currLine = stdin.nextLine().split("\t");

            for (int i = 1; i < currLine.length; i++)
                inner.put(states[i-1], Double.valueOf(currLine[i]));
            
            transition.put(state, inner);
        }

        System.out.println(pathProbability(pi, states, transition));
    }
}
