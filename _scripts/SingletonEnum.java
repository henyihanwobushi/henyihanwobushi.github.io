public enum SingletonEnum {
    INSTANCE;

    public void doSomething() {
        System.out.println("do something");
    }

    public static void main(String[] args) {
        System.out.println(new String("abc") == new String("abc"));
        // prints false
        System.out.println(SingletonEnum.INSTANCE == SingletonEnum.INSTANCE);
        // prints true
    }
}