import programme_classes.Human;
import programme_classes.BMICalculator;

public class Main {

    public static void main(String[] args){
        System.out.println("Running the BMI calculator program");
        Human conor = new Human("Conor", 1.74, 70);
        conor.greet();
        BMICalculator myCalculator = new BMICalculator() ;
        myCalculator.reportOnBMI(conor);
    }
}
