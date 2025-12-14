import java.util.*;

public class VernamCipher {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextLine()) return;

        String line = sc.nextLine();

        List<String> tokens = new ArrayList<>();
        StringBuilder sb = new StringBuilder();
        boolean inQuotes = false;

        for (int i = 0; i < line.length(); i++) {
            char ch = line.charAt(i);
            if (ch == '"') {
                inQuotes = !inQuotes;
                if (!inQuotes) {
                    tokens.add(sb.toString());
                    sb.setLength(0);
                }
            } else if (inQuotes) {
                sb.append(ch);
            }
        }

        if (tokens.size() < 2) return;

        String msg = tokens.get(0);
        String key = tokens.get(1);

        int[] res = decode(msg, key);

        System.out.print("[");
        for (int i = 0; i < res.length; i++) {
            if (i > 0) System.out.print(", ");
            System.out.print(res[i]);
        }
        System.out.print("]");
    }

    public static int[] decode(String msg, String key) {
        int n = msg.length();
        int[] result = new int[n];
        int k = key.length();

        for (int i = 0; i < n; i++) {
            result[i] = msg.charAt(i) ^ key.charAt(i % k);
        }

        return result;
    }
}
