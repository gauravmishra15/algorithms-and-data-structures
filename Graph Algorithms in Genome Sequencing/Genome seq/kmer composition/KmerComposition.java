import java.util.Scanner;

public class KmerComposition {
    /*
     * Computes the k-mer composition of a string text
     *
     * @param k         integer length of k-mers to be found
     * @param text      string to be split into a k-mer composition
     *
     * @return a string with each k-mer in text separated by newlines
     */
    public static String kmerComposition(int k, String text) {
        return "";
    }

    public static void main(String[] args) {
        Scanner stdin = new Scanner(System.in);
        
        int k = stdin.nextInt();
        stdin.nextLine(); // ignore newline after k

        String text = stdin.nextLine();

        System.out.println(kmerComposition(k, text));
    }
}
