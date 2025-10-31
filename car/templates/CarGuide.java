// name: car
import java.io.*;

public class CarGuide {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    static class TestCase {
        // This is the class that stores the values in an input!
        float v;
        float x;
    }
    
    // You don't need to do anything here; I've already written it for you! You're welcome
    public static TestCase read() throws java.lang.Exception {
        // Creates a TestCase object to store the inputs
        TestCase testCase = new TestCase();

        // Read in the input and break it up over the colon
        // Ex: turns "12.33:39.33" into ["12.33", "39.33"]
        String[] info = br.readLine().split(":");

        // Turn the string into a decimal value
        testCase.v = Float.parseFloat(info[0]);
        // Turn the string into a decimal value
        testCase.x = Float.parseFloat(info[1]);

        return testCase;
    }

    public static void logic(TestCase testCase) {
        // v: A non-negative decimal value denoting the vehicle’s current speed (in m/s)
        // x: A positive decimal value denoting the obstacle distance from the front of the car (in m)
        float v = testCase.v;
        float x = testCase.x;
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