package programme_classes;

public class BMICalculator {
    public BMICalculator(){
    }

    public double computeBMI(Human person){
        double heightSquared = person.height * person.height;
        double bmi = person.weight / heightSquared;
        return  bmi;
    }

    public void reportOnBMI(Human person){
        double bmi = computeBMI(person);
        if(bmi < 18.5){
            System.out.println(person.name + " is underweight" );
        }else if(bmi > 18.5 && bmi < 24.9){
            System.out.println(person.name + " has a healthy BMI :) " );
        }else if(bmi > 24.9){
            System.out.println(person.name + " is overweight " );
        }
    }

}
