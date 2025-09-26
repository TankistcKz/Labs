import java.util.Scanner;

public class Daystoweeks {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("");
        int day = scanner.nextInt();
        
        String result = daysToWeeks(day);
        System.out.println(result);
        scanner.close();
    }
    
    public static String daysToWeeks(int day) {
        int weeks = day / 7;
        int Days = day % 7;
        
        String weekWord = WeekWord(weeks);
        String dayWord = DayWord(Days);
        return weeks + " " + weekWord + " и " + Days + " " + dayWord;
    }
    
    private static String WeekWord(int weeks) {
        if (weeks % 10 == 1 && weeks % 100 != 11) return "неделя";
        if (weeks % 10 >= 2 && weeks % 10 <= 4 && (weeks % 100 < 10 || weeks % 100 >= 20)) return "недели";
        return "недель";
    }
     
    private static String DayWord(int days) {
        if (days % 10 == 1 && days % 100 != 11) return "день";
        if (days % 10 >= 2 && days % 10 <= 4 && (days % 100 < 10 || days % 100 >= 20)) return "дня";
        return "дней";
    }
}