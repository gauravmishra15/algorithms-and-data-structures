import java.util.Scanner;
import java.util.HashMap;

public class OutcomeLikelihood {
    /*
     * Computes the maximum likelihood of a given outcome for an HMM.
     *
     * @param x             the emitting string from the HMM
     * @param sigma         an array of chars representing the HMM alphabet
     * @param states        an array of chars representing possible states
     * @param transition    a HashMap s.t. transition.get(x).get(y)
     *                      is the probability of transition from 
     *                      state x to state y. 
     *                      x and y are both chars in states.
     * @param emission      a HashMap s.t. emission.get(x).get(y)
     *                      is the probability of emitting character y from 
     *                      state x. x and y are both chars. x is a state,
     *                      y is a letter in sigma.
     *              
     * @return a double maximum likelihood to at least three significant figures
     */
    public static double outcomeLikelihood(String x, char[] sigma, char[] states, 
            HashMap<Character, HashMap<Character, Double>> transition,
            HashMap<Character, HashMap<Character, Double>> emission) {
        // TODO: your code here
        return 0.0; 
    }

    public static void main(String[] args) {
        Scanner stdin = new Scanner(System.in);
        String x = stdin.nextLine();
        stdin.nextLine(); // delimiter

        char[] sigma = String.join("", stdin.nextLine().split(" ")).toCharArray();
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

        stdin.nextLine(); // delimiter
        stdin.nextLine(); // first line of emission

        HashMap<Character, HashMap<Character, Double>> emission;
        emission = new HashMap<>();

        for (char state : states) {
            HashMap<Character, Double> inner = new HashMap<>();
            String[] currLine = stdin.nextLine().split("\t");

            for (int i = 1; i < currLine.length; i++)
                inner.put(sigma[i-1], Double.valueOf(currLine[i]));
            
            emission.put(state, inner);
        }

        System.out.println(outcomeLikelihood(x, sigma, states, transition, emission));
    }
}
