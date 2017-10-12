public class People implements Comparable<People> {
    private String name;
    private int age;

    public People() { }

    public People(String name, int age) {
        this.name = name;
        this.age = age;
    }

    @Override
    public int compareTo(People that) {
        if (this.age < that.age) {
            return -1;
        } else if (this.age > that.age) {
            return 1;
        } else {
            return this.name.compareTo(that.name);
        }
    }

    @Override
    public String toString() {
        return "People " + this.name + " " + this.age;
    }
}
