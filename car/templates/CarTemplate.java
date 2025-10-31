// name: car
import java.io.*;

public class CarTemplate {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    static class TestCase {
        float v;
        float x;
    }
    
    public static TestCase read() throws java.lang.Exception {
        TestCase testCase = new TestCase();
        String[] info = br.readLine().split(":");
        testCase.v = Float.parseFloat(info[0]);
        testCase.x = Float.parseFloat(info[1]);
        return testCase;
    }

    public static void logic(TestCase testCase) {
        // v: A non-negative decimal value denoting the vehicle’s current speed (in m/s)
        // x: A positive decimal value denoting the obstacle distance from the front of the car (in m)
        float v = testCase.v;
        float x = testCase.x;

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