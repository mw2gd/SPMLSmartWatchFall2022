import util.MyWekaUtils;

/*
 * The Main function for Assignment 2; Uses methods in MyWekaUtils
 * Note: Static methods in MyWekaUtils can be used without instantiating
 */
public class A1 {
    public static void main(String[] args) {


        /*
         * Check for command line arguments (filepath, featureindices)
         */
        if (args.length < 3) {
            System.out.println("Testing");
            System.exit(0);
        }
        else {
            Integer featureIndices = Integer.parseInt(args[2]); 

            /*
            * My idea is to execute the python script before running this
            * CSV file with features must already exist
            */
            String filePath = args[1]; // Add path to preprocessed csv 
        }


        try {
            String[][] csvData = MyWekaUtils.readCSV(filePath);
            String arffData = csvToArff(csvData, featureIndices);
        }
        catch(Exception e) {
            System.out.println(e); // print excpetion that was thrown
        }

        // continue code...
        
    }
  }
  