import java.util.Scanner;
import java.util.ArrayList;
import java.util.List;

public class StringFromGenomePath {
    /*
     * Reconstructs a string from its genome path
     *
     * @param patterns      a list of String k-mers in the order they appear
     *                      in text
     *
     * @return a String text with the given genome path
     */
    public static String reconstructString(List<String> patterns) {
        // TODO: your code here
        return "";
    }

    public static void main(String[] args) {
        Scanner stdin = new Scanner(System.in);
        List<String> patterns = new ArrayList<String>();

        while (stdin.hasNextLine()) patterns.add(stdin.nextLine());

        System.out.println(reconstructString(patterns));
    }
}
