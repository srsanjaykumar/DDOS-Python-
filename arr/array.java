package arr;
import java.util.Arrays;
public class array {

    public static void main(String[] args) {
        int number [] ={10 , 50 ,70};
        number[0]=10;
        number[1]=20;
        int data[] = number.clone();
        System.out.println(Arrays.toString(data) + " " + data.hashCode());
        System.out.println(Arrays.toString(number) + " "+ number.hashCode());
    }
}