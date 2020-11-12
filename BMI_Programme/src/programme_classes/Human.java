package programme_classes;

public class Human {

    public String name;
    public double height;
    public double weight;
    BMICalculator myCalculator = new BMICalculator();

    public Human( String nameInput, double heightInput, double weightInput ){
        name = nameInput;
        height = heightInput;
        weight = weightInput;
    }


    public void eat(){
        weight = weight + 2;
    }

    public  void  exercise(){
        weight = weight -2;
    }

    public void greet(){
        double myBmi = myCalculator.computeBMI(this);
        System.out.println("Hey my name is "+ name + "and my BMI is "+myBmi);
    }

    
}
