// name: dna
import java.io.*;

public class DnaGuide {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    static class TestCase {
        String dna;
    }
    
    public static TestCase read() throws java.lang.Exception {
        TestCase testCase = new TestCase();
        String dna = br.readLine();
        testCase.dna = dna;
        return testCase;
    }

    public static void logic(TestCase testCase) {
        // dna: the string of DNA bases, consisting of letters A, T, C, and G
        String dna = testCase.dna;

        // TODO: YOUR CODE HERE

        return;
    }

	public static void main(String[] args) throws java.lang.Exception {
        int T = Integer.parseInt(br.readLine());
        for (int i = 0; i < T; i++) {
            logic(read());
        }
    }
}