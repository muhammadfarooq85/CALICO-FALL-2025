// name: dna
import java.io.*;

public class DnaGuide {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    static class TestCase {
        // This is the class that stores the values in an input!
        String dna;
    }
    
    // You don't need to do anything here; I've already written it for you! You're welcome
    public static TestCase read() throws java.lang.Exception {
        // Creates a TestCase object to store the inputs
        TestCase testCase = new TestCase();

        // Read in the input
        String dna = br.readLine();

        // Store the input into the TestCase object
        testCase.dna = dna;

        return testCase;
    }

    public static void logic(TestCase testCase) {
        // dna: the string of DNA bases, consisting of letters A, T, C, and G
        String dna = testCase.dna;
        // It's your turn to code! Use the variable(s) above to find your answer

        // TODO: YOUR CODE HERE

        return; // Remember to output your solution; replace this line when you're done!
    }

	public static void main(String[] args) throws java.lang.Exception {
        int T = Integer.parseInt(br.readLine());
        for (int i = 0; i < T; i++) {
            logic(read());
        }
    }
}