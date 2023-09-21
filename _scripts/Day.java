public enum Day {
    MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY;

    public static void main(String[] args) {
        for (Day day : Day.values()) {
            switch (day) {
                case SATURDAY:
                case SUNDAY:
                    System.out.println(day.name() + ": Weekends");
                    break;
                default:
                    System.out.println(day.name() + ": Weekdays");
                    break;
            }
        }
    }
}