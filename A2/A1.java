import util.MyWekaUtils;

/*
 * The Main function for Assignment 2; Uses methods in MyWekaUtils
 * Note: Static methods in MyWekaUtils can be used without instantiating
 */
public class A1 {
    public static void main(String[] args) {
        int[] featureIndices = new int[20];
        String filePath = "";

        System.out.println(args.length);

        /*
         * Check for command line arguments (filepath, featureindices)
         */
        if (args.length < 3) {
            System.exit(0);
        }
        else {
             /*
            * My idea is to execute the python script before running this
            * CSV file with features must already exist
            */
            filePath = args[1]; // Add path to preprocessed csv 

            // pass unknown number of feature indices to command line
            for (int i = 2; i < args.length; i++) {
                featureIndices[i-2] = Integer.parseInt(args[i]); 
            }
        }


        try {
            String[][] csvData = MyWekaUtils.readCSV(filePath);
            String arffData = MyWekaUtils.csvToArff(csvData, featureIndices);
        }
        catch(Exception e) {
            System.out.println(e); // print excpetion that was thrown
        }

        // continue code...

    }
  }
  