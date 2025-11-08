// name: spiral
import java.io.*;

public class SpiralTemplate {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    static class TestCase {
        int n;
    }
    
    public static TestCase read() throws java.lang.Exception {
        TestCase testCase = new TestCase();
        int n = Integer.parseInt(br.readLine());
        testCase.n = n;
        return testCase;
    }

    public static void logic(TestCase testCase) {
        // n: A positive integer denoting the number of loops the spiral must have
        int n = testCase.n;

        // TODO: YOUR CODE HERE

        return;
    }

	public static void main(String[] args) throws java.lang.Exception {
        int T = Integer.parseInt(br.readLine());
        for (int i = 0; i < T; i++) {
            logic(read());
            System.out.println(""); // Remember the blank line in between outputs!
        }
    }
}