// name: spiral
import java.io.*;

public class SpiralGuide {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    static class TestCase {
        // This is the class that stores the values in an input!
        int n;
    }
    
    // You don't need to do anything here; I've already written it for you! You're welcome
    public static TestCase read() throws java.lang.Exception {
        // Creates a TestCase object to store the inputs
        TestCase testCase = new TestCase();

        // Read in the input and turns it into an integer
        // Ex: turns "9" into 9
        int n = Integer.parseInt(br.readLine());

        // Store the input into the TestCase object
        testCase.n = n;

        return testCase;
    }

    public static void logic(TestCase testCase) {
        // n: A positive integer denoting the number of loops the spiral must have
        int n = testCase.n;
        // It's your turn to code! Use the variable(s) above to find your answer

        // TODO: YOUR CODE HERE

        return; // Remember to output your solution; replace this line when you're done!
    }

	public static void main(String[] args) throws java.lang.Exception {
        int T = Integer.parseInt(br.readLine());
        for (int i = 0; i < T; i++) {
            logic(read());
            System.out.println(""); // Remember the blank line in between outputs!
        }
    }
}