import util.MyWekaUtils;
import java.util.*;

/*
 * The Main function for Assignment 2; Uses methods in MyWekaUtils
 * Note: Static methods in MyWekaUtils can be used without instantiating
 */
public class A2 {
    public static void main(String[] args) {
        int[] featureIndices;
        Integer model = 0;
        String filePath = "";
        String[][] csvData;
        String arffData;

        /*
         * Check for command line arguments (filepath, featureindices)
         */
        if (args.length < 3) {
            System.out.println("Missing Arguments:\n\t<path to csv>\n\t<model type> (1=Decision Tree, 2=Random Forest, 3=SVM)\n\t<features indices> (column number of feature(s) in CSV)\n\tExample (uses columns 0,1,4,5,8,9): java -cp .:util/weka.jar A2 features.part1.csv 1 0 1 4 5 8 9");
            return;
        }

        /*
        * My idea is to execute the python script before running this
        * CSV file with features must already exist
        */
        filePath = args[0]; // Add path to preprocessed csv 
        model = Integer.parseInt(args[1]);

        featureIndices = new int[args.length - 2];
        // pass unknown number of feature indices to command line
        for (int i = 2; i < args.length; i++) {
            featureIndices[i-2] = Integer.parseInt(args[i]); 
        }
        
        // System.out.println(filePath);
        // System.out.println(model.toString());
        // System.out.println(Arrays.toString(featureIndices));

        try {
            csvData  = MyWekaUtils.readCSV(filePath);
            arffData = MyWekaUtils.csvToArff(csvData, featureIndices);
        }
        catch(Exception e) {
            System.out.println(e); // print excpetion that was thrown
            return;
        }

        // Sanity check
        //for(String[] x: csvData)  System.out.println(Arrays.toString(x));
        //System.out.println(arffData);

        /*
         * Build Classifier and get accuracy %
         */       
        try {
            double eval = MyWekaUtils.classify(arffData, model);
            System.out.println("\nACCURACY: " + Double.toString(eval) + "%");
        }
        catch(Exception e) {
            System.out.println(e); // print excpetion that was thrown
            return;
        }
    }
  }
  